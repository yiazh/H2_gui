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
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
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
        self.gridLayout_5 = QGridLayout(self.Wind_turbine)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBox_4 = QCheckBox(self.Wind_turbine)
        self.checkBox_4.setObjectName(u"checkBox_4")
        font = QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)

        self.gridLayout_5.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.wt_data = QWidget(self.Wind_turbine)
        self.wt_data.setObjectName(u"wt_data")
        self.wt_data.setEnabled(True)
        self.gridLayout_4 = QGridLayout(self.wt_data)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_24 = QLabel(self.wt_data)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.wt_data)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_28 = QLabel(self.wt_data)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 0, 2, 1, 1)

        self.label_25 = QLabel(self.wt_data)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_2.addWidget(self.label_25, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.wt_data)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_2.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.label_29 = QLabel(self.wt_data)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 1, 2, 1, 1)

        self.label_26 = QLabel(self.wt_data)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 2, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.wt_data)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_2.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.label_30 = QLabel(self.wt_data)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_3 = QRadioButton(self.wt_data)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.wt_data)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_3.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.wt_data)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.wt_stackedWidget = QStackedWidget(self.wt_data)
        self.wt_stackedWidget.setObjectName(u"wt_stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(1, 10, 81, 31))
        self.wt_stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_23 = QLabel(self.page_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(1, 10, 81, 31))
        self.wt_stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMaximumSize(QSize(300, 16777215))
        self.layoutWidget = QWidget(self.page_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 17, 168, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.layoutWidget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setMinimumSize(QSize(110, 0))
        self.label_27.setBaseSize(QSize(85, 10))

        self.horizontalLayout_4.addWidget(self.label_27)

        self.lineEdit_18 = QLineEdit(self.layoutWidget)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_4.addWidget(self.lineEdit_18)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.wt_stackedWidget.addWidget(self.page_3)

        self.gridLayout_4.addWidget(self.wt_stackedWidget, 2, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.wt_data)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 4, 1, 1, 1)


        self.gridLayout_5.addWidget(self.wt_data, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 263, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.Wind_turbine)
        self.PV = QWidget()
        self.PV.setObjectName(u"PV")
        self.checkBox_8 = QCheckBox(self.PV)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(20, 20, 70, 17))
        self.layoutWidget_2 = QWidget(self.PV)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 60, 231, 74))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 0, 0, 1, 1)

        self.lineEdit_31 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_31.setObjectName(u"lineEdit_31")

        self.gridLayout_6.addWidget(self.lineEdit_31, 0, 1, 1, 1)

        self.label_38 = QLabel(self.layoutWidget_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 0, 2, 1, 1)

        self.label_39 = QLabel(self.layoutWidget_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 1, 0, 1, 1)

        self.lineEdit_32 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_32.setObjectName(u"lineEdit_32")

        self.gridLayout_6.addWidget(self.lineEdit_32, 1, 1, 1, 1)

        self.label_40 = QLabel(self.layoutWidget_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 1, 2, 1, 1)

        self.label_41 = QLabel(self.layoutWidget_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 2, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_33.setObjectName(u"lineEdit_33")

        self.gridLayout_6.addWidget(self.lineEdit_33, 2, 1, 1, 1)

        self.label_42 = QLabel(self.layoutWidget_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_6.addWidget(self.label_42, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.PV)
        self.Utility_grid = QWidget()
        self.Utility_grid.setObjectName(u"Utility_grid")
        self.checkBox_5 = QCheckBox(self.Utility_grid)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 10, 101, 31))
        self.checkBox_5.setFont(font)
        self.stackedWidget.addWidget(self.Utility_grid)
        self.Electrolyser_page = QWidget()
        self.Electrolyser_page.setObjectName(u"Electrolyser_page")
        self.aEle = QLabel(self.Electrolyser_page)
        self.aEle.setObjectName(u"aEle")
        self.aEle.setGeometry(QRect(20, 20, 351, 31))
        self.aEle.setStyleSheet(u"font: 18pt \"Arial\";\n"
"")
        self.toolBox = QToolBox(self.Electrolyser_page)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(20, 70, 501, 371))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 100, 30))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_4.sizePolicy().hasHeightForWidth())
        self.page_4.setSizePolicy(sizePolicy2)
        self.layoutWidget1 = QWidget(self.page_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(2, 10, 318, 213))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 2, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.label_57 = QLabel(self.layoutWidget1)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout.addWidget(self.label_57, 3, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.layoutWidget1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.label_58 = QLabel(self.layoutWidget1)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout.addWidget(self.label_58, 4, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.layoutWidget1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 5, 1, 1, 1)

        self.label_59 = QLabel(self.layoutWidget1)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout.addWidget(self.label_59, 5, 2, 1, 1)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.layoutWidget1)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout.addWidget(self.lineEdit_13, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 6, 2, 1, 1)

        self.toolBox.addItem(self.page_4, u"Basic information")
        self.AdvancedSetting = QWidget()
        self.AdvancedSetting.setObjectName(u"AdvancedSetting")
        self.AdvancedSetting.setGeometry(QRect(0, 0, 100, 30))
        self.checkBox = QCheckBox(self.AdvancedSetting)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 81, 20))
        self.VarEffWidget = QWidget(self.AdvancedSetting)
        self.VarEffWidget.setObjectName(u"VarEffWidget")
        self.VarEffWidget.setEnabled(False)
        self.VarEffWidget.setGeometry(QRect(10, 30, 491, 211))
        self.comboBox_2 = QComboBox(self.VarEffWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(240, 10, 81, 22))
        self.layoutWidget2 = QWidget(self.VarEffWidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 227, 182))
        self.gridLayout_3 = QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_19 = QLabel(self.layoutWidget2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.layoutWidget2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_3.addWidget(self.lineEdit_14, 1, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.layoutWidget2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_3.addWidget(self.lineEdit_15, 1, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.layoutWidget2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_3.addWidget(self.lineEdit_19, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.layoutWidget2)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_3.addWidget(self.lineEdit_21, 2, 1, 2, 1)

        self.lineEdit_20 = QLineEdit(self.layoutWidget2)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_3.addWidget(self.lineEdit_20, 3, 0, 2, 1)

        self.lineEdit_23 = QLineEdit(self.layoutWidget2)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_3.addWidget(self.lineEdit_23, 4, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.layoutWidget2)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_3.addWidget(self.lineEdit_22, 5, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.layoutWidget2)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_3.addWidget(self.lineEdit_24, 5, 1, 1, 1)

        self.lineEdit_25 = QLineEdit(self.layoutWidget2)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_3.addWidget(self.lineEdit_25, 6, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.layoutWidget2)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_3.addWidget(self.lineEdit_26, 6, 1, 1, 1)

        self.toolBox.addItem(self.AdvancedSetting, u"Varing efficiecny")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 501, 263))
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
        self.page_6.setGeometry(QRect(0, 0, 100, 30))
        self.checkBox_3 = QCheckBox(self.page_6)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 10, 81, 20))
        self.widget_2 = QWidget(self.page_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 481, 201))
        self.toolBox.addItem(self.page_6, u"Heat generation")
        self.stackedWidget.addWidget(self.Electrolyser_page)
        self.Hydrogen_storage_page = QWidget()
        self.Hydrogen_storage_page.setObjectName(u"Hydrogen_storage_page")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(13)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Hydrogen_storage_page.sizePolicy().hasHeightForWidth())
        self.Hydrogen_storage_page.setSizePolicy(sizePolicy3)
        self.layoutWidget3 = QWidget(self.Hydrogen_storage_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 60, 188, 151))
        self.formLayout_2 = QFormLayout(self.layoutWidget3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_7 = QLineEdit(self.layoutWidget3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_8 = QLabel(self.layoutWidget3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_8 = QLineEdit(self.layoutWidget3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_9 = QLineEdit(self.layoutWidget3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_10)

        self.lineEdit_10 = QLineEdit(self.layoutWidget3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_21 = QLabel(self.Hydrogen_storage_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 20, 301, 31))
        self.label_21.setStyleSheet(u"font: 18pt \"Arial\";\n"
"")
        self.stackedWidget.addWidget(self.Hydrogen_storage_page)
        self.Calculation_page = QWidget()
        self.Calculation_page.setObjectName(u"Calculation_page")
        self.pushButton_2 = QPushButton(self.Calculation_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 370, 81, 31))
        self.label_34 = QLabel(self.Calculation_page)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 20, 271, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_34.setFont(font1)
        self.layoutWidget4 = QWidget(self.Calculation_page)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 100, 384, 241))
        self.gridLayout_7 = QGridLayout(self.layoutWidget4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.layoutWidget4)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_7.addWidget(self.label_35, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.layoutWidget4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_80 = QLabel(self.layoutWidget4)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_7.addWidget(self.label_80, 1, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.layoutWidget4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_7.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.label_36 = QLabel(self.layoutWidget4)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)

        self.spinBox = QSpinBox(self.layoutWidget4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setSingleStep(1)

        self.gridLayout_7.addWidget(self.spinBox, 2, 1, 1, 1)

        self.label_79 = QLabel(self.layoutWidget4)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_7.addWidget(self.label_79, 3, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.layoutWidget4)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_7.addWidget(self.checkBox_15, 3, 1, 1, 1)

        self.label_81 = QLabel(self.layoutWidget4)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_7.addWidget(self.label_81, 4, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.layoutWidget4)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_7.addWidget(self.checkBox_16, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.Calculation_page)
        self.Results_page = QWidget()
        self.Results_page.setObjectName(u"Results_page")
        self.textBrowser = QTextBrowser(self.Results_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 40, 256, 192))
        self.stackedWidget.addWidget(self.Results_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.treeWidget.itemClicked.connect(Form.display_sub_window)
        self.pushButton_2.clicked.connect(Form.calculate)
        self.checkBox_4.clicked.connect(Form.activate_wind)
        self.radioButton_4.clicked.connect(Form.show_wt_speed)
        self.radioButton_3.clicked.connect(Form.show_wt_power)
        self.radioButton_5.clicked.connect(Form.show_wt_cf)
        self.checkBox.clicked.connect(Form.activate_var_eff)
        self.checkBox_2.clicked.connect(Form.activate_onoff)

        self.stackedWidget.setCurrentIndex(2)
        self.wt_stackedWidget.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(2)
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
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"MW", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Number", None))
        self.label_29.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"Capital cost", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"$/MW", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"Power input", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"Wind speed input", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"Capacity factor", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Power", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Speed", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Capacity factor", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Build", None))
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"MW", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Number", None))
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("Form", u"Capital cost", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"$/MW", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.aEle.setText(QCoreApplication.translate("Form", u"Electrolyser", None))
        self.label.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"MW", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Number", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Capex", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"$/MW", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"OM cost", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"$/MW", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Minimum load", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Maximum load", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"% nominal", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Efficiency", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"kg/MWh", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"m3/MWh", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form", u"Basic information", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Enabled", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"MWh/kg", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"MWh/m3", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"kWh/kg", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"kWh/m3", None))

        self.label_14.setText(QCoreApplication.translate("Form", u"Partial load", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Power consumption", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AdvancedSetting), QCoreApplication.translate("Form", u"Varing efficiecny", None))
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
        self.label_6.setText(QCoreApplication.translate("Form", u"Capacity", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Hydrogen storage", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Calculating settings", None))
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
    # retranslateUi

