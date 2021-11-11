'''
风电制氢系统的最优定容问题（可以包含电池）
一个非凸混合整数二次规划问题

Created on: 20211110

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
import math

import numpy as np
import pandas as pd

from pyomo.environ import *
from pyomo.mpec import *
from pyomo.opt import SolverFactory

from wind_turbine import wind_turbine
from economic import capital_recovery_factor
from advanced_eletrolyser_model import AEL_system
from lcoh_analysis_offgrid_integrated import coordinate_conversion


def optimal_sizing_effvary(wt: wind_turbine, ael:AEL_system, wind_speed_se:pd.Series):
    '''
    接收一个风机对象，电解池对象和一年的风速数据，以最小化LCOH为目标，得到最优容量配置。
    虽然此处接收了一个电解池对象，但实际上只获取了其unit_capex属性，电解池模型还是通过优化的约束条件实现的。

    :param wt:
    :param ael:
    :param wind_speed_se:
    :return:
    '''
    model = ConcreteModel()
    # 参数，风电发电量
    p_w_t = [wt.wt_ac_output(ws) for ws in wind_speed_se]

    # 时间集合
    model.Time = Set(initialize = range(len(wind_speed_se)))

    model.lcoh = Var(within= NonNegativeReals)
    # 电解池功率
    model.p_ele = Var(model.Time)
    # 电解池负荷因子
    model.lf = Var(model.Time)
    # 电解池容量
    model.C_ele = Var(within= NonNegativeReals)
    # 氢气产量
    model.m_H2 = Var(model.Time)

    # 目标，最小化LCOH
    model.obj = Objective(expr= model.lcoh, sense= minimize)

    # 约束，LCOH的定义
    model.c1 = Constraint(expr= model.lcoh * sum(model.m_H2[t] for t in model.Time) ==
                                wt.get_fixed_cost()* capital_recovery_factor(0.05, 20)/365
                                + ael.unit_capex * model.C_ele * capital_recovery_factor(0.05, 20)/365)

    # 约束，电解池的产氢量
    # 首先估算不同负荷因子下的产氢率，得到线性函数关系mh2(kg/h)~lf(1) y = kx+b
    m_H2_lf1 = 1/ael.nom_h2_con_rate*1000 # kg/h
    m_H2_lf0d25 = 0.25/ael.quarter_h2_con_rate*1000 # kg/h
    k = (m_H2_lf1-m_H2_lf0d25)/(1-0.25)
    b = m_H2_lf1 - k
    def h2_production_t(model, t):
        return model.m_H2[t] == k * model.p_ele[t] + b*model.C_ele

    model.c5 = Constraint(model.Time, rule = h2_production_t)

    # 约束，电解池的工作范围
    model.c2 = Constraint(model.Time, rule = lambda model, t: model.lf[t]>=0)
    model.c3 = Constraint(model.Time, rule = lambda model, t: model.lf[t]<=1)
    model.c4 = Constraint(model.Time, rule = lambda model, t: model.p_ele[t]<=p_w_t[t])

    # 约束，负荷因子的定义
    model.c6 = Constraint(model.Time, rule = lambda model, t: model.p_ele[t]== model.lf[t]*model.C_ele)

    opt = SolverFactory("gurobi")
    # 注意，计算非凸的二次规划问题必须要将NonConvex参数设置为2
    opt.options['NonConvex'] = 2
    results = opt.solve(model, tee = True)

    print(f'Electrolyser capacity: {value(model.C_ele)}MW')
    pass


def optimal_sizing_ideal(wt: wind_turbine, ael:AEL_system, wind_speed_se:pd.Series):
    '''
    接收一个风机对象，电解池对象和一年的风速数据，以最小化LCOH为目标，得到最优容量配置

    :param wt:
    :param ael:
    :param wind_speed_se:
    :return:
    '''
    model = ConcreteModel()
    # 参数，风电发电量
    p_w_t = [wt.wt_ac_output(ws) for ws in wind_speed_se]

    # 时间集合
    model.Time = Set(initialize = range(len(wind_speed_se)))

    model.lcoh = Var()
    # 电解池功率
    model.p_ele = Var(model.Time)
    # 电解池容量
    model.C_ele = Var(within= NonNegativeReals)

    # 目标，最小化LCOH
    model.obj = Objective(expr= model.lcoh, sense= minimize)

    # 约束，LCOH的定义
    model.c1 = Constraint(expr= model.lcoh * 20 *sum(model.p_ele[t] for t in model.Time) ==
                                wt.get_fixed_cost()* capital_recovery_factor(0.05, 20)/365
                                + ael.unit_capex * model.C_ele * capital_recovery_factor(0.05, 20)/365)

    # 约束，电解池的工作范围
    model.c2 = Constraint(model.Time, rule = lambda model, t: model.p_ele[t]>=0)
    model.c3 = Constraint(model.Time, rule = lambda model, t: model.p_ele[t]<=model.C_ele)
    model.c4 = Constraint(model.Time, rule = lambda model, t: model.p_ele[t]<=p_w_t[t])

    opt = SolverFactory("gurobi")
    opt.options['NonConvex'] = 2
    results = opt.solve(model, tee = True)

    print(f'Electrolyser capacity: {value(model.C_ele)}MW')

    pass

if __name__ == '__main__':
    # 实例化一个风机，采用Vesta V136-4.2MW参数
    # 注意，额定风速数据v_r未知，通过额定功率4.2MW反算为10.85m/s。hub height也未知，估计为120m。
    wt = wind_turbine(V_ci=3, V_co=25, height=120, r=136 / 2, V_r=10.85, capital_cost=1000, life_time= 20)
    print(f'The rated power is {wt.rated_power()} MW')

    # 实例化一个碱性电解池, 部分参数参考了GreenHydrogen A90
    ael = AEL_system(T=90, P=30, capacity=2.1, unit_capex=1000, om_fixed_factor=0.03, lifetime=20,
                     cold_start_time=2, working_range=(0, 1),
                     nom_hydronge_con_rate=48.65, half_h2_con_rate=45.5, quarter_h2_con_rate=43.14, varying_eff= True)

    # 采用智利某地的数据进行测试
    file_name = './Inputdata/wind_speed_data/' + coordinate_conversion(10.53, -86.13)
    wind_speed_df = pd.read_csv(file_name, header=9).query('YEAR == 2020')
    wind_speed_df.reset_index(drop= True, inplace= True)
    wind_speed = wind_speed_df['WS10M'][0:24]

    optimal_sizing_effvary(wt, ael, wind_speed)