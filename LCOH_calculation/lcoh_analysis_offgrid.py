'''
计算一个风氢系统的lcoh，考虑不同模型对计算结果的影响。

Created on: 20211102

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''

from wind_turbine import wind_turbine
from advanced_eletrolyser_model import *
from economic import capital_recovery_factor

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 打包成函数，方便循环调用
def offgrid_analysis(ele_capacity = 4.2, ele_cs = 2, ele_working_range = (0.1, 1), ele_eff_varying = False):
    # 实例化一个风机，采用Vesta V136-4.2MW参数
    # 注意，额定风速数据v_r未知，通过额定功率4.2MW反算为10.85m/s。hub height也未知，估计为70m。
    wt = wind_turbine(V_ci= 3, V_co=25, height= 70, r=136/2, V_r= 10.85, capital_cost= 1000)
    # print(f'The rated power is {wt.rated_power()} MW')

    # 实例化一个碱性电解池, 部分参数参考了GreenHydrogen A90
    ael = AEL_system(T = 90, P= 30, capacity= ele_capacity, unit_capex= 1000, om_fixed_factor= 0.03, lifetime= 20,
                     cold_start_time= ele_cs, working_range= ele_working_range,
                     nom_hydronge_con_rate=48.65, half_h2_con_rate= 45.5, quarter_h2_con_rate= 43.14)

    # 风速数据
    wind_speed_df = pd.read_csv('./Inputdata/Historical_data.csv')
    # 将时间设置为index
    wind_speed_df.set_index(['time'], inplace= True)
    # 获得某一年全年风速数据
    wind_speed_se = wind_speed_df['WS10m']['20150101:0011':'20151231:2311']
    # # 数据总数
    # print(wind_speed_se.__len__())

    # 首先通过估算capacity factor的方法计算lcoh
    # 计算风机capacity factor, 实际发电量除以额定发电量
    wt_cf_2015 = sum(wt.wt_ac_output(v_wind= wind_speed_se[i]) for i in range(8760))/(wt.rated_power() * 8760)
    print(f'The capacity factor of the wind turbine in 2015 is {wt_cf_2015}')

    # 估算电解池load factor
    ele_lf = wt.rated_power()*wt_cf_2015/ael.get_capacity()
    # print(f'The load factor of electrolyser is estimated to be {ele_lf}')

    # 计算lcoh
    lcoh_1 = lcoh_cf_based(fixed_cost = wt.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=wt.life_time)
                           +ael.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=ael.lifetime,),
                           var_cost = 0,
                           cf = ele_lf,
                           h2_capacity = ael.get_capacity(power_or_h2= 'h2'))
    # print(lcoh_1)

    # 根据实际运行数据，采用不同模型，计算lcoh
    h2_production_list = []
    wind_power_list = []
    for h in range(0,8760):
        # 风机出力
        wind_power_h = wt.wt_ac_output(wind_speed_se[h])
        wind_power_list.append(wind_power_h)
        # 电解池产氢量
        h2_production_list.append(ael.hydrogen_production(power= wind_power_h, varying_eff= ele_eff_varying))

    # 计算lcoh
    lcoh_2 = lcoh_real(fixed_cost= wt.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=wt.life_time)
                           +ael.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=ael.lifetime,),
                       var_cost= 0,
                       annual_production= sum(h2_production_list)
                       )
    print(lcoh_2)
    print(ael.get_cf())
    # fig, ax = plt.subplots()
    # hours = 1000
    # ax.plot(range(0, hours), h2_production_list[0:hours], label= 'h2 produciton', color = 'red')
    # ax1 = ax.twinx()
    # ax1.plot(range(0, hours), wind_power_list[0:hours], label= 'wind power', color = 'blue')
    # ax.legend()
    # plt.show()

    return lcoh_2

# 一个测试
# Model A
offgrid_analysis(ele_cs= 0, ele_working_range=(0,1), ele_eff_varying= False)
# Model B
offgrid_analysis(ele_cs= 0, ele_working_range=(0.1,1), ele_eff_varying= False)
# Model C
offgrid_analysis(ele_cs= 0, ele_working_range=(0.2,1), ele_eff_varying= False)
# Model D
offgrid_analysis(ele_cs= 1, ele_working_range=(0.2,1), ele_eff_varying= False)
# Model E
offgrid_analysis(ele_cs= 2, ele_working_range=(0.2,1), ele_eff_varying= False)
# Model F
offgrid_analysis(ele_cs= 3, ele_working_range=(0.2,1), ele_eff_varying= False)
# Model G
offgrid_analysis(ele_cs= 3, ele_working_range=(0.2,1), ele_eff_varying= True)

# # 计算不同工作范围以及启动时间下的lcoh
# lcoh_dict = {}
# for min_range in [0, 0.05, 0.1, 0.15, 0.2]:
#     #最小负荷因数
#     lcoh_list = []
#     for cs in range(7):
#         # 冷启动时间从0到6小时
#         lcoh_list.append(offgrid_analysis(ele_cs = cs, ele_working_range= (min_range, 1)))
#     lcoh_dict[min_range] = lcoh_list
#
# pd.DataFrame(lcoh_dict).to_excel('./lcoh_off_grid1.xlsx')

# 计算不同容量配置下的lcoh
# lcoh_ls = []
# for ele_ca in [i/10 for i in range(1,61)]:
#     print(ele_ca)
#     lcoh_ls.append(offgrid_analysis(ele_capacity=ele_ca, ele_working_range=(0.05, 1)))
# fig, ax = plt.subplots()
# ax.plot([i/10 for i in range(1,61)], lcoh_ls)
# plt.show()
# # 获取最优容量配置
# print(min(lcoh_ls))
# print([i/10 for i in range(1,61)][lcoh_ls.index(min(lcoh_ls))])