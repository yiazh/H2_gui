# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cal_dialog(object):
    def setupUi(self, Cal_dialog):
        if not Cal_dialog.objectName():
            Cal_dialog.setObjectName(u"Cal_dialog")
        Cal_dialog.resize(427, 131)
        self.label = QLabel(Cal_dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 211, 41))
        self.label.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.pushButton = QPushButton(Cal_dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 90, 93, 28))

        self.retranslateUi(Cal_dialog)
        self.pushButton.clicked.connect(Cal_dialog.close)

        QMetaObject.connectSlotsByName(Cal_dialog)
    # setupUi

    def retranslateUi(self, Cal_dialog):
        Cal_dialog.setWindowTitle(QCoreApplication.translate("Cal_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Cal_dialog", u"Conponents not initialized.", None))
        self.pushButton.setText(QCoreApplication.translate("Cal_dialog", u"OK", None))
    # retranslateUi

