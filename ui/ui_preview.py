# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/preview.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName("Preview")
        Preview.resize(802, 628)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preview.sizePolicy().hasHeightForWidth())
        Preview.setSizePolicy(sizePolicy)
        Preview.setStyleSheet("QWebView { background-color:rgba(0,0,0,0); }")
        self.gridLayout_2 = QtWidgets.QGridLayout(Preview)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(767, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(Preview)
        self.cancelButton.setMaximumSize(QtCore.QSize(32, 16777215))
        self.cancelButton.setText("")
        self.cancelButton.setAutoDefault(True)
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout_2.addWidget(self.cancelButton, 0, 1, 1, 1)
        self.webLayout = QtWidgets.QGridLayout()
        self.webLayout.setObjectName("webLayout")
        self.webView = QtWebKitWidgets.QWebView(Preview)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.webLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.webLayout, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(1, 3)

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        _translate = QtCore.QCoreApplication.translate
        Preview.setWindowTitle(_translate("Preview", "Preview"))

from PyQt5 import QtWebKitWidgets
