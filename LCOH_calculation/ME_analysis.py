'''
分析并网电解池的总成本，平均成本和边际成本

Created on: 20211026

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from economic import capital_recovery_factor
import matplotlib.pyplot as plt
import numpy as np

def ME_curve(CAPEX = 1000, eta_nom = 50, eta_min = 40, price_e = 20, varing_eff = False):

    CAPEX = CAPEX # Overnight cost, $/kW
    price_e = price_e/1e3 # $/MWh --> $/kWh

    eta_nom = eta_nom # kWh/kg
    eta_min = eta_min # $ kWh/kg

    H2_price = 1.65

    FC = CAPEX*capital_recovery_factor(0.05, 20)/8760*eta_nom
    print(f'Fixed cost is {FC} $/kg')
    l = np.linspace(0.05, 1, 100)
    if varing_eff:
        eta = (eta_nom - eta_min)*(l-0.05)/0.95+eta_min
        TC = FC + price_e*eta*l
        VC = price_e*eta*l
        AC = TC/l
        MC = price_e*(eta + (eta_nom -eta_min)/0.95*l)
        MR = H2_price*(1-l/1e8)
        TR = H2_price*l
        MCon = TR - VC
    else:
        TC = FC + price_e*eta_nom*l
        VC = price_e*eta_nom*l
        AC = TC/l
        MC = price_e*eta_nom*(1-l/1e8)
        MR = H2_price*(1-l/1e8)
        TR = H2_price * l
        MCon = TR - VC

    fig, ax = plt.subplots()
    ax.plot(l, TC, label= 'Total cost')
    ax.plot(l, AC, label= 'Average total cost')
    ax.plot(l, MC, label= 'Marginal cost')
    ax.plot(l, MR, label= 'Marginal revenue')
    ax.plot(l, MCon, label= 'Marginal contribution')
    ax.set_ylabel('$/kg')
    ax.set_xlabel('load factor')
    ax.legend()


ME_curve(CAPEX= 600, price_e= 30, varing_eff= True)
plt.show()