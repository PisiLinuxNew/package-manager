# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/basketdialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BasketDialog(object):
    def setupUi(self, BasketDialog):
        BasketDialog.setObjectName("BasketDialog")
        BasketDialog.resize(630, 483)
        BasketDialog.setStyleSheet("#Basket {\n"
"background-color: rgb(164, 164, 164);\n"
"border:0px solid white ;\n"
"border-radius:4px;\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(BasketDialog)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Basket = QtWidgets.QWidget(BasketDialog)
        self.Basket.setStyleSheet("#packageList, #extraList {\n"
"    border:1px solid #888;\n"
"    border-radius:3px;\n"
"    background-color:rgba(252,252,252,100);\n"
"    color:rgba(20,20,20);\n"
"}\n"
"QLabel { color:rgb(20,20,20); }")
        self.Basket.setObjectName("Basket")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Basket)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.Basket)
        self.widget.setMinimumSize(QtCore.QSize(0, 26))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 26))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"\n"
"border:0px solid #666;\n"
"border-top-left-radius:4px;\n"
"border-top-right-radius:4px;\n"
"border-bottom:1px solid #999;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(4, 0, 3, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setIndent(3)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setStyleSheet("color:rgb(20,20,20);")
        self.cancelButton.setText("")
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.Basket)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.packageList = PackageView(self.widget_2)
        self.packageList.setMinimumSize(QtCore.QSize(400, 0))
        self.packageList.setStyleSheet("")
        self.packageList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.packageList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.packageList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.packageList.setProperty("showDropIndicator", False)
        self.packageList.setDragDropOverwriteMode(False)
        self.packageList.setAlternatingRowColors(False)
        self.packageList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.packageList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.packageList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.packageList.setShowGrid(False)
        self.packageList.setWordWrap(True)
        self.packageList.setCornerButtonEnabled(False)
        self.packageList.setObjectName("packageList")
        self.packageList.horizontalHeader().setVisible(False)
        self.packageList.horizontalHeader().setStretchLastSection(True)
        self.packageList.verticalHeader().setVisible(False)
        self.packageList.verticalHeader().setDefaultSectionSize(52)
        self.packageList.verticalHeader().setMinimumSectionSize(52)
        self.gridLayout.addWidget(self.packageList, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 3)
        self.extrasLabel = QtWidgets.QLabel(self.widget_2)
        self.extrasLabel.setIndent(3)
        self.extrasLabel.setObjectName("extrasLabel")
        self.gridLayout.addWidget(self.extrasLabel, 2, 0, 1, 3)
        self.extraList = PackageView(self.widget_2)
        self.extraList.setMinimumSize(QtCore.QSize(400, 0))
        self.extraList.setStyleSheet("")
        self.extraList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.extraList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.extraList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.extraList.setProperty("showDropIndicator", False)
        self.extraList.setDragDropOverwriteMode(False)
        self.extraList.setAlternatingRowColors(False)
        self.extraList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.extraList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.extraList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.extraList.setShowGrid(False)
        self.extraList.setWordWrap(True)
        self.extraList.setCornerButtonEnabled(False)
        self.extraList.setObjectName("extraList")
        self.extraList.horizontalHeader().setVisible(False)
        self.extraList.horizontalHeader().setStretchLastSection(True)
        self.extraList.verticalHeader().setVisible(False)
        self.extraList.verticalHeader().setDefaultSectionSize(52)
        self.extraList.verticalHeader().setMinimumSectionSize(52)
        self.gridLayout.addWidget(self.extraList, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setIndent(3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.totalSize = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalSize.sizePolicy().hasHeightForWidth())
        self.totalSize.setSizePolicy(sizePolicy)
        self.totalSize.setObjectName("totalSize")
        self.gridLayout.addWidget(self.totalSize, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clearButton = QtWidgets.QPushButton(self.widget_2)
        self.clearButton.setStyleSheet("")
        self.clearButton.setAutoDefault(False)
        self.clearButton.setFlat(False)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.actionButton = QtWidgets.QPushButton(self.widget_2)
        self.actionButton.setStyleSheet("")
        self.actionButton.setDefault(True)
        self.actionButton.setObjectName("actionButton")
        self.horizontalLayout_2.addWidget(self.actionButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 2, 2, 1)
        self.downloadSizeLabel = QtWidgets.QLabel(self.widget_2)
        self.downloadSizeLabel.setIndent(3)
        self.downloadSizeLabel.setObjectName("downloadSizeLabel")
        self.gridLayout.addWidget(self.downloadSizeLabel, 6, 0, 1, 1)
        self.downloadSize = QtWidgets.QLabel(self.widget_2)
        self.downloadSize.setObjectName("downloadSize")
        self.gridLayout.addWidget(self.downloadSize, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 7, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.Basket, 0, 0, 1, 1)

        self.retranslateUi(BasketDialog)
        QtCore.QMetaObject.connectSlotsByName(BasketDialog)
        BasketDialog.setTabOrder(self.packageList, self.extraList)

    def retranslateUi(self, BasketDialog):
        _translate = QtCore.QCoreApplication.translate
        BasketDialog.setWindowTitle(_translate("BasketDialog", "Basket"))
        self.infoLabel.setText(_translate("BasketDialog", "Selected package(s) for install:"))
        self.extrasLabel.setText(_translate("BasketDialog", "Extra dependencies of the selected package(s) that are also going to be installed:"))
        self.label_3.setText(_translate("BasketDialog", "Total Size:"))
        self.totalSize.setText(_translate("BasketDialog", "<b>2.2 MB</b>"))
        self.clearButton.setText(_translate("BasketDialog", "Clear Basket"))
        self.actionButton.setText(_translate("BasketDialog", "Install Package(s)"))
        self.downloadSizeLabel.setText(_translate("BasketDialog", "Download Size:"))
        self.downloadSize.setText(_translate("BasketDialog", "<b>2.0 MB</"))

from packageview import PackageView
