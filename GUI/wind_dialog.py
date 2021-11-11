# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_wind_built_dialog(object):
    def setupUi(self, wind_built_dialog):
        if not wind_built_dialog.objectName():
            wind_built_dialog.setObjectName(u"wind_built_dialog")
        wind_built_dialog.resize(364, 128)
        self.pushButton = QPushButton(wind_built_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 80, 93, 28))
        self.label = QLabel(wind_built_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 191, 41))
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.retranslateUi(wind_built_dialog)
        self.pushButton.clicked.connect(wind_built_dialog.exec)

        QMetaObject.connectSlotsByName(wind_built_dialog)
    # setupUi

    def retranslateUi(self, wind_built_dialog):
        wind_built_dialog.setWindowTitle(QCoreApplication.translate("wind_built_dialog", u"Status", None))
        self.pushButton.setText(QCoreApplication.translate("wind_built_dialog", u"OK", None))
        self.label.setText(QCoreApplication.translate("wind_built_dialog", u"Succesfully built", None))
    # retranslateUi

