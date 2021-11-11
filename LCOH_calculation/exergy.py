'''
Created on: 20211014
计算氢气在不同状态下的物理和化学Exergy
Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from math import log,sqrt

R = 8.314 # J/mol K
T_0 = 298.15
p_0 = 1

def physical_exergy(T = 298.15, p = 700, c_p = 7/2* R):
    # Calculate the physical exergy of a substance at (T, p)
    phys_ex = c_p * (T - T_0) - T_0 * (c_p*log(T/T_0)-R*log(p/p_0)) # J/mol
    # to kJ/mol
    return phys_ex/1e3

def chem_exergy():
    # kJ/mol
    return 228.61+R/1e3*T_0*log(sqrt(0.21)/0.0313)

if __name__ == '__main__':
    print(physical_exergy(T = 1073, p = 200))
    print(chem_exergy())