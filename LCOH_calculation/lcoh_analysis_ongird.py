'''
Created on: 20211018

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from advanced_eletrolyser_model import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def grid_connected(unit_capex_ele = 700, capacity_factor = 0.95, figure = False, country = 'DK1', ele_cs = 2):
    # 读取2020年指定国家的日前市场电价
    ele_price_df = pd.read_csv('./Inputdata/elspot_2020.csv')
    ele_price_se = ele_price_df[country]
    ele_price_ls = [1.16*i for i in ele_price_se.tolist()] # $

    # Define an objective capacity factor
    cf = capacity_factor

    #-------------------------Find the cut-off price-------------------------Start
    # Sort the price
    ele_price_ls.sort()
    # Cut-off price
    COP = ele_price_ls[int(ele_price_ls.__len__()*cf)-1]
    print(COP)
    if figure:
        fig, ax = plt.subplots()
        ax.plot(range(ele_price_ls.__len__()), ele_price_ls)
        ax.set_xlabel('Time(s)')
        ax.set_ylabel('Price($/MWh)')
        ax.axvline(x = cf * 366*24, ymin= 0.1, ymax= 0.9, color = 'red')
        ax.axhline(y = COP, xmin=0, xmax= 1, linestyle = 'dashed')
    #-------------------------Find the cut-off price-------------------------End

    # 实例化一个电解池
    ael = AEL_system(T = 90, P= 30, capacity= 1, unit_capex= unit_capex_ele, om_fixed_factor= 0.03, lifetime= 20,
                     cold_start_time= ele_cs, working_range= (0.1, 1),
                     nom_hydronge_con_rate=48.65, half_h2_con_rate= 45.5, quarter_h2_con_rate= 43.14)

    # 将原始的电价数据的单位改成美元
    ele_price_ls = [1.16*i for i in ele_price_se.tolist()]
    time_horizon = range(ele_price_ls.__len__())

    for h in time_horizon:
        # 如果电价高于COP，则关机，如果电价低于COP，则满功率产氢
        if ele_price_ls[h] >= COP:
            ael.shut_down()
        if ael.state == 0 and ele_price_ls[h]<COP:
            ael.cold_start()
        ael.hydrogen_production(power = ael.get_working_range()[1], auto_start= False)

    if figure:
        fig, ax = plt.subplots()
        ax.plot(time_horizon, ael.p)
        ax.set_xlabel('Time(h)')
        ax.set_ylabel('Power(MW)')

    lcoh = lcoh_real(fixed_cost= ael.get_fixed_cost()* capital_recovery_factor(0.07, 20),
              var_cost= ael.get_var_cost(ele_price= ele_price_ls, Time= time_horizon),
              annual_production= sum(ael.h2_production))
    # print(lcoh)
    # print(ael.get_cf())

    return lcoh

country_name = 'DK1'

# 计算不同电解池capex以及load factor下的lcoh。设定冷启动时间为2h
# fig ,ax = plt.subplots()
# ax.set_xlabel('Capacity factor')
# ax.set_ylabel('LCOH')
# cf_array = np.linspace(0.1, 1, 19*4).tolist()
# res_dict = {'capacity factor': cf_array}
# res_least_dict = {'cf':[], 'lcoh':[]}
# for uc in range(800, 1900, 100):
#     # 电解池不同的资本支出
#     lcoh_list = []
#     for cf in cf_array:
#         print(uc, cf)
#         lcoh_list.append(grid_connected(unit_capex_ele= uc, capacity_factor= cf, country= country_name, ele_cs =2))
#     res_dict[f'uc={uc}'] = lcoh_list
#     least = min(lcoh_list)
#     least_index = lcoh_list.index(least)
#     res_least_dict['cf'].append(cf_array[least_index])
#     res_least_dict['lcoh'].append(least)
#     ax.plot(cf_array, lcoh_list, label= f'uc = {uc}')
# ax.legend()
# ax.set_ylim([0, 15])
#
# res_df = pd.DataFrame(res_dict)
# res_df.to_excel('./'+country_name+'_cf_lcoh.xlsx')
#
# res_least_df = pd.DataFrame(res_least_dict)
# res_least_df.to_excel('./'+country_name+'ideal_cf_lcoh_least.xlsx')
#
# plt.show()

# 计算丹麦例子中，不同启动时间下的lcoh区域
country_name = 'DK1'

cf_array = np.linspace(0.1, 1, 19*4).tolist()
res_dict = {'capacity factor': cf_array}
for cs in [0,1,2,3]:
    for uc in [800, 1800]:
        lcoh_list = []
        for cf in cf_array:
            print(uc, cf)
            lcoh_list.append(grid_connected(unit_capex_ele=uc, capacity_factor=cf, country=country_name, ele_cs=cs))
        res_dict[f'uc={uc}'] = lcoh_list
    res_df = pd.DataFrame(res_dict)
    res_df.to_excel('./' + country_name + '_cst='+str(cs)+'_cf_lcoh.xlsx')