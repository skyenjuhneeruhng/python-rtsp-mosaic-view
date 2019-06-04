# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wMain(object):
    def setupUi(self, wMain):
        wMain.setObjectName("wMain")
        wMain.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(wMain)
        self.centralwidget.setStyleSheet("background : #333333;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loGrid = QtWidgets.QGridLayout()
        self.loGrid.setVerticalSpacing(10)
        self.loGrid.setObjectName("loGrid")
        self.verticalLayout.addLayout(self.loGrid)
        wMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet("background : grey;\n"
"color : white;\n"
"border-bottom-style: outset;\n"
"border-bottom-width: 1px;\n"
"border-bottom-color: #222222;")
        self.menubar.setObjectName("menubar")
        wMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(wMain)
        self.statusbar.setStyleSheet("background : grey;\n"
"color : white;\n"
"border-top-style: outset;\n"
"border-top-width: 1px;\n"
"border-top-color: #222222;")
        self.statusbar.setObjectName("statusbar")
        wMain.setStatusBar(self.statusbar)

        self.retranslateUi(wMain)
        QtCore.QMetaObject.connectSlotsByName(wMain)

    def retranslateUi(self, wMain):
        _translate = QtCore.QCoreApplication.translate
        wMain.setWindowTitle(_translate("wMain", "RTSP Viewer"))

