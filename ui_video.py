# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_video.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wVideo(object):
    def setupUi(self, wVideo):
        wVideo.setObjectName("wVideo")
        wVideo.resize(520, 436)
        wVideo.setStyleSheet("background : #333333;")
        self.verticalLayout = QtWidgets.QVBoxLayout(wVideo)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmControlPanel = QtWidgets.QFrame(wVideo)
        self.frmControlPanel.setMaximumSize(QtCore.QSize(16777215, 38))
        self.frmControlPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmControlPanel.setObjectName("frmControlPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmControlPanel)
        self.verticalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.frmControlPanel)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.loUp = QtWidgets.QHBoxLayout()
        self.loUp.setContentsMargins(-1, -1, 0, -1)
        self.loUp.setObjectName("loUp")
        self.frame = QtWidgets.QFrame(self.frmControlPanel)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblAlias = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblAlias.setFont(font)
        self.lblAlias.setStyleSheet("color : white;")
        self.lblAlias.setObjectName("lblAlias")
        self.horizontalLayout.addWidget(self.lblAlias)
        self.loUp.addWidget(self.frame)
        self.wControlPanel = QtWidgets.QWidget(self.frmControlPanel)
        self.wControlPanel.setMaximumSize(QtCore.QSize(67, 16777215))
        self.wControlPanel.setObjectName("wControlPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wControlPanel)
        self.horizontalLayout_2.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnResume = PicButton(self.wControlPanel)
        self.btnResume.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.btnResume.setObjectName("btnResume")
        self.horizontalLayout_2.addWidget(self.btnResume)
        self.btnRecord = PicButton(self.wControlPanel)
        self.btnRecord.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.btnRecord.setObjectName("btnRecord")
        self.horizontalLayout_2.addWidget(self.btnRecord)
        self.loUp.addWidget(self.wControlPanel)
        self.verticalLayout_2.addLayout(self.loUp)
        self.verticalLayout.addWidget(self.frmControlPanel)
        self.frmVideo = QtWidgets.QFrame(wVideo)
        self.frmVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmVideo.setObjectName("frmVideo")
        self.verticalLayout.addWidget(self.frmVideo)

        self.retranslateUi(wVideo)
        QtCore.QMetaObject.connectSlotsByName(wVideo)

    def retranslateUi(self, wVideo):
        _translate = QtCore.QCoreApplication.translate
        self.lblAlias.setText(_translate("wVideo", "Alias"))

from picbutton import PicButton
