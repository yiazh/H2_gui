'''
计算一个风氢系统的lcoh，考虑不同模型对计算结果的影响。
此版本为集成形式，以符合直观认知的方式构建算例，方便调用。

Created on: 20211105

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''

from wind_turbine import wind_turbine
from advanced_eletrolyser_model import *
from economic import capital_recovery_factor

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 定义一个函数，接受Latitude和Longitude，转化为一个NASA csv文件标准名，以方便分析数据
def coordinate_conversion(latitude, longitude):

    latitude_before_d = str(abs(int(latitude)))
    # 如果不足三位，则用0填充
    while latitude_before_d.__len__()<3:
        latitude_before_d = '0'+latitude_before_d
    # 考虑到所有经纬度均为两位小数
    dot_index = str(latitude).index('.')
    latitude_after_d = str(latitude)[dot_index+1:len(str(latitude))]
    while latitude_after_d.__len__()<4:
        latitude_after_d = latitude_after_d + '0'

    if latitude > 0:
    # 纬度大于零，用北纬表示
        latitude_str = latitude_before_d +'d' +latitude_after_d+'N'
    else:
    # 小于零，用南纬表示
        latitude_str = latitude_before_d +'d' +latitude_after_d+'S'

    longitude_before_d = str(abs(int(longitude)))
    while longitude_before_d.__len__()<3:
        longitude_before_d = '0'+longitude_before_d

    dot_index = str(longitude).index('.')
    longitude_after_d = str(longitude)[dot_index+1:len(str(longitude))]

    while longitude_after_d.__len__()<4:
        longitude_after_d = longitude_after_d + '0'
    if longitude > 0:
        longitude_str = longitude_before_d +'d' +longitude_after_d+'E'
    else:
        longitude_str = longitude_before_d +'d' +longitude_after_d+'W'

    return 'POWER_Point_Hourly_20160101_20201231_' + latitude_str + '_' + longitude_str + '_LST.csv'

# 分析函数
def offgrid_analysis(ael: AEL_system, wt: wind_turbine, wind_speed_se: pd.Series):
    # 此函数暂时接受三个变量，电解池，风机和风速数据
    h2_production_list = []
    wind_power_list = []

    for h in range(0,wind_speed_se.__len__()):
        # 风机出力
        wind_power_h = wt.wt_ac_output(wind_speed_se[h])
        wind_power_list.append(wind_power_h)
        # 电解池产氢量
        h2_production_list.append(ael.hydrogen_production(power= wind_power_h))

    # 计算风机Capacity factor
    wt_cf = sum(wt.wt_ac_output(v_wind=wind_speed_se[i]) for i in range(wind_speed_se.__len__())) / (wt.rated_power() * 8760)

    # 计算lcoh
    lcoh = lcoh_real(fixed_cost= wt.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=wt.life_time)
                           +ael.get_fixed_cost()*capital_recovery_factor(rate=0.07, life=ael.lifetime,),
                       var_cost= 0,
                       annual_production= sum(h2_production_list)
                       )
    # 计算弃风量, MWh
    wind_curtailment = sum([wind_power_list[i]-ael.p[i] for i in range(wind_speed_se.__len__())])

    # 计算总产氢量
    h2_total_production = sum(h2_production_list)/1000
    # 计算电解池的运行小时数
    total_hours = ael.get_cf()*len(wind_speed_se)

    # fig, ax = plt.subplots()
    # hours = 1000
    # ax.plot(range(0, hours), h2_production_list[0:hours], label= 'h2 produciton', color = 'red')
    # ax1 = ax.twinx()
    # ax1.plot(range(0, hours), wind_power_list[0:hours], label= 'wind power', color = 'blue')
    # ax.legend()
    # plt.show()

    # 返回以下结果
    # lcoh, 风机的容量因子，弃风量，总的产氢量，总的电解池工作时间
    return {'lcoh':round(lcoh, 2), 'wind_turbine_cf':round(wt_cf, 2), 'wind_curtailment':round(wind_curtailment, 2),
            'h2_total_production': round(h2_total_production,2), 'total_hours':int(total_hours)}

if __name__ == '__main__':

    # 实例化一个风机，采用Vesta V136-4.2MW参数
    # 注意，额定风速数据v_r未知，通过额定功率4.2MW反算为10.85m/s。hub height也未知，估计为120m。
    wt = wind_turbine(V_ci=3, V_co=25, height=120, r=136 / 2, V_r=10.85, capital_cost=1000, life_time= 20)
    print(f'The rated power is {wt.rated_power()} MW')

    # 实例化一个碱性电解池, 部分参数参考了GreenHydrogen A90
    ael = AEL_system(T=90, P=30, capacity=2.1, unit_capex=1000, om_fixed_factor=0.03, lifetime=20,
                     cold_start_time=2, working_range=(0, 1),
                     nom_hydronge_con_rate=48.65, half_h2_con_rate=45.5, quarter_h2_con_rate=43.14, varying_eff= True)

    # 风速数据
    wind_speed_df = pd.read_csv('./Inputdata/Historical_data.csv')
    # 将时间设置为index
    wind_speed_df.set_index(['time'], inplace=True)
    # 获得2015年全年风速数据
    wind_speed_se = wind_speed_df['WS10m']['20150101:0011':'20151231:2311']

    print(offgrid_analysis(ael=ael, wt=wt, wind_speed_se=wind_speed_se))

