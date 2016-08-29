# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/message.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        MessageBox.setObjectName("MessageBox")
        MessageBox.resize(603, 61)
        self.mainLayout = QtWidgets.QHBoxLayout(MessageBox)
        self.mainLayout.setObjectName("mainLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem)
        self.icon = QtWidgets.QLabel(MessageBox)
        self.icon.setMinimumSize(QtCore.QSize(32, 32))
        self.icon.setMaximumSize(QtCore.QSize(32, 32))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.mainLayout.addWidget(self.icon)
        self.label = QtWidgets.QLabel(MessageBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.mainLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem1)

        self.retranslateUi(MessageBox)
        QtCore.QMetaObject.connectSlotsByName(MessageBox)

    def retranslateUi(self, MessageBox):
        _translate = QtCore.QCoreApplication.translate
        MessageBox.setWindowTitle(_translate("MessageBox", "Form"))

