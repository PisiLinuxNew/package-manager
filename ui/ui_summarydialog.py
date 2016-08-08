# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/summarydialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SummaryDialog(object):
    def setupUi(self, SummaryDialog):
        SummaryDialog.setObjectName("SummaryDialog")
        SummaryDialog.resize(385, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SummaryDialog.sizePolicy().hasHeightForWidth())
        SummaryDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(SummaryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(SummaryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(32, 32))
        self.label_2.setMaximumSize(QtCore.QSize(32, 32))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/data/package-manager.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.startAppInfo = QtWidgets.QLabel(SummaryDialog)
        self.startAppInfo.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.startAppInfo.setFont(font)
        self.startAppInfo.setTextFormat(QtCore.Qt.AutoText)
        self.startAppInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.startAppInfo.setWordWrap(True)
        self.startAppInfo.setObjectName("startAppInfo")
        self.gridLayout.addWidget(self.startAppInfo, 0, 1, 1, 2)
        self.appList = QtWidgets.QListWidget(SummaryDialog)
        self.appList.setObjectName("appList")
        self.gridLayout.addWidget(self.appList, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(307, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.closeButton = QtWidgets.QPushButton(SummaryDialog)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 2, 2, 1, 1)

        self.retranslateUi(SummaryDialog)
        QtCore.QMetaObject.connectSlotsByName(SummaryDialog)

    def retranslateUi(self, SummaryDialog):
        _translate = QtCore.QCoreApplication.translate
        SummaryDialog.setWindowTitle(_translate("SummaryDialog", "Operation Summary"))
        self.startAppInfo.setText(_translate("SummaryDialog", "You can start the new installed application by double-clicking on the list below or later from the applications menu."))
        self.closeButton.setText(_translate("SummaryDialog", "&Ok"))

import data_rc
