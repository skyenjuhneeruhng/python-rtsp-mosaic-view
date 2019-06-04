# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_empty.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wEmpty(object):
    def setupUi(self, wEmpty):
        wEmpty.setObjectName("wEmpty")
        wEmpty.resize(670, 501)
        wEmpty.setStyleSheet("background : #333333;")
        self.verticalLayout = QtWidgets.QVBoxLayout(wEmpty)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmEmpty = QtWidgets.QFrame(wEmpty)
        self.frmEmpty.setFrameShape(QtWidgets.QFrame.Box)
        self.frmEmpty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmEmpty.setObjectName("frmEmpty")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmEmpty)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblNote = QtWidgets.QLabel(self.frmEmpty)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lblNote.setFont(font)
        self.lblNote.setStyleSheet("color: rgb(139, 139, 139);")
        self.lblNote.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNote.setObjectName("lblNote")
        self.verticalLayout_2.addWidget(self.lblNote)
        self.verticalLayout.addWidget(self.frmEmpty)

        self.retranslateUi(wEmpty)
        QtCore.QMetaObject.connectSlotsByName(wEmpty)

    def retranslateUi(self, wEmpty):
        _translate = QtCore.QCoreApplication.translate
        self.lblNote.setText(_translate("wEmpty", "NO STREAM"))

