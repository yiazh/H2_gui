'''
Created on:20210717

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from PySide2.QtWidgets import *


import Mainwindow

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
        pass

    def JudgeEff(self):
        self.Eff_input.text()
        pass

    def activate_wind(self, checked):
        print(checked)
        if checked:
            self.wt_data.setVisible(True)
        else:
            self.wt_data.setVisible(False)
        pass

    def show_wt_power(self, checked):
        if checked:
            self.wt_stackedWidget.setCurrentIndex(0)

    def show_wt_speed(self, checked):
        if checked:
            self.wt_stackedWidget.setCurrentIndex(1)

    def show_wt_cf(self, checked):
        if checked:
            self.wt_stackedWidget.setCurrentIndex(2)

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

        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = PtX_gui()
    window.show()

    app.exec_()


