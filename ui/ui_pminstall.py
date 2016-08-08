# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/pminstall.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PmWindow(object):
    def setupUi(self, PmWindow):
        PmWindow.setObjectName("PmWindow")
        PmWindow.resize(580, 230)
        PmWindow.setMinimumSize(QtCore.QSize(550, 170))
        self.gridLayout = QtWidgets.QGridLayout(PmWindow)
        self.gridLayout.setContentsMargins(4, 8, 4, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(PmWindow)
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
        self.gridLayout.addWidget(self.label_2, 0, 0, 2, 1)
        self.label = QtWidgets.QLabel(PmWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 2, 1)
        self.packageList = PackageView(PmWindow)
        self.packageList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.packageList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packageList.setProperty("showDropIndicator", False)
        self.packageList.setDragDropOverwriteMode(False)
        self.packageList.setAlternatingRowColors(True)
        self.packageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.packageList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.packageList.setShowGrid(False)
        self.packageList.setWordWrap(True)
        self.packageList.setCornerButtonEnabled(False)
        self.packageList.setObjectName("packageList")
        self.packageList.horizontalHeader().setVisible(False)
        self.packageList.horizontalHeader().setStretchLastSection(True)
        self.packageList.verticalHeader().setVisible(False)
        self.packageList.verticalHeader().setDefaultSectionSize(52)
        self.packageList.verticalHeader().setMinimumSectionSize(52)
        self.gridLayout.addWidget(self.packageList, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_size = QtWidgets.QLabel(PmWindow)
        self.label_size.setText("")
        self.label_size.setObjectName("label_size")
        self.horizontalLayout.addWidget(self.label_size)
        spacerItem = QtWidgets.QSpacerItem(152, 21, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_install = QtWidgets.QPushButton(PmWindow)
        self.button_install.setObjectName("button_install")
        self.horizontalLayout.addWidget(self.button_install)
        self.button_cancel = QtWidgets.QPushButton(PmWindow)
        self.button_cancel.setShortcut("Esc")
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.retranslateUi(PmWindow)
        QtCore.QMetaObject.connectSlotsByName(PmWindow)

    def retranslateUi(self, PmWindow):
        _translate = QtCore.QCoreApplication.translate
        PmWindow.setWindowTitle(_translate("PmWindow", "Package Manager Quick Install"))
        self.label.setText(_translate("PmWindow", "Following packages are selected to install. Do you want to install these packages ?"))
        self.packageList.setWhatsThis(_translate("PmWindow", "Package List"))
        self.button_install.setText(_translate("PmWindow", "Install"))
        self.button_cancel.setText(_translate("PmWindow", "Cancel"))

from packageview import PackageView
import data_rc
