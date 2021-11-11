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
        Form.resize(1000, 600)
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
        self.wind_build.setGeometry(QRect(170, 390, 93, 28))
        self.wind_build.setFont(font)
        self.widget = QWidget(self.Wind_turbine)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 251, 291))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.gridLayout_5.addWidget(self.label_22, 0, 0, 1, 1)

        self.wind_radius = QLineEdit(self.widget)
        self.wind_radius.setObjectName(u"wind_radius")
        font2 = QFont()
        font2.setPointSize(7)
        self.wind_radius.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_radius, 0, 1, 1, 1)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_5.addWidget(self.label_23, 1, 0, 1, 1)

        self.wind_height = QLineEdit(self.widget)
        self.wind_height.setObjectName(u"wind_height")
        self.wind_height.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_height, 1, 1, 1, 1)

        self.label_77 = QLabel(self.widget)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font)

        self.gridLayout_5.addWidget(self.label_77, 2, 0, 1, 1)

        self.wind_ci_speed = QLineEdit(self.widget)
        self.wind_ci_speed.setObjectName(u"wind_ci_speed")
        self.wind_ci_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_ci_speed, 2, 1, 1, 1)

        self.label_78 = QLabel(self.widget)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font)

        self.gridLayout_5.addWidget(self.label_78, 3, 0, 1, 1)

        self.wind_co_speed = QLineEdit(self.widget)
        self.wind_co_speed.setObjectName(u"wind_co_speed")
        self.wind_co_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_co_speed, 3, 1, 1, 1)

        self.label_85 = QLabel(self.widget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font)

        self.gridLayout_5.addWidget(self.label_85, 4, 0, 1, 1)

        self.wind_rate_speed = QLineEdit(self.widget)
        self.wind_rate_speed.setObjectName(u"wind_rate_speed")
        self.wind_rate_speed.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_rate_speed, 4, 1, 1, 1)

        self.label_86 = QLabel(self.widget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font)

        self.gridLayout_5.addWidget(self.label_86, 5, 0, 1, 1)

        self.wind_capex = QLineEdit(self.widget)
        self.wind_capex.setObjectName(u"wind_capex")
        self.wind_capex.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_capex, 5, 1, 1, 1)

        self.label_87 = QLabel(self.widget)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font)

        self.gridLayout_5.addWidget(self.label_87, 6, 0, 1, 1)

        self.wind_opex = QLineEdit(self.widget)
        self.wind_opex.setObjectName(u"wind_opex")
        self.wind_opex.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_opex, 6, 1, 1, 1)

        self.label_88 = QLabel(self.widget)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font)

        self.gridLayout_5.addWidget(self.label_88, 7, 0, 1, 1)

        self.wind_lifetime = QLineEdit(self.widget)
        self.wind_lifetime.setObjectName(u"wind_lifetime")
        self.wind_lifetime.setFont(font2)

        self.gridLayout_5.addWidget(self.wind_lifetime, 7, 1, 1, 1)

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
        self.toolBox.setGeometry(QRect(20, 70, 571, 421))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 571, 281))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_4.sizePolicy().hasHeightForWidth())
        self.page_4.setSizePolicy(sizePolicy2)
        self.widget1 = QWidget(self.page_4)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(340, 10, 223, 97))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget1)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 0, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.widget1)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout.addWidget(self.lineEdit_19, 0, 1, 1, 1)

        self.label_93 = QLabel(self.widget1)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout.addWidget(self.label_93, 0, 2, 1, 1)

        self.label_38 = QLabel(self.widget1)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 1, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.widget1)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout.addWidget(self.lineEdit_20, 1, 1, 1, 1)

        self.label_94 = QLabel(self.widget1)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout.addWidget(self.label_94, 1, 2, 1, 1)

        self.label_39 = QLabel(self.widget1)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.widget1)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.label_95 = QLabel(self.widget1)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout.addWidget(self.label_95, 2, 2, 1, 1)

        self.widget2 = QWidget(self.page_4)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(3, 11, 311, 233))
        self.gridLayout_6 = QGridLayout(self.widget2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget2)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_17 = QLabel(self.widget2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_18 = QLabel(self.widget2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy3.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.label_57 = QLabel(self.widget2)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_6.addWidget(self.label_57, 3, 2, 1, 1)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy3.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.label_58 = QLabel(self.widget2)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_6.addWidget(self.label_58, 4, 2, 1, 1)

        self.label_15 = QLabel(self.widget2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 5, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy3.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_12, 5, 1, 1, 1)

        self.label_59 = QLabel(self.widget2)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_6.addWidget(self.label_59, 5, 2, 1, 1)

        self.label_16 = QLabel(self.widget2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 6, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.widget2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        sizePolicy3.setHeightForWidth(self.lineEdit_13.sizePolicy().hasHeightForWidth())
        self.lineEdit_13.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.lineEdit_13, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.widget2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(70, 0))

        self.gridLayout_6.addWidget(self.comboBox, 6, 2, 1, 1)

        self.toolBox.addItem(self.page_4, u"Basic information")
        self.AdvancedSetting = QWidget()
        self.AdvancedSetting.setObjectName(u"AdvancedSetting")
        self.AdvancedSetting.setGeometry(QRect(0, 0, 571, 281))
        self.checkBox = QCheckBox(self.AdvancedSetting)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 81, 20))
        self.widget3 = QWidget(self.AdvancedSetting)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 40, 324, 63))
        self.gridLayout_3 = QGridLayout(self.widget3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.widget3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_3.addWidget(self.lineEdit_14, 0, 1, 1, 1)

        self.label_19 = QLabel(self.widget3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.widget3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.toolBox.addItem(self.AdvancedSetting, u"Partial load properties")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 571, 281))
        self.OnOffWidget = QWidget(self.page_5)
        self.OnOffWidget.setObjectName(u"OnOffWidget")
        self.OnOffWidget.setEnabled(False)
        self.OnOffWidget.setGeometry(QRect(10, 30, 481, 201))
        self.label_20 = QLabel(self.OnOffWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(11, 38, 115, 16))
        self.checkBox_6 = QCheckBox(self.OnOffWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(11, 11, 91, 20))
        self.lineEdit_27 = QLineEdit(self.OnOffWidget)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(133, 38, 137, 24))
        self.label_31 = QLabel(self.OnOffWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(11, 69, 98, 16))
        self.lineEdit_28 = QLineEdit(self.OnOffWidget)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(133, 69, 137, 24))
        self.checkBox_7 = QCheckBox(self.OnOffWidget)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(11, 111, 101, 20))
        self.label_32 = QLabel(self.OnOffWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(11, 138, 115, 16))
        self.lineEdit_29 = QLineEdit(self.OnOffWidget)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(133, 138, 137, 24))
        self.label_33 = QLabel(self.OnOffWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(11, 169, 98, 16))
        self.lineEdit_30 = QLineEdit(self.OnOffWidget)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(133, 169, 137, 24))
        self.checkBox_2 = QCheckBox(self.page_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 10, 81, 20))
        self.toolBox.addItem(self.page_5, u"On-off properties")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 571, 281))
        self.checkBox_3 = QCheckBox(self.page_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 10, 81, 20))
        self.widget_2 = QWidget(self.page_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 481, 201))
        self.toolBox.addItem(self.page_6, u"Heat generation")
        self.pushButton_4 = QPushButton(self.Electrolyser_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(390, 520, 93, 28))
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
        self.pushButton_2 = QPushButton(self.Calculation_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 370, 81, 31))
        self.layoutWidget = QWidget(self.Calculation_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 100, 384, 241))
        self.gridLayout_7 = QGridLayout(self.layoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.layoutWidget)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_7.addWidget(self.label_35, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_80 = QLabel(self.layoutWidget)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_7.addWidget(self.label_80, 1, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.layoutWidget)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_7.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.label_36 = QLabel(self.layoutWidget)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setSingleStep(1)

        self.gridLayout_7.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label_79 = QLabel(self.layoutWidget)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_7.addWidget(self.label_79, 3, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.layoutWidget)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_7.addWidget(self.checkBox_15, 3, 1, 1, 1)

        self.label_81 = QLabel(self.layoutWidget)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_7.addWidget(self.label_81, 4, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.layoutWidget)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_7.addWidget(self.checkBox_16, 4, 1, 1, 1)

        self.label_97 = QLabel(self.Calculation_page)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(10, 20, 260, 30))
        self.label_97.setFont(font1)
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
        self.widget4 = QWidget(self.Results_page)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 290, 321, 165))
        self.gridLayout_10 = QGridLayout(self.widget4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_10.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widget4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_10.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.label_8 = QLabel(self.widget4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_10.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 3, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_10.addWidget(self.lineEdit_9, 3, 1, 1, 1)

        self.label_10 = QLabel(self.widget4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 4, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_10.addWidget(self.lineEdit_10, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.Results_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 2)

        self.retranslateUi(Form)
        self.treeWidget.itemClicked.connect(Form.display_sub_window)
        self.pushButton_2.clicked.connect(Form.calculate)
        self.checkBox.clicked.connect(Form.activate_var_eff)
        self.checkBox_2.clicked.connect(Form.activate_onoff)
        self.wind_build.clicked.connect(Form.build_wind_turbine)

        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
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
        self.label_90.setText(QCoreApplication.translate("Form", u"PV Panels", None))
        self.label_91.setText(QCoreApplication.translate("Form", u"Utility grid", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Temperature", None))
        self.lineEdit_19.setText(QCoreApplication.translate("Form", u"90", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"\u2103", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Pressure", None))
        self.lineEdit_20.setText(QCoreApplication.translate("Form", u"30", None))
        self.label_94.setText(QCoreApplication.translate("Form", u"Bar", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Lifetime", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"20", None))
        self.label_95.setText(QCoreApplication.translate("Form", u"Year", None))
        self.label.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"MW", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Number", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Capex", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"1000", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"$/kW", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"OM cost", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"0.02", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"Capex", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Minimum load", None))
        self.lineEdit_11.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Maximum load", None))
        self.lineEdit_12.setText(QCoreApplication.translate("Form", u"1.0", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Efficiency", None))
        self.lineEdit_13.setText(QCoreApplication.translate("Form", u"50", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"kWh/kg", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form", u"Basic information", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Efficiency at half load (kWh/kg)", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Efficiency at 0.25 load (kWh/kg)", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AdvancedSetting), QCoreApplication.translate("Form", u"Partial load properties", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Start up time (hour)", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"Hot start", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_27.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Hello world<br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_27.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_27.setText("")
        self.label_31.setText(QCoreApplication.translate("Form", u"Start up cost ($) ", None))
        self.lineEdit_28.setText("")
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"Cold start", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Start up time (hour)", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Start up cost ($) ", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("Form", u"On-off properties", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("Form", u"Heat generation", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Build", None))
        self.label_92.setText(QCoreApplication.translate("Form", u"Electrolyser", None))
        self.label_96.setText(QCoreApplication.translate("Form", u"Hydrogen Storage", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
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
        self.label_98.setText(QCoreApplication.translate("Form", u"Results", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6.6pt;\">Print some calculation information</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"LCOH($/kg)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Wind capacity factor", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Wind curtailment(MWh)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"H2 total production (kg)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Electrolyser total working hours", None))
    # retranslateUi

