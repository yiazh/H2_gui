'''
电解池的物理模型以及一个经典的Alkaline的经验模型

主要参考文献: Low-temperature electrolysis system modelling: A review

'''
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.optimize import minimize
import pandas as pd
from pathlib import Path

import numpy as np

import pytest

F = 96485  # C/mol
R = 8.314  # J/(mol K)
p_0 = 101325  # pa


def Butler_Bolmer(E_act_k, i, i0=3000, alpha=0.5, z=2, T=300):
    # Equation depicting the current density and activation overpotential
    # \left.i=I_{0, k}\left[\exp \left(\frac{\alpha_{k} \cdot z . F \cdot E_{a c t, k}}{R \cdot T}\right)-\exp
    # \left(-\frac{\left(1-\alpha_{k}\right) \cdot z \cdot F \cdot E_{a c t, k}}{R \cdot T}\right)\right]\right]
    A = alpha * z * F / R / T
    B = -(1 - alpha) * z * F / R / T
    return i - i0 * (math.exp(A * E_act_k) - math.exp(B * E_act_k))


def derivative_Butler_bolmer(E_act_k, i, i0=3000, alpha=0.5, z=2, T=300):
    # \frac{dI}{dE_{act}}
    A = alpha * z * F / R / T
    B = -(1 - alpha) * z * F / R / T
    return -i0 * (A * math.exp(A * E_act_k) - B * math.exp(B * E_act_k))

class electrolyser():
    def __init__(self, T=300, p=p_0, A=0.05, i=5000, i0_an=200, i0_ca=100, thickness=1.4e-2, alpha_an=0.5,
                 alpha_ca=0.5):
        self.T = T  # K
        self.p = p  # Pa
        self.A = A  # m2
        self.i = i  # A/m2, current density not current!
        self.I = self.i * self.A
        self.i0_an = i0_an  # A/m2, exchange current density of anode, highly depends on electrode reaction
        self.i0_ca = i0_ca  # A/m2, cathode
        self.thickness = thickness  # m
        self.alpha_an = alpha_an  # charge transfer coefficient, anode
        self.alpha_ca = alpha_ca  # charge transfer coefficient,cathode

    def set_tem(self, T):
        self.T = T

    def H2_production(self, f1=250, f2=0.96):
        # Faraday law
        # kg/s, considering the leak current, eta_faraday is slightly less than one
        # faraday efficiency is also called current efficiency, deviation of which to one is produced by parasitic current
        # refer to: Modeling of advanced alkaline electrolyzers: a system computation approach, 2003
        eta_faraday = (self.i / 10) ** 2 / (f1 + (self.i / 10) ** 2) * f2
        n_H2 = eta_faraday * self.i * self.A / (2 * F)
        m_H2 = n_H2 * 2 / 1000
        return m_H2  # kg/s

    def efficiency(self):
        """
        \eta = \frac{H_{2,p}H_{H\!H\!V,H_2}}{E_{cell}I}
        :return:
        """
        if self.power_input() != 0:
            return self.H2_production() * 142000 / self.power_input() * 1000  #
        else:
            return 0
        """
        The high heat value of hydrogen is 286kJ/mol, responding to around 142kJ/g, 142000kJ/kg
        Another choice is :
        return 1.473/self.E_cell()# 1.473 is the thermal neural voltage, with which the cell is thermal balanced.
        """

    def E_rev_0(self):
        '''
        Standard reversible potential
        Refer to : Low-temperature electrolysis system modelling: A review
        '''
        E_0_T = 1.5184 - 1.5421e-3 * self.T + 9.523e-5 * self.T * math.log(self.T) + 9.84e-8 * self.T ** 2
        return E_0_T

    def E_rev_0_appr(self):
        E_0_T = 1.5184 - 1.5421e-3 * self.T
        return E_0_T

    def E_rev(self, p_H2O=0.5 * p_0):
        '''
        Reversible potential
        '''
        E_rev = self.E_rev_0() + R * self.T / (2 * F) * math.log((self.p - p_H2O) ** 1.5 / (p_H2O))
        return E_rev

    def E_act_an(self):
        act_op = 0.5  # activation over potential
        # Solved by Newton Method
        while math.fabs(Butler_Bolmer(act_op, self.i, i0=self.i0_an, alpha=self.alpha_an, T=self.T)) >= 1e-5:
            slope = derivative_Butler_bolmer(act_op, self.i, i0=self.i0_an, alpha=self.alpha_an, T=self.T)
            act_op = act_op - Butler_Bolmer(act_op, self.i, i0=self.i0_an, alpha=self.alpha_an, T=self.T) \
                     / derivative_Butler_bolmer(act_op, self.i, i0=self.i0_an, alpha=self.alpha_an, T=self.T)
        return act_op

    def E_act_ca(self):
        act_op = 0.5  # activation over potential
        # Solved by Newton Method
        while math.fabs(Butler_Bolmer(act_op, self.i, i0=self.i0_ca, alpha=self.alpha_ca, T=self.T)) >= 1e-5:
            slope = derivative_Butler_bolmer(act_op, self.i, i0=self.i0_ca, alpha=self.alpha_ca, T=self.T)
            act_op = act_op - Butler_Bolmer(act_op, self.i, i0=self.i0_ca, alpha=self.alpha_ca, T=self.T) \
                     / derivative_Butler_bolmer(act_op, self.i, i0=self.i0_ca, alpha=self.alpha_ca, T=self.T)
        return act_op

    # Some approximate approaches to estimate activation overpotential
    # def E_act(self, T_ref=400, mode='Tafel',
    #           p_H2=101325, p_O2=101325, I_0ref=3454, alpha_k=0.25
    #           ):
    #     '''
    #     Activation over-voltage
    #     :param T:Temperature
    #     :param i:Current density
    #     :return: E_act
    #     '''
    #     E = 1.1e5  # activation energy
    #     # I_0k = I_0ref*math.exp(-E/R*(1/self.T-1/T_ref))*(p_H2/p_0)*(p_O2/p_0)**0.5
    #     I_0k = I_0ref
    #     if self.i <= 1.5 * I_0k:
    #         mode = 'symmetry'
    #     else:
    #         mode = 'Tafel'
    #     if mode == 'Tafel':
    #         # The validity domain of this equation is limited to high current density
    #         E_act = R * self.T / (2 * alpha_k * F) * math.log(self.i / I_0k)
    #         return E_act
    #     elif mode == 'symmetry':
    #         E_act = R * self.T / F * math.asin(self.i / (2 * I_0k))
    #         return E_act
    #         pass
    #     else:
    #         pass

    def E_ohm(self, w=0.25):
        # sigma = 0.005139*lamda - 0.0326*(1268*(1/303-1/self.T)) # conductivity of proton exchange membrane S/cm
        # sigma = 2.96396 -0.02371*self.T-0.12269*w+(5.7e-5)*self.T**2 \
        # 		+0.00173*w**2+(4.7e-4)*w-(3.6e-8)*self.T**3 + (2.7e-6)*w**3 -(8.9e-6)*self.T*w**2+(2.4e-7)*self.T**2*w
        # refer to New multi-physics approach for modelling and design of alkaline electrolyzers, eq 31,
        # but the result is negative, weird

        sigma = 0.279844 * (100 * w) - 0.009241 * self.T - 0.000149 * self.T ** 2 - 0.000905 * (100 * w) * self.T \
                + 0.000114 * self.T ** 2 * math.pow((100 * w), 0.1765) + 0.069664 * self.T / (100 * w) - 28.9815 * (
                        100 * w) / self.T
        # refer to: Temperature and Concentration Dependence of the Specific Conductivity of Concentrated Solutions of Potassium Hydroxide
        # S/cm

        E_ohm = self.i / (sigma * 100) * self.thickness
        return E_ohm

    def E_diff(self, I_lim=12000, beta=1.2):
        '''
        Diffusion overvoltage
        :param I_lim: Limiting current density
        :param beta: empiric coefficient
        :return: Diffusion overvoltage
        '''
        E_diff = R * self.T / (2 * beta * F) * math.log(1 + self.i / I_lim)
        return E_diff

    def E_cell(self):
        E_cell = self.E_rev() + self.E_act_an() + self.E_act_ca() + self.E_ohm() + self.E_diff()
        return E_cell

    def power_input(self):
        '''
        :return: W
        '''
        self.power = self.E_cell() * self.i * self.A  # W
        return self.power

    def power_density(self):
        """
        :return: power density [W/m2]
        """
        return self.E_cell() * self.i

    def set_current_density(self, set_i=4000):
        """
        """
        self.i = set_i
        self.I = self.i * self.A

    def set_current(self, set_I = 1000):
        self.I = set_I
        self.i = self.I / self.A

    def temperature_variation(self,
                    H_air=100,  # W/(m2 K)
                    H_water=7000,  # W/(m2 K)
                    time_interval=1  # s
                    ):
        Heat_Capacity = 174  # kJ/celcius
        Area = 0.05
        T_air = 20 + 273.15
        T_water = 50 + 273.15
        heat_generation = (self.E_cell() - 1.473) * self.i * self.A
        Delta_T = (heat_generation + H_air * Area * (T_air - self.T) + H_water * Area * (
                T_water - self.T)) * time_interval / 1000 / Heat_Capacity
        self.T = self.T + Delta_T

def set_power(ele=electrolyser(), power=1000):
    '''
    Given a power output, calculating the corresponding current density.
    If the power demand is out of range, return False
    :param ele:
    :param power:
    :return:
    '''
    ia = 0
    ib = 10000
    if power < electrolyser(i=ia).power_input() or power > electrolyser(i=ib).power_input():
        print('Out of range of work')
        return False
    ic = (ia + ib) / 2
    for i in range(0, 1000):
        if math.fabs(electrolyser(i=ic).power_input() - power) <= 1e-4:
            ele.set_current_density(ic)
            return ic
            break
        else:
            if electrolyser(i=ic).power_input() < power:
                ia = ic
                ic = (ia + ib) / 2
            else:
                ib = ic
                ic = (ia + ib) / 2
    pass

# An emperical model for alkaline electrolysers.
class alkaline_ele(electrolyser):
    def __init__(self, T=300, p=p_0, A=100e-4, i=1000):
        super().__init__(T, p, A, i)
        self.I = i * A

    def E_cell_empirical(self,
                         r1=8.05e-5,  # ohm m2
                         r2=-2.5e-7,  # ohm m2/celcius
                         s=0.08,  # V
                         t1=1.002,  # A-1 m2
                         t2=8.424,  # A-1 m2 celcius
                         t3=247.3e3,  # A-1 m2 celcius **2
                         ):
        """
        An empirical model from Ulleberg
        :param r1: Electrolyte ohmic resistive parameter
        :param r2: Electrolyte ohmic resistive parameter
        :param s: over voltage parameter of electrode
        :param t1: empirical over voltage parameter of electrode
        :param t2: empirical over voltage parameter of electrode
        :param t3: empirical over voltage parameter of electrode
        :return: cell voltage
        """
        assert (t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) * self.i + 1 > 0
        U = self.E_rev() + (r1 + r2 * (self.T - 273.15)) * self.i + s * math.log(
            (t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) * self.i + 1, 10)
        return U

    # Auxiliary functions
    def pUpT(self,
             r1=8.05e-5,  # ohm m2
             r2=-2.5e-7,  # ohm m2/celcius
             s=0.08,  # V
             t1=1.002,  # A-1 m2
             t2=8.424,  # A-1 m2 celcius
             t3=247.3e3,  # A-1 m2 celcius **2
             a=1.5421e-3
             ):
        # Partial derivative
        return -a + r2 / self.A * self.I \
               + s / ((t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) / self.A * self.I + 1) \
               * (-t2 / (self.T - 273.15) ** 2 - 2 * t3 / (self.T - 273.15) ** 3) * self.I / self.A

    def pUpI(self,
             r1=8.05e-5,  # ohm m2
             r2=-2.5e-7,  # ohm m2/celcius
             s=0.08,  # V
             t1=1.002,  # A-1 m2
             t2=8.424,  # A-1 m2 celcius
             t3=247.3e3,  # A-1 m2 celcius **2
             a=1.5421e-3
             ):
        # Partial derivative
        return (r1 + r2 * (self.T - 273.15)) / self.A \
               + s / ((t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) / self.A * self.I + 1) \
               * (t1 + t2 / (self.T - 273.15) + t3 / (self.T - 273.15) ** 2) / self.A

    def power_linearization(self, I_r=1000, T_r=353.15):
        # Linearize the Power (as a fucntion of temperature T and current I) with respect to different reference parameter
        self.I = I_r
        self.T = T_r
        self.i = I_r / self.A
        self.a = self.pUpT() * I_r
        self.b = self.pUpI() * I_r + self.E_cell_empirical()
        self.c = self.power_input() - (self.pUpI() * I_r + self.E_cell_empirical()) * I_r - self.pUpT() * I_r * (T_r-273.15)
        print(f'a = {self.a}, b = {self.b}, c = {self.c}')

    def piece_wise_linearization(self, current, temperature):
        if 1000<=current<=2000:
            if 20<=temperature<=40:
                self.power_linearization(I_r=1500*self.A, T_r = 30 + 273.15)

            if 40<temperature<=60:
                self.power_linearization(I_r=1500*self.A, T_r = 50 + 273.15)

            if 60<temperature<=90:
                self.power_linearization(I_r=1500*self.A, T_r = 75 + 273.15)

        if 2000 < current <= 3000:
            if 20 <= temperature <= 40:
                self.power_linearization(I_r=2500 * self.A, T_r=30 + 273.15)

            if 40 < temperature <= 60:
                self.power_linearization(I_r=2500 * self.A, T_r=50 + 273.15)

            if 60 < temperature <= 90:
                self.power_linearization(I_r=2500 * self.A, T_r=75 + 273.15)

        if 3000 < current <= 5000:
            if 20 <= temperature <= 40:
                self.power_linearization(I_r=4000 * self.A, T_r=30 + 273.15)

            if 40 < temperature <= 60:
                self.power_linearization(I_r=4000 * self.A, T_r=50 + 273.15)

            if 60 < temperature <= 90:
                self.power_linearization(I_r=4000 * self.A, T_r=75 + 273.15)

    def eta_empirical(self):
        # Energy efficiency.
        # Provided that auxiliary heat is supplied, this could be higher than one
        E_tn = 1.473  # thermal neural voltage
        return E_tn / self.E_cell_empirical()

    def power_input(self):
        self.power = self.E_cell_empirical() * self.A * self.i
        return self.power

    def efficiency(self, linearization = True):
        if linearization:
            return self.H2_production() * 142000 / self.power_wrt_I_T() * 1000  #
        else:
            return self.H2_production() * 142000 / self.power_input() * 1000
        return

    def power_wrt_I_T(self):
        """
        # Get the approximate linear representation of power(I, T)

        :return: Power (W)
        """
        self.power = self.a * (self.T-273.15) + self.b * self.I + self.c
        return self.power

def test_3D_physical_model():
    butterfly = electrolyser(T=273, i0_ca=200, i0_an=100, thickness=1.4e-2, p=7 * p_0)
    # Linearization
    # butterfly.power_linearization(I_r=1000 * butterfly.A, T_r=40 + 273.15)

    # # -------------------------------------Voltage vs Temperature-----------------------------------
    # x = []
    # y = []
    # for T in range(20, 80, 1):
    #     butterfly.set_tem(T + 273.15)
    #     x.append(T)
    #     y.append(butterfly.E_cell_empirical(t1=1.002))
    # fig, ax = plt.subplots()  # type:figure.Figure, axes.Axes
    # ax.plot(x, y)
    # ax.grid()  # Make the figure look better
    #
    # # -------------------------------------V-I curve----------------------------------------------
    # x1 = []
    # y1 = []
    # for i in range(500, 4000, 100):
    #     butterfly.set_current_density(i)
    #     x1.append(i)
    #     y1.append(butterfly.E_cell_empirical(t1=1.002))
    # fig, ax = plt.subplots()  # type:figure.Figure, axes.Axes
    # ax.plot(x1, y1, color='tab:red', )
    # ax.grid()  # Make the figure look better

    # ----------------------------------------3D surface-----------------------------------------
    nodes = 100
    current_density = np.linspace(1000, 5000, nodes)
    temperature = np.linspace(20, 80, nodes)
    voltage = np.zeros((nodes, nodes))
    eta = np.zeros((nodes, nodes))
    power_linear = np.zeros((nodes, nodes))
    power = np.zeros((nodes, nodes))

    # 3D plot of U(i,T), scatter
    for i, c in enumerate(current_density):
        for j, T in enumerate(temperature):
            # butterfly.piece_wise_linearization(current=c, temperature=T)
            butterfly.set_tem(T + 273.15)
            butterfly.set_current_density(c)
            # voltage[(j, i)] = butterfly.E_cell_empirical()
            power_linear[(j, i)] = butterfly.power_density()
            eta[(j, i)] = butterfly.efficiency()
            power[(j, i)] = butterfly.power_input()

            # ax2.scatter(c, T, voltage[(i,j)], marker='.', color='grey')

    fig = plt.figure(dpi=100)  # type:figure.Figure
    ax = Axes3D(fig)
    X, Y = np.meshgrid(current_density, temperature)
    ax.plot_surface(X, Y, eta, rstride=1, cstride=1, cmap='plasma', zorder=0.2)
    ax.set_xlabel('Current density(A/$m^2$)')
    ax.set_ylabel('Temperature(℃)')
    ax.set_zlabel('Efficiency')

    fig = plt.figure(dpi=100)  # type:figure.Figure
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, power_linear, rstride=1, cstride=1, cmap='plasma', zorder=0.2)
    ax.set_xlabel('Current density(A/$m^2$)')
    ax.set_ylabel('Temperature(℃)')
    ax.set_zlabel('Power density(W/$m^2$)')
    # ax3.plot_surface(X, Y, power, rstride=1, cstride=1, cmap='Oranges', zorder = 0.3)

    # --------------------------Ulleberg model vs linearization model-----------------------

    # fig, ax = plt.subplots(2, 2, sharex=False, sharey=True)  # type:figure.Figure, axes.Axes
    #
    # # Under different temperature, compare the linear model and ulleberg model
    #
    # # --------------------Fixed temperature----------------------
    # for i, temp in enumerate([40, 80]):
    #     temp = temp
    #     butterfly.set_tem(temp + 273.15)
    #     voltage = []
    #     m_h2 = []
    #     power = []
    #     power_linear = []
    #     eff = []
    #     current_den = range(1000, 4500, 10)
    #     for c in current_den:
    #         butterfly.piece_wise_linearization(current=c, temperature=80)
    #         butterfly.set_current_density(c)
    #         voltage.append(butterfly.E_cell_empirical())
    #         m_h2.append(butterfly.H2_production() * 3600)
    #         power.append(butterfly.power_input())
    #         power_linear.append(butterfly.power_wrt_I_T())
    #         eff.append(butterfly.efficiency())
    #     x = current_den
    #     y = [i / 1000 for i in power_linear]
    #     z = [i / 1000 for i in power]
    #     df = pd.DataFrame({'Current density(A/$m^2$)': x, 'Power(linear)': y, 'Power(Ulleberg)': z})
    #     df.to_excel(f'fixed_temperature_{temp}.xlsx')
    #     ax[i, 0].plot(x, y, label='Linear approximation', color='blue', linestyle='solid')
    #     ax[i, 0].plot(x, z, label='Ulleberg model', color='lightcoral', linestyle='-')
    #     ax[i, 0].set_ylim([0, 4])
    #     ax[i, 0].set_title(f'@Temperature = {temp}℃')
    #     ax[i, 0].set_xlabel('Current density(A/${m^2}$)')
    #     ax[i, 0].set_ylabel('Power(kW)')
    #     ax[i, 0].legend()
    #
    # # #--------------------Fixed current----------------------
    # for i, cd in enumerate([2500, 4000]):
    #     butterfly.set_current_density(cd)
    #     temperature_range = range(30, 90, 1)
    #     voltage = []
    #     m_h2 = []
    #     power = []
    #     power_linear = []
    #     eff = []
    #     for temperature in temperature_range:
    #         # set the temperature of electrolyser to 'temperature'
    #         butterfly.piece_wise_linearization(current=cd, temperature=80)
    #         butterfly.set_tem(temperature + 273.15)
    #         voltage.append(butterfly.E_cell_empirical())
    #         m_h2.append(butterfly.H2_production() * 3600)
    #         power.append(butterfly.power_input())
    #         power_linear.append(butterfly.power_wrt_I_T())
    #         eff.append(butterfly.efficiency())
    #     x = temperature_range
    #     y = [i / 1000 for i in power_linear]
    #     z = [i / 1000 for i in power]
    #
    #     # Save excel files
    #     df = pd.DataFrame({'Temperature(℃)': x, 'Power(linear)': y, 'Power(Ulleberg)': z})
    #     df.to_excel(f'fixed_current_den_{cd}.xlsx')
    #
    #     # Drawing figures
    #     ax[i, 1].plot(x, y, label='Linear approximation', color='blue', linestyle='solid')
    #     ax[i, 1].plot(x, z, label='Ulleberg model', color='lightcoral', linestyle='-')
    #     ax[i, 1].set_ylim([0, 4])
    #     ax[i, 1].set_xlim([20, 100])
    #     ax[i, 1].set_title(f'@Currend density = {cd}A/$m^2$')
    #     ax[i, 1].set_xlabel('Temperature(℃)')
    #     ax[i, 1].set_ylabel('Power(kW)')
    #     ax[i, 1].legend()
    #
    # plt.tight_layout()
    plt.show()

def test_Model_validation():
    # Colors
    Colors = ['navy', 'dodgerblue', 'cyan', 'khaki', 'gold', 'lightcoral']

    # Define a figure
    fig, ax = plt.subplots()

    # Define an electrolyser with pressure of 7bar
    butterfly = electrolyser(T=273, i0_ca=200, i0_an=100, thickness=1.4e-2, p=7 * p_0)
    # The current density range
    current_density = [i for i in range(500, 5000, 10)]

    # line_style = ['solid','dotted','dashed','dashdot']
    # dict_line_tem = dict(zip(temperature_range,line_style))
    for i, temperature in enumerate([35, 53.5, 55, 65, 75, 80]):
        # set the temperature of electrolyser to 'temperature'
        butterfly.set_tem(temperature+273.15)
        voltage = []
        m_h2 = []
        power_density = []
        eff = []
        over_voltage = []
        for c in current_density:
            butterfly.set_current_density(c)
            voltage.append(butterfly.E_cell())
            m_h2.append(butterfly.H2_production() * 3600)
            power_density.append(butterfly.power_density())
            eff.append(butterfly.efficiency())
            over_voltage.append(butterfly.E_ohm())
        ax.plot(current_density, power_density, label=f'Model @T={temperature}℃', linestyle='solid', color = Colors[i])

    #-------------------------------Experimental data---------------------------------
    exp_data_1 = pd.read_excel('./Electrolyser_experiment_data.xlsx', sheet_name= 'Sheet1')
    exp_data_2 = pd.read_excel('./Electrolyser_experiment_data.xlsx', sheet_name= 'Sheet2')

    ax.scatter(exp_data_2.iloc[1:,1], exp_data_2.iloc[1:,3], marker = '.', label = 'Experiment @T=35℃', color = 'navy')
    ax.scatter(exp_data_1.iloc[1:,1], exp_data_1.iloc[1:,3], marker = '.', label = 'Experiment @T=53.5℃', color = 'cyan')
    ax.scatter(exp_data_2.iloc[1:,6], exp_data_2.iloc[1:,8], marker = 'd', label = 'Experiment @T=55℃', color = 'dodgerblue')

    ax.scatter(exp_data_1.iloc[1:,6], exp_data_1.iloc[1:,8], marker = 'd', label = 'Experiment @T=65℃', color = 'khaki')
    ax.scatter(exp_data_1.iloc[1:,11], exp_data_1.iloc[1:,13], marker = '*', label = 'Experiment @T=75℃', color = 'gold')
    ax.scatter(exp_data_2.iloc[1:,11], exp_data_2.iloc[1:,13], marker = '*', label = 'Experiment @T=80℃', color = 'lightcoral')

    ax.set(xlabel = 'Current density(A/$m^2$)', ylabel = 'Power density(W/$m^2$)')
    ax.legend()

    plt.show()
    pass

def test_3D_tangent_plane_based():
    butterfly = alkaline_ele(T=300, A=0.37)

    nodes = 100
    current_density = np.linspace(1000, 5000, nodes)
    temperature = np.linspace(20, 80, nodes)
    voltage = np.zeros((nodes, nodes))
    eta = np.zeros((nodes, nodes))
    power_linear = np.zeros((nodes, nodes))
    power = np.zeros((nodes, nodes))

    butterfly.power_linearization(I_r=1000 * butterfly.A, T_r=40 + 273.15)

    for i, c in enumerate(current_density):
        for j, T in enumerate(temperature):
            # butterfly.piece_wise_linearization(current=c, temperature=T)
            butterfly.set_tem(T + 273.15)
            butterfly.set_current_density(c)
            # voltage[(j, i)] = butterfly.E_cell_empirical()
            power_linear[(j, i)] = butterfly.power_density()
            eta[(j, i)] = butterfly.efficiency(linearization= True)
            power[(j, i)] = butterfly.power_input()

            # ax2.scatter(c, T, voltage[(i,j)], marker='.', color='grey')

    fig = plt.figure(dpi=100)  # type:figure.Figure
    ax = Axes3D(fig)
    X, Y = np.meshgrid(current_density, temperature)
    ax.plot_surface(X, Y, eta, rstride=1, cstride=1, cmap='plasma', zorder=0.2)
    ax.set_xlabel('Current density(A/$m^2$)')
    ax.set_ylabel('Temperature(℃)')
    ax.set_zlabel('Efficiency')

    fig = plt.figure(dpi=100)  # type:figure.Figure
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, power_linear, rstride=1, cstride=1, cmap='plasma', zorder=0.2)
    ax.set_xlabel('Current density(A/$m^2$)')
    ax.set_ylabel('Temperature(℃)')
    ax.set_zlabel('Power density(W/$m^2$)')

    plt.show()

def test_none():
    butterfly = electrolyser(T=90+273.15, i0_ca=200, i0_an=100, thickness=1.4e-2, p=7 * p_0, A=1)
    butterfly.set_current(1800)
    print('hello')
    print(butterfly.H2_production()*3600)



