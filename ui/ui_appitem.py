# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/appitem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplicationItem(object):
    def setupUi(self, ApplicationItem):
        ApplicationItem.setObjectName("ApplicationItem")
        ApplicationItem.resize(369, 51)
        ApplicationItem.setMinimumSize(QtCore.QSize(0, 50))
        ApplicationItem.setMaximumSize(QtCore.QSize(16777215, 51))
        self.gridLayout_2 = QtWidgets.QGridLayout(ApplicationItem)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.appIcon = QtWidgets.QLabel(ApplicationItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appIcon.sizePolicy().hasHeightForWidth())
        self.appIcon.setSizePolicy(sizePolicy)
        self.appIcon.setMinimumSize(QtCore.QSize(36, 32))
        self.appIcon.setMaximumSize(QtCore.QSize(36, 32))
        self.appIcon.setText("")
        self.appIcon.setPixmap(QtGui.QPixmap(":/data/package.png"))
        self.appIcon.setObjectName("appIcon")
        self.gridLayout_2.addWidget(self.appIcon, 0, 0, 2, 1)
        self.appGenericName = QtWidgets.QLabel(ApplicationItem)
        self.appGenericName.setObjectName("appGenericName")
        self.gridLayout_2.addWidget(self.appGenericName, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(ApplicationItem)
        self.widget.setMinimumSize(QtCore.QSize(0, 18))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.appName = QtWidgets.QLabel(self.widget)
        self.appName.setStyleSheet("color:gray")
        self.appName.setWordWrap(True)
        self.appName.setObjectName("appName")
        self.gridLayout.addWidget(self.appName, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(ApplicationItem)
        QtCore.QMetaObject.connectSlotsByName(ApplicationItem)

    def retranslateUi(self, ApplicationItem):
        _translate = QtCore.QCoreApplication.translate
        ApplicationItem.setWindowTitle(_translate("ApplicationItem", "Application"))
        self.appGenericName.setText(_translate("ApplicationItem", "Web Tarayıcı"))
        self.appName.setText(_translate("ApplicationItem", "Firefox"))

import data_rc
