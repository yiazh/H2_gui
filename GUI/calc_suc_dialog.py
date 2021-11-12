# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_suc_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_calc_suc_dialog(object):
    def setupUi(self, calc_suc_dialog):
        if not calc_suc_dialog.objectName():
            calc_suc_dialog.setObjectName(u"calc_suc_dialog")
        calc_suc_dialog.resize(330, 120)
        self.pushButton = QPushButton(calc_suc_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 80, 93, 28))
        self.label = QLabel(calc_suc_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 141, 35))
        self.label.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.retranslateUi(calc_suc_dialog)
        self.pushButton.clicked.connect(calc_suc_dialog.close)

        QMetaObject.connectSlotsByName(calc_suc_dialog)
    # setupUi

    def retranslateUi(self, calc_suc_dialog):
        calc_suc_dialog.setWindowTitle(QCoreApplication.translate("calc_suc_dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("calc_suc_dialog", u"OK", None))
        self.label.setText(QCoreApplication.translate("calc_suc_dialog", u"Completed", None))
    # retranslateUi

