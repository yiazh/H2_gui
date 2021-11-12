# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 661)
        Form.setMinimumSize(QSize(1000, 600))
        Form.setMaximumSize(QSize(1800, 1200))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.treeWidget)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(600, 0))
        font = QFont()
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.Component_page = QWidget()
        self.Component_page.setObjectName(u"Component_page")
        self.Component_page.setMaximumSize(QSize(600, 600))
        self.Component_page.setStyleSheet(u"")
        self.label_11 = QLabel(self.Component_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 30, 582, 401))
        self.label_11.setPixmap(QPixmap(u":/GUI/Images/Green-hydrogen-scaled.jpg"))
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.Component_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 460, 331, 31))
        self.label_12.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.label_13 = QLabel(self.Component_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(310, 500, 241, 31))
        self.label_13.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.Component_page)
        self.Wind_turbine = QWidget()
        self.Wind_turbine.setObjectName(u"Wind_turbine")
        self.label_89 = QLabel(self.Wind_turbine)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(10, 20, 260, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_89.setFont(font1)
        self.wind_build = QPushButton(self.Wind_turbine)
        self.wind_build.setObjectName(u"wind_build")
        self.wind_build.setGeometry(QRect(440, 374, 93, 28))
        self.wind_build.setFont(font)
        self.layoutWidget = QWidget(self.Wind_turbine)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 321, 331))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 35))
        self.label_22.setFont(font)

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.wind_radius = QLineEdit(self.layoutWidget)
        self.wind_radius.setObjectName(u"wind_radius")
        self.wind_radius.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setPointSize(7)
        self.wind_radius.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_radius, 0, 1, 1, 1)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 35))
        self.label_23.setFont(font)

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.wind_height = QLineEdit(self.layoutWidget)
        self.wind_height.setObjectName(u"wind_height")
        self.wind_height.setMinimumSize(QSize(0, 35))
        self.wind_height.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_height, 1, 1, 1, 1)

        self.label_77 = QLabel(self.layoutWidget)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(0, 35))
        self.label_77.setFont(font)

        self.gridLayout_5.addWidget(self.label_77, 2, 0, 1, 1)

        self.wind_ci_speed = QLineEdit(self.layoutWidget)
        self.wind_ci_speed.setObjectName(u"wind_ci_speed")
        self.wind_ci_speed.setMinimumSize(QSize(0, 35))
        self.wind_ci_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_ci_speed, 2, 1, 1, 1)

        self.label_78 = QLabel(self.layoutWidget)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(0, 35))
        self.label_78.setFont(font)

        self.gridLayout_5.addWidget(self.label_78, 3, 0, 1, 1)

        self.wind_co_speed = QLineEdit(self.layoutWidget)
        self.wind_co_speed.setObjectName(u"wind_co_speed")
        self.wind_co_speed.setMinimumSize(QSize(0, 35))
        self.wind_co_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_co_speed, 3, 1, 1, 1)

        self.label_85 = QLabel(self.layoutWidget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 35))
        self.label_85.setFont(font)

        self.gridLayout_5.addWidget(self.label_85, 4, 0, 1, 1)

        self.wind_rate_speed = QLineEdit(self.layoutWidget)
        self.wind_rate_speed.setObjectName(u"wind_rate_speed")
        self.wind_rate_speed.setMinimumSize(QSize(0, 35))
        self.wind_rate_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_rate_speed, 4, 1, 1, 1)

        self.label_86 = QLabel(self.layoutWidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 35))
        self.label_86.setFont(font)

        self.gridLayout_5.addWidget(self.label_86, 5, 0, 1, 1)

        self.wind_capex = QLineEdit(self.layoutWidget)
        self.wind_capex.setObjectName(u"wind_capex")
        self.wind_capex.setMinimumSize(QSize(0, 35))
        self.wind_capex.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_capex, 5, 1, 1, 1)

        self.label_87 = QLabel(self.layoutWidget)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 35))
        self.label_87.setFont(font)

        self.gridLayout_5.addWidget(self.label_87, 6, 0, 1, 1)

        self.wind_opex = QLineEdit(self.layoutWidget)
        self.wind_opex.setObjectName(u"wind_opex")
        self.wind_opex.setMinimumSize(QSize(0, 35))
        self.wind_opex.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_opex, 6, 1, 1, 1)

        self.label_88 = QLabel(self.layoutWidget)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(0, 35))
        self.label_88.setFont(font)

        self.gridLayout_5.addWidget(self.label_88, 7, 0, 1, 1)

        self.wind_lifetime = QLineEdit(self.layoutWidget)
        self.wind_lifetime.setObjectName(u"wind_lifetime")
        self.wind_lifetime.setMinimumSize(QSize(0, 35))
        self.wind_lifetime.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_lifetime, 7, 1, 1, 1)

        self.wind_text = QTextEdit(self.Wind_turbine)
        self.wind_text.setObjectName(u"wind_text")
        self.wind_text.setGeometry(QRect(10, 430, 521, 87))
        self.wind_text.setReadOnly(True)
        self.stackedWidget.addWidget(self.Wind_turbine)
        self.PV = QWidget()
        self.PV.setObjectName(u"PV")
        self.label_90 = QLabel(self.PV)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(10, 20, 300, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy1)
        self.label_90.setFont(font1)
        self.stackedWidget.addWidget(self.PV)
        self.Utility_grid = QWidget()
        self.Utility_grid.setObjectName(u"Utility_grid")
        self.label_91 = QLabel(self.Utility_grid)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(10, 20, 300, 30))
        self.label_91.setFont(font1)
        self.stackedWidget.addWidget(self.Utility_grid)
        self.Electrolyser_page = QWidget()
        self.Electrolyser_page.setObjectName(u"Electrolyser_page")
        self.toolBox = QToolBox(self.Electrolyser_page)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(10, 60, 571, 461))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 98, 28))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_4.sizePolicy().hasHeightForWidth())
        self.page_4.setSizePolicy(sizePolicy2)
        self.layoutWidget1 = QWidget(self.page_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(340, 10, 223, 121))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget1)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_37, 0, 0, 1, 1)

        self.Ele_temp = QLineEdit(self.layoutWidget1)
        self.Ele_temp.setObjectName(u"Ele_temp")
        self.Ele_temp.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.Ele_temp, 0, 1, 1, 1)

        self.label_93 = QLabel(self.layoutWidget1)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_93, 0, 2, 1, 1)

        self.label_38 = QLabel(self.layoutWidget1)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_38, 1, 0, 1, 1)

        self.Ele_pre = QLineEdit(self.layoutWidget1)
        self.Ele_pre.setObjectName(u"Ele_pre")
        self.Ele_pre.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.Ele_pre, 1, 1, 1, 1)

        self.label_94 = QLabel(self.layoutWidget1)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_94, 1, 2, 1, 1)

        self.label_39 = QLabel(self.layoutWidget1)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_39, 2, 0, 1, 1)

        self.Ele_life = QLineEdit(self.layoutWidget1)
        self.Ele_life.setObjectName(u"Ele_life")
        self.Ele_life.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.Ele_life, 2, 1, 1, 1)

        self.label_95 = QLabel(self.layoutWidget1)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.label_95, 2, 2, 1, 1)

        self.layoutWidget2 = QWidget(self.page_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(3, 11, 321, 289))
        self.gridLayout_6 = QGridLayout(self.layoutWidget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.Ele_cap = QLineEdit(self.layoutWidget2)
        self.Ele_cap.setObjectName(u"Ele_cap")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Ele_cap.sizePolicy().hasHeightForWidth())
        self.Ele_cap.setSizePolicy(sizePolicy3)
        self.Ele_cap.setMinimumSize(QSize(0, 35))
        self.Ele_cap.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_cap, 0, 1, 1, 1)

        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.Ele_number = QLineEdit(self.layoutWidget2)
        self.Ele_number.setObjectName(u"Ele_number")
        sizePolicy3.setHeightForWidth(self.Ele_number.sizePolicy().hasHeightForWidth())
        self.Ele_number.setSizePolicy(sizePolicy3)
        self.Ele_number.setMinimumSize(QSize(0, 35))
        self.Ele_number.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_number, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.Ele_capex = QLineEdit(self.layoutWidget2)
        self.Ele_capex.setObjectName(u"Ele_capex")
        sizePolicy3.setHeightForWidth(self.Ele_capex.sizePolicy().hasHeightForWidth())
        self.Ele_capex.setSizePolicy(sizePolicy3)
        self.Ele_capex.setMinimumSize(QSize(0, 35))
        self.Ele_capex.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_capex, 2, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_18, 2, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_4, 3, 0, 1, 1)

        self.Ele_opex = QLineEdit(self.layoutWidget2)
        self.Ele_opex.setObjectName(u"Ele_opex")
        sizePolicy3.setHeightForWidth(self.Ele_opex.sizePolicy().hasHeightForWidth())
        self.Ele_opex.setSizePolicy(sizePolicy3)
        self.Ele_opex.setMinimumSize(QSize(0, 35))
        self.Ele_opex.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_opex, 3, 1, 1, 1)

        self.label_57 = QLabel(self.layoutWidget2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_57, 3, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_5, 4, 0, 1, 1)

        self.Ele_min_lf = QLineEdit(self.layoutWidget2)
        self.Ele_min_lf.setObjectName(u"Ele_min_lf")
        sizePolicy3.setHeightForWidth(self.Ele_min_lf.sizePolicy().hasHeightForWidth())
        self.Ele_min_lf.setSizePolicy(sizePolicy3)
        self.Ele_min_lf.setMinimumSize(QSize(0, 35))
        self.Ele_min_lf.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_min_lf, 4, 1, 1, 1)

        self.label_58 = QLabel(self.layoutWidget2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_58, 4, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_15, 5, 0, 1, 1)

        self.Ele_max_lf = QLineEdit(self.layoutWidget2)
        self.Ele_max_lf.setObjectName(u"Ele_max_lf")
        sizePolicy3.setHeightForWidth(self.Ele_max_lf.sizePolicy().hasHeightForWidth())
        self.Ele_max_lf.setSizePolicy(sizePolicy3)
        self.Ele_max_lf.setMinimumSize(QSize(0, 35))
        self.Ele_max_lf.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_max_lf, 5, 1, 1, 1)

        self.label_59 = QLabel(self.layoutWidget2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_59, 5, 2, 1, 1)

        self.label_16 = QLabel(self.layoutWidget2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 35))

        self.gridLayout_6.addWidget(self.label_16, 6, 0, 1, 1)

        self.Ele_nom_eff = QLineEdit(self.layoutWidget2)
        self.Ele_nom_eff.setObjectName(u"Ele_nom_eff")
        sizePolicy3.setHeightForWidth(self.Ele_nom_eff.sizePolicy().hasHeightForWidth())
        self.Ele_nom_eff.setSizePolicy(sizePolicy3)
        self.Ele_nom_eff.setMinimumSize(QSize(0, 35))
        self.Ele_nom_eff.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_6.addWidget(self.Ele_nom_eff, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(70, 35))

        self.gridLayout_6.addWidget(self.comboBox, 6, 2, 1, 1)

        self.toolBox.addItem(self.page_4, u"Basic information")
        self.AdvancedSetting = QWidget()
        self.AdvancedSetting.setObjectName(u"AdvancedSetting")
        self.AdvancedSetting.setGeometry(QRect(0, 0, 571, 341))
        self.Ele_vary_eff = QCheckBox(self.AdvancedSetting)
        self.Ele_vary_eff.setObjectName(u"Ele_vary_eff")
        self.Ele_vary_eff.setGeometry(QRect(10, 10, 81, 20))
        self.VarEffWidget = QWidget(self.AdvancedSetting)
        self.VarEffWidget.setObjectName(u"VarEffWidget")
        self.VarEffWidget.setEnabled(False)
        self.VarEffWidget.setGeometry(QRect(0, 40, 451, 121))
        self.layoutWidget3 = QWidget(self.VarEffWidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 324, 91))
        self.gridLayout_3 = QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.Ele_half_eff = QLineEdit(self.layoutWidget3)
        self.Ele_half_eff.setObjectName(u"Ele_half_eff")
        self.Ele_half_eff.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.Ele_half_eff, 0, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.Ele_qua_eff = QLineEdit(self.layoutWidget3)
        self.Ele_qua_eff.setObjectName(u"Ele_qua_eff")
        self.Ele_qua_eff.setMinimumSize(QSize(0, 35))

        self.gridLayout_3.addWidget(self.Ele_qua_eff, 1, 1, 1, 1)

        self.toolBox.addItem(self.AdvancedSetting, u"Partial load properties")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 98, 28))
        self.OnOffWidget = QWidget(self.page_5)
        self.OnOffWidget.setObjectName(u"OnOffWidget")
        self.OnOffWidget.setEnabled(False)
        self.OnOffWidget.setGeometry(QRect(10, 40, 481, 241))
        self.label_20 = QLabel(self.OnOffWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(11, 30, 161, 35))
        self.label_20.setMinimumSize(QSize(0, 35))
        self.checkBox_6 = QCheckBox(self.OnOffWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(11, 10, 120, 20))
        self.checkBox_6.setMinimumSize(QSize(120, 0))
        self.Ele_hot_time = QLineEdit(self.OnOffWidget)
        self.Ele_hot_time.setObjectName(u"Ele_hot_time")
        self.Ele_hot_time.setGeometry(QRect(190, 30, 137, 35))
        self.Ele_hot_time.setMinimumSize(QSize(0, 35))
        self.label_31 = QLabel(self.OnOffWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(11, 69, 98, 35))
        self.label_31.setMinimumSize(QSize(0, 35))
        self.Ele_hot_cost = QLineEdit(self.OnOffWidget)
        self.Ele_hot_cost.setObjectName(u"Ele_hot_cost")
        self.Ele_hot_cost.setGeometry(QRect(190, 70, 137, 35))
        self.Ele_hot_cost.setMinimumSize(QSize(0, 35))
        self.checkBox_7 = QCheckBox(self.OnOffWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(11, 111, 120, 20))
        self.checkBox_7.setMinimumSize(QSize(120, 0))
        self.label_32 = QLabel(self.OnOffWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(11, 138, 171, 35))
        self.label_32.setMinimumSize(QSize(0, 35))
        self.Ele_cold_time = QLineEdit(self.OnOffWidget)
        self.Ele_cold_time.setObjectName(u"Ele_cold_time")
        self.Ele_cold_time.setGeometry(QRect(190, 138, 137, 35))
        self.Ele_cold_time.setMinimumSize(QSize(0, 35))
        self.label_33 = QLabel(self.OnOffWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(11, 180, 98, 35))
        self.label_33.setMinimumSize(QSize(0, 35))
        self.Ele_cold_cost = QLineEdit(self.OnOffWidget)
        self.Ele_cold_cost.setObjectName(u"Ele_cold_cost")
        self.Ele_cold_cost.setGeometry(QRect(190, 180, 137, 35))
        self.Ele_cold_cost.setMinimumSize(QSize(0, 35))
        self.Ele_on_off = QCheckBox(self.page_5)
        self.Ele_on_off.setObjectName(u"Ele_on_off")
        self.Ele_on_off.setGeometry(QRect(10, 10, 81, 20))
        self.toolBox.addItem(self.page_5, u"On-off properties")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 98, 28))
        self.Heat_bool = QCheckBox(self.page_6)
        self.Heat_bool.setObjectName(u"Heat_bool")
        self.Heat_bool.setGeometry(QRect(10, 10, 81, 20))
        self.widget_2 = QWidget(self.page_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 481, 201))
        self.toolBox.addItem(self.page_6, u"Heat generation")
        self.pushButton_4 = QPushButton(self.Electrolyser_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 560, 93, 28))
        self.pushButton_4.setFont(font)
        self.label_92 = QLabel(self.Electrolyser_page)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(10, 20, 300, 30))
        self.label_92.setFont(font1)
        self.stackedWidget.addWidget(self.Electrolyser_page)
        self.Hydrogen_storage_page = QWidget()
        self.Hydrogen_storage_page.setObjectName(u"Hydrogen_storage_page")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(13)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Hydrogen_storage_page.sizePolicy().hasHeightForWidth())
        self.Hydrogen_storage_page.setSizePolicy(sizePolicy4)
        self.label_96 = QLabel(self.Hydrogen_storage_page)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(10, 20, 300, 30))
        self.label_96.setFont(font1)
        self.stackedWidget.addWidget(self.Hydrogen_storage_page)
        self.Calculation_page = QWidget()
        self.Calculation_page.setObjectName(u"Calculation_page")
        self.Calculate = QPushButton(self.Calculation_page)
        self.Calculate.setObjectName(u"Calculate")
        self.Calculate.setGeometry(QRect(260, 470, 150, 41))
        self.Calculate.setMinimumSize(QSize(150, 35))
        self.layoutWidget4 = QWidget(self.Calculation_page)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 80, 401, 231))
        self.gridLayout_7 = QGridLayout(self.layoutWidget4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.layoutWidget4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 35))
        self.label_35.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.label_35, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 35))
        self.comboBox_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_80 = QLabel(self.layoutWidget4)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(0, 35))
        self.label_80.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.label_80, 1, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.layoutWidget4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(0, 35))
        self.comboBox_7.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_7.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.label_36 = QLabel(self.layoutWidget4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 35))
        self.label_36.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.layoutWidget4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 35))
        self.spinBox.setMaximumSize(QSize(150, 16777215))
        self.spinBox.setMinimum(1)
        self.spinBox.setSingleStep(1)

        self.gridLayout_7.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label_79 = QLabel(self.layoutWidget4)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(0, 35))
        self.label_79.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.label_79, 3, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.layoutWidget4)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setMinimumSize(QSize(0, 35))
        self.checkBox_15.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_7.addWidget(self.checkBox_15, 3, 1, 1, 1)

        self.label_81 = QLabel(self.layoutWidget4)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 35))
        self.label_81.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.label_81, 4, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.layoutWidget4)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setMinimumSize(QSize(0, 35))
        self.checkBox_16.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_7.addWidget(self.checkBox_16, 4, 1, 1, 1)

        self.label_97 = QLabel(self.Calculation_page)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 20, 260, 30))
        self.label_97.setFont(font1)
        self.label_99 = QLabel(self.Calculation_page)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(10, 320, 260, 30))
        self.label_99.setFont(font1)
        self.layoutWidget5 = QWidget(self.Calculation_page)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 360, 401, 37))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setMinimumSize(QSize(170, 35))

        self.horizontalLayout_2.addWidget(self.label_21)

        self.wind_speed_data_display = QLineEdit(self.layoutWidget5)
        self.wind_speed_data_display.setObjectName(u"wind_speed_data_display")
        self.wind_speed_data_display.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.wind_speed_data_display)

        self.wind_speed_data = QToolButton(self.layoutWidget5)
        self.wind_speed_data.setObjectName(u"wind_speed_data")
        sizePolicy3.setHeightForWidth(self.wind_speed_data.sizePolicy().hasHeightForWidth())
        self.wind_speed_data.setSizePolicy(sizePolicy3)
        self.wind_speed_data.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_2.addWidget(self.wind_speed_data)

        self.stackedWidget.addWidget(self.Calculation_page)
        self.Results_page = QWidget()
        self.Results_page.setObjectName(u"Results_page")
        self.Results_page.setFont(font)
        self.label_98 = QLabel(self.Results_page)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(10, 20, 91, 30))
        self.label_98.setFont(font1)
        self.textBrowser = QTextBrowser(self.Results_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 60, 256, 192))
        self.layoutWidget6 = QWidget(self.Results_page)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 290, 381, 205))
        self.gridLayout_10 = QGridLayout(self.layoutWidget6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.LCOH = QLineEdit(self.layoutWidget6)
        self.LCOH.setObjectName(u"LCOH")
        self.LCOH.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.LCOH, 0, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)

        self.Wind_cf = QLineEdit(self.layoutWidget6)
        self.Wind_cf.setObjectName(u"Wind_cf")
        self.Wind_cf.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.Wind_cf, 1, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 1)

        self.Wind_curt = QLineEdit(self.layoutWidget6)
        self.Wind_curt.setObjectName(u"Wind_curt")
        self.Wind_curt.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.Wind_curt, 2, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.label_9, 3, 0, 1, 1)

        self.H2_production = QLineEdit(self.layoutWidget6)
        self.H2_production.setObjectName(u"H2_production")
        self.H2_production.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.H2_production, 3, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.label_10, 4, 0, 1, 1)

        self.Ele_total_hours = QLineEdit(self.layoutWidget6)
        self.Ele_total_hours.setObjectName(u"Ele_total_hours")
        self.Ele_total_hours.setMinimumSize(QSize(0, 35))

        self.gridLayout_10.addWidget(self.Ele_total_hours, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.Results_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)
        self.treeWidget.itemClicked.connect(Form.display_sub_window)
        self.Calculate.clicked.connect(Form.calculate)
        self.Ele_vary_eff.clicked.connect(Form.activate_var_eff)
        self.Ele_on_off.clicked.connect(Form.activate_onoff)
        self.wind_build.clicked.connect(Form.build_wind_turbine)
        self.wind_speed_data.clicked.connect(Form.get_wind_speed_data)
        self.pushButton_4.clicked.connect(Form.build_electrolyser)

        self.stackedWidget.setCurrentIndex(7)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Project", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Power sources", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"Wind turbine", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"Solar panels", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"Utility grid", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"Electrolysis", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"Hydrogen storage", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Form", u"Calculation", None));
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Form", u"Results", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Welcome to hydrogen manager", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Developed by Tom&Jerry", None))
        self.label_89.setText(QCoreApplication.translate("Form", u"Wind turbine parameters", None))
        self.wind_build.setText(QCoreApplication.translate("Form", u"Build", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Radius(m)", None))
        self.wind_radius.setText(QCoreApplication.translate("Form", u"40", None))
        self.wind_radius.setPlaceholderText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Hub height(m)", None))
        self.wind_height.setText(QCoreApplication.translate("Form", u"120", None))
        self.label_77.setText(QCoreApplication.translate("Form", u"Cut-in speed(m/s)", None))
        self.wind_ci_speed.setText(QCoreApplication.translate("Form", u"4", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"Cut-out speed(m/s)", None))
        self.wind_co_speed.setText(QCoreApplication.translate("Form", u"14", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"Rated speed(m/s)", None))
        self.wind_rate_speed.setText(QCoreApplication.translate("Form", u"10.75", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"CAPEX($/kW)", None))
        self.wind_capex.setText(QCoreApplication.translate("Form", u"1000", None))
        self.label_87.setText(QCoreApplication.translate("Form", u"OPEX(CAPEX)", None))
        self.wind_opex.setText(QCoreApplication.translate("Form", u"0.03", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"Lifetime(Year)", None))
        self.wind_lifetime.setText(QCoreApplication.translate("Form", u"20", None))
        self.wind_text.setPlaceholderText(QCoreApplication.translate("Form", u"Status", None))
        self.label_90.setText(QCoreApplication.translate("Form", u"PV Panels", None))
        self.label_91.setText(QCoreApplication.translate("Form", u"Utility grid", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Temperature", None))
        self.Ele_temp.setText(QCoreApplication.translate("Form", u"90", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"\u2103", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Pressure", None))
        self.Ele_pre.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_94.setText(QCoreApplication.translate("Form", u"Bar", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Lifetime", None))
        self.Ele_life.setText(QCoreApplication.translate("Form", u"20", None))
        self.label_95.setText(QCoreApplication.translate("Form", u"Year", None))
        self.label.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.Ele_cap.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"MW", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Number", None))
        self.Ele_number.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Capex", None))
        self.Ele_capex.setText(QCoreApplication.translate("Form", u"1000", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"$/kW", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"OM cost", None))
        self.Ele_opex.setText(QCoreApplication.translate("Form", u"0.02", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Capex", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Minimum load", None))
        self.Ele_min_lf.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Maximum load", None))
        self.Ele_max_lf.setText(QCoreApplication.translate("Form", u"1.0", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Efficiency", None))
        self.Ele_nom_eff.setText(QCoreApplication.translate("Form", u"48.65", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"kWh/kg", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form", u"Basic information", None))
        self.Ele_vary_eff.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Efficiency at half load (kWh/kg)", None))
        self.Ele_half_eff.setText(QCoreApplication.translate("Form", u"45.5", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Efficiency at 0.25 load (kWh/kg)", None))
        self.Ele_qua_eff.setText(QCoreApplication.translate("Form", u"43.14", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AdvancedSetting), QCoreApplication.translate("Form", u"Partial load properties", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Start up time (hour)", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"Hot start", None))
#if QT_CONFIG(tooltip)
        self.Ele_hot_time.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Hello world<br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Ele_hot_time.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Ele_hot_time.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Start up cost ($) ", None))
        self.Ele_hot_cost.setText(QCoreApplication.translate("Form", u"30", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"Cold start", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Start up time (hour)", None))
        self.Ele_cold_time.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Start up cost ($) ", None))
        self.Ele_cold_cost.setText(QCoreApplication.translate("Form", u"100", None))
        self.Ele_on_off.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("Form", u"On-off properties", None))
        self.Heat_bool.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("Form", u"Heat generation", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Build", None))
        self.label_92.setText(QCoreApplication.translate("Form", u"Electrolyser", None))
        self.label_96.setText(QCoreApplication.translate("Form", u"Hydrogen Storage", None))
        self.Calculate.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Operational strategies", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Rule based", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Optimization", None))

        self.label_80.setText(QCoreApplication.translate("Form", u"Operational objective", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Form", u"Minimize cost", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Form", u"Minimize carbon emmision", None))

        self.label_36.setText(QCoreApplication.translate("Form", u"Time resolution (hour)", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"Green certificate", None))
        self.checkBox_15.setText("")
        self.label_81.setText(QCoreApplication.translate("Form", u"Carbon trading", None))
        self.checkBox_16.setText("")
        self.label_97.setText(QCoreApplication.translate("Form", u"Calculation settings", None))
        self.label_99.setText(QCoreApplication.translate("Form", u"Meteorological data", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Wind Speed data", None))
        self.wind_speed_data.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_98.setText(QCoreApplication.translate("Form", u"Results", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Print some calculation information</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"LCOH($/kg)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Wind capacity factor", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Wind curtailment(MWh)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"H2 total production (ton)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Electrolyser total working hours", None))
    # retranslateUi

