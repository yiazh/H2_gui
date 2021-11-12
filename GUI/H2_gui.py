'''
Created on:20210717

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from PySide2.QtWidgets import *
from LCOH_calculation.wind_turbine import wind_turbine
from LCOH_calculation.advanced_eletrolyser_model import AEL_system
from LCOH_calculation.lcoh_analysis_offgrid_integrated import *

from wind_dialog import Ui_wind_built_dialog
from calc_dialog import Ui_Cal_dialog
from calc_suc_dialog import Ui_calc_suc_dialog
import Mainwindow
import pandas as pd

import sys
from qt_material import apply_stylesheet
sys.path.append('C:/PhD/H2_gui')

class PtX_gui(QWidget, Mainwindow.Ui_Form):

    def __init__(self):
        super(PtX_gui, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

    def display_sub_window(self):
        current_item = self.treeWidget.currentItem().text(0)
        print(current_item)
        if current_item == 'Electrolysis':
            self.stackedWidget.setCurrentIndex(4)
        elif current_item == 'Wind turbine':
            self.stackedWidget.setCurrentIndex(1)
        elif current_item == 'Solar panels':
            self.stackedWidget.setCurrentIndex(2)
        elif current_item == 'Utility grid':
            self.stackedWidget.setCurrentIndex(3)
        elif current_item == 'Hydrogen storage':
            self.stackedWidget.setCurrentIndex(5)
        elif current_item == 'Component':
            self.stackedWidget.setCurrentIndex(0)
        elif current_item == 'Calculation':
            self.stackedWidget.setCurrentIndex(6)
        elif current_item == 'Results':
            self.stackedWidget.setCurrentIndex(7)

    def calculate(self):
        try:
            res = offgrid_analysis(ael = self.ael, wt = self.wt, wind_speed_se = self.wind_speed_se)
            self.LCOH.setText(str(res['lcoh']))
            self.H2_production.setText(str(res['h2_total_production']))
            self.Wind_curt.setText(str(res['wind_curtailment']))
            self.Wind_cf.setText(str(res['wind_turbine_cf']))
            self.Ele_total_hours.setText(str(res['total_hours']))
            dialog = QDialog()
            Ui_calc_suc_dialog().setupUi(dialog)
            dialog.exec_()
        # 捕捉一个异常，如果用户未定义组件直接计算则抛出一个对话框
        except AttributeError:
            dialog = QDialog()
            Ui_Cal_dialog().setupUi(dialog)
            dialog.exec_()

    def activate_var_eff(self, checked):
        if checked:
            self.VarEffWidget.setEnabled(True)
        else:
            self.VarEffWidget.setEnabled(False)

    def activate_onoff(self, checked):
        if checked:
            self.OnOffWidget.setEnabled(True)
        else:
            self.OnOffWidget.setEnabled(False)

    def build_wind_turbine(self):
        self.wt = wind_turbine(r = float(self.wind_radius.text()), V_r= float(self.wind_rate_speed.text()),
                               V_co=float(self.wind_co_speed.text()), V_ci= float(self.wind_ci_speed.text()),
                               height= float(self.wind_height.text()), life_time= float(self.wind_lifetime.text()),
                               capital_cost= float(self.wind_capex.text()), OM_cost= float(self.wind_opex.text())
                               )
        dialog = QDialog()
        Ui_wind_built_dialog().setupUi(dialog)
        dialog.exec_()
        self.wind_text.setPlainText(f'The rated power of the wind turbine is {round(self.wt.rated_power(), 2)} MW')
        pass

    def get_wind_speed_data(self):
        ws_path = QFileDialog.getOpenFileName(self, 'Select wind speed data (NASA) format',
                                              '../LCOH_calculation/Inputdata/wind_speed_data', 'CSV(*.csv)')
        try:
            wind_speed_df = pd.read_csv(ws_path[0], header= 9).query('YEAR == 2020')
            wind_speed_df.reset_index(drop = True, inplace = True)
            self.wind_speed_se = wind_speed_df['WS10M']
            print(self.wind_speed_se)
            self.wind_speed_data_display.setText(ws_path[0])
        except:
            pass
        pass

    def build_electrolyser(self):
        if self.Ele_on_off.isChecked():
            cst = float(self.Ele_cold_time.text())
        else:
            cst = 0
        self.ael = AEL_system(T = float(self.Ele_temp.text()), P= float(self.Ele_pre.text()),
                              capacity= float(self.Ele_cap.text()), unit_capex= float(self.Ele_capex.text()),
                              om_fixed_factor= float(self.Ele_opex.text()), lifetime= float(self.Ele_life.text()),
                              cold_start_time= cst,
                              working_range= (float(self.Ele_min_lf.text()), float(self.Ele_max_lf.text())),
                              nom_hydronge_con_rate= float(self.Ele_nom_eff.text()),
                              half_h2_con_rate=float(self.Ele_half_eff.text()),
                              quarter_h2_con_rate=float(self.Ele_qua_eff.text()),
                              varying_eff= self.Ele_vary_eff.isChecked()
                              )
        dialog = QDialog()
        Ui_wind_built_dialog().setupUi(dialog)
        dialog.exec_()
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = PtX_gui()
    apply_stylesheet(app, theme='light_blue.xml')

    window.show()
    app.exec_()


