'''
Created on: 20211018

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from abc import ABC, abstractmethod
from LCOH_calculation.economic import capital_recovery_factor
# from electrolyser import *

# def faraday_fun(current):
#     return current/(2 * F) *2e-3 * 3600 # kgH2/h

# Note that in terms of electrolysis, there are three levels: cell, stack and system. Here we define
# an electrolysis system, which includes bop etc.
class AbstractElectrolysisSystem(ABC):

    # 抽象类，定义了电解池应具有的API。
    # 抽象方法必须被继承
    @abstractmethod
    def hydrogen_production(self, power, fixed_eff = True):
        """
        Having electrolyser power as input and hydrogen production rate as output.

        :param power: MW AC
        :return: hydrogen production rate: kg/h
        """
        pass

    @abstractmethod
    def get_temp_pre(self):
        """
        Get temperature (celcius) and pressure (bar)

        :return: (T, P)
        """
        pass

    @abstractmethod
    def cold_start(self):
        pass

    @abstractmethod
    def shut_down(self):
        pass

    @abstractmethod
    def get_working_range(self):
        """
        Get the working range: minimum power and maximum power (p_min, p_max)

        :return: (p_min, p_max)
        """
        pass

    @abstractmethod
    def get_fixed_cost(self):
        """

        :return: capex $
        """
        pass

    @abstractmethod
    def get_var_cost(self):
        pass


class AEL_system(AbstractElectrolysisSystem):

    def __init__(self, T, P, capacity, unit_capex, om_fixed_factor, lifetime, cold_start_time, working_range,
                 nom_hydronge_con_rate = 48.65, half_h2_con_rate = 45.5, quarter_h2_con_rate = 43.14, varying_eff = False):
        """

        :param T: Temperature ℃
        :param P: Pressure bar
        :param capacity: MW
        :param unit_capex: $/kW
        :param om_fixed_factor:
        :param lifetime: years
        :param cold_start_time: hours
        :param working_range: 工作范围，元组（0~1，0~1?），对应最小和最大负荷因数
        :param nom_hydronge_con_rate: 最大负荷下的氢气转化率，kWh/kg
        :param half_h2_con_rate: 半负荷下氢气转化率， kWh/kg
        :param quarter_h2_con_rate: 四分之一负荷下氢气转化率， kWh/kg
        """
        self.T = T
        self.P = P
        self.capacity = capacity
        self.unit_capex = unit_capex * 1000 # $/MW
        self.om_fixed_factor = om_fixed_factor # 固定运行成本占资产成本的比例
        self.lifetime = lifetime
        self.cold_start_time = cold_start_time # hours
        self.working_range_dimensionless = working_range
        self.working_range = (working_range[0]*capacity, working_range[1]*capacity) # 工作范围, MW

        # 电解池在不同负荷时的转换率
        self.nom_h2_con_rate = nom_hydronge_con_rate
        self.half_h2_con_rate = half_h2_con_rate
        self.quarter_h2_con_rate = quarter_h2_con_rate

        self.varying_eff = varying_eff
        self.startup_time = 0

        # 固定成本，电解池实例化后为一常数
        self.capex = capacity * self.unit_capex # $
        self.om_fixed = capacity * self.unit_capex * self.om_fixed_factor # $

        # 此处用列表储存不同时刻的产率，方便计算成本
        self.p = []
        self.h2_production = []

        # 状态变量state，0表示关闭，1到cold_start_time均表示启动中，cold_start_time+1表示工作中
        self.state = 1 + self.cold_start_time

        # p_max不同于capacity，是指当前可用容量，取决于state。运行状态等于capacity，关机状态为0.
        self.p_max = self.capacity
        pass

    def get_fixed_cost(self):
        # 对外接口，获取固定成本，单位为$
        return self.om_fixed + self.capex

    def get_var_cost(self, ele_price: [], Time: []):
        # 可变成本，取决于电价和运行时间，两者皆用列表表示，$ 仅适用于并网模式
        return sum(self.p[i]* ele_price[i] for i in Time)

    def get_temp_pre(self):
        # 获取温度（摄氏度）和压力（bar）
        # 对外提供接口，用于计算物理和化学exergy
        return (self.T, self.P)

    def get_working_range(self):
        return self.working_range

    def get_working_range_de(self):
        # 返回无量纲的工作范围，即负荷因子的范围
        return self.working_range_dimensionless

    def hydrogen_production(self, power, auto_start = True):
        """
        输入功率MW，输出产氢率kg/h

        :param power: power input (MW)
        :param fixed_eff: Default True
        :return: hydrogen production rate, kg/h
        """
        if auto_start:
            # 做这样一个判断，如果上一时刻是关机的，并且当前时刻的功率输入在正常范围内，则冷启动。
            # 如果启动与否取决于外界信号，则自启动设置为False
            if self.state == 0 and self.working_range[0]<= power <= self.working_range[1]:
                self.cold_start()

        if self.state == 0:
            # 收到关机信号后，state变量置为0，并且设置p_max为0
            self.p_max = 0
        elif 0 < self.state <= self.cold_start_time:
            # 收到启动信号后，state变量置为1，并且每次计算加1，直到大于启动所需时间。
            self.p_max = 0
            self.state += 1
        else:
            self.state = 1 + self.cold_start_time
            self.p_max = self.working_range[1]


        if  self.working_range[0]<= power <= self.p_max:
            # 如果输入功率在工作范围内，正常运行。
            self.p.append(power)
            if self.varying_eff:
                # 分段线性，依据power不同，采用不同斜率和截距。
                if power >= 0.5 * self.p_max:
                    conversion_rate = 6.3*(power/self.p_max)+42.35 # kW/(kg/h)
                elif 0.25*self.p_max <= power < 0.5 * self.p_max:
                    conversion_rate = 9.44 * (power/self.p_max)+40.78
                elif power < 0.25 *self.p_max:
                    conversion_rate = 43.14

            else:
                # 固定转化率，采用名义值
                conversion_rate = self.nom_h2_con_rate

            # 氢气产量（kg/h），注意power的单位默认为MW，此处乘以1000转换为kW. 后面也是一样
            self.h2_production.append(power / conversion_rate * 1e3)
            # 返回当前时刻氢气产量
            return power / conversion_rate * 1e3

        elif power< self.working_range[0]:
            # 输入功率小于安全范围内最小值，关机，不产氢
            self.shut_down()
            self.h2_production.append(0)
            self.p.append(0)
            return 0

        elif power > self.p_max:
            # 输入功率大于工作上限，以最大功率计算
            self.p.append(self.p_max)
            self.h2_production.append(self.p_max / self.nom_h2_con_rate *1e3)
            return self.p_max / self.nom_h2_con_rate *1e3

    def cold_start(self):
        self.startup_time = self.startup_time + 1
        self.state = 1
        pass

    def shut_down(self):
        self.state = 0
        pass

    def get_cf(self):
        # 根据实际生产情况，计算平均负荷因数
        # 注意，此处需要用额定产氢量计算
        return sum(self.h2_production)/(self.get_capacity(power_or_h2= 'h2')*8760)

    def get_capacity(self, power_or_h2 = 'power'):
        '''
        # 对外接口，获取容量

        :param power_or_h2: 如果是power，则返回功率容量；h2则返回产氢容量
        :return:
        '''
        if power_or_h2 == 'power':
            return self.capacity
        elif power_or_h2 == 'h2':
            return self.capacity*1e3/self.nom_h2_con_rate

    def get_total_hydrogen_production(self):
        # 获取总的产氢量
        return sum(self.h2_production)

def lcoh_real(fixed_cost, var_cost, annual_production):
    '''
    根据实际运行情况计算lcoh，注意此处采用了年金+年可变成本 除以年产量的方法。另外也可以用生命周期的方法。
    单位：$/kg

    :param fixed_cost:
    :param var_cost:
    :param annual_production:
    :return:
    '''
    return (fixed_cost + var_cost)/annual_production

def lcoh_cf_based(fixed_cost, var_cost, cf, h2_capacity, leap_year = False):
    '''
    该函数提供了一个估算lcoh的方法，即采用capacity factor而非真实产量。

    :param fixed_cost: 固定成本，需转化为年金
    :param var_cost: 可变成本
    :param cf: 容量因子
    :param h2_capacity: 产氢能力，kg/h
    :return: lcoh
    '''
    if not leap_year:
        return (fixed_cost + var_cost)/(8760 * h2_capacity * cf)
    else:
        return (fixed_cost + var_cost) / (8784 * h2_capacity * cf)

if __name__ == '__main__':
    a = AEL_system(T = 90, P= 30, capacity= 14,
                   unit_capex= 700, om_fixed_factor= 0.03, lifetime= 20, cold_start_time=2, working_range= (0.1, 1))
    year = range(0, 365 * 24)
    ele_price = [30] * 365 * 24
    for h in year:
        if h == 10:
            a.shut_down()
        if h == 105:
            a.cold_start()
        a.hydrogen_production(14)
    print(a.get_fixed_cost())
    print(a.get_var_cost(ele_price=ele_price, Time= year))
    print(sum(a.h2_production))
    lcoh = (a.get_fixed_cost() * capital_recovery_factor(0.07, 20) + a.get_var_cost(ele_price=ele_price, Time= year)) / sum(a.h2_production)
    print(lcoh)
    print(a.get_cf())