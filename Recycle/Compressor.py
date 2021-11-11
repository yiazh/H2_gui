'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from AbstractComponent import AbstractCompressor
import math
R = 8.314

class Compressor(AbstractCompressor):
    def __init__(self,eta_c = 0.75):
        self.eta_c = 0.75
        self.setOperatingPara()

    def setOperatingPara(self, P_in = 35, P_out = 50, gamma = 1.4, T_in = 50, mass_flow_rate = 0.01, molar_mass = 2):
        '''

        :param P_in: inlet pressure
        :param P_out: outlet pressure
        :param gamma: adiabatic efficient
        :param T_in: inlet temperature
        :param mass_flow_rate: g/s
        :param molar_mass: molar mass of inlet gas
        :return:
        '''
        self.P_in = P_in
        self.P_out = P_out
        self.gamma = gamma
        self.T_in = T_in
        self.mass_flow_rate = mass_flow_rate
        self.molar_mass = molar_mass

    def power(self):
        '''
        power consumed by compressor
        :return: power, W
        '''
        p = (R*(self.T_in+273.15))/(self.molar_mass*(self.gamma-1)*self.eta_c)*\
            (math.pow((self.P_out/self.P_in),(self.gamma-1)/self.gamma)-1)*self.mass_flow_rate
        return p

    def getPowerToMassFlowRate(self):
        '''

        :return: MW/kg/h
        '''
        self.setOperatingPara(mass_flow_rate=1000/3600)
        return self.power()/1e6

if __name__ == '__main__':
    a = Compressor()
    print(a.getPowerToMassFlowRate())