# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/webdialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebDialog(object):
    def setupUi(self, WebDialog):
        WebDialog.setObjectName("WebDialog")
        WebDialog.resize(700, 460)
        WebDialog.setStyleSheet("#Basket {\n"
"background-color: rgb(164, 164, 164);\n"
"border:1px solid #AAA;\n"
"border-radius:4px;\n"
"\n"
"}")
        self.gridLayout_3 = QtWidgets.QGridLayout(WebDialog)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Basket = QtWidgets.QWidget(WebDialog)
        self.Basket.setStyleSheet("QLabel { color:rgb(20,20,20); }")
        self.Basket.setObjectName("Basket")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Basket)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.Basket)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.packageFiles = QtWidgets.QWidget()
        self.packageFiles.setAutoFillBackground(False)
        self.packageFiles.setObjectName("packageFiles")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.packageFiles)
        self.gridLayout_5.setContentsMargins(8, 8, 8, 8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.filesList = QtWidgets.QListWidget(self.packageFiles)
        self.filesList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filesList.setObjectName("filesList")
        self.gridLayout_5.addWidget(self.filesList, 0, 0, 1, 2)
        self.tabWidget.addTab(self.packageFiles, "")
        self.packageDetails = QtWidgets.QWidget()
        self.packageDetails.setAutoFillBackground(False)
        self.packageDetails.setStyleSheet("QWidget#webWidget {\n"
"    border:0px solid #555;\n"
"    border-radius:6px;\n"
"\n"
"    background-color:rgba(122,122,122);\n"
"    color:rgba(20,20,20);\n"
"\n"
"}")
        self.packageDetails.setObjectName("packageDetails")
        self.webLayout = QtWidgets.QGridLayout(self.packageDetails)
        self.webLayout.setContentsMargins(4, 0, 4, 4)
        self.webLayout.setObjectName("webLayout")
        self.noconnection = QtWidgets.QLabel(self.packageDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noconnection.setFont(font)
        self.noconnection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.noconnection.setStyleSheet("")
        self.noconnection.setAlignment(QtCore.Qt.AlignCenter)
        self.noconnection.setObjectName("noconnection")
        self.webLayout.addWidget(self.noconnection, 0, 0, 1, 1)
        self.webWidget = QtWidgets.QWidget(self.packageDetails)
        self.webWidget.setStyleSheet("")
        self.webWidget.setObjectName("webWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.webWidget)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.webView = QtWebKitWidgets.QWebView(self.webWidget)
        self.webView.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)
        self.webLayout.addWidget(self.webWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.packageDetails, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 26))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"\n"
"border-bottom:1px solid #CCC;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.packageName = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.packageName.setFont(font)
        self.packageName.setIndent(3)
        self.packageName.setObjectName("packageName")
        self.horizontalLayout.addWidget(self.packageName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMinimumSize(QtCore.QSize(36, 26))
        self.cancelButton.setMaximumSize(QtCore.QSize(36, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("color:rgb(20,20,20);\n"
"")
        self.cancelButton.setText("X")
        self.cancelButton.setFlat(True)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Basket, 0, 0, 1, 1)

        self.retranslateUi(WebDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WebDialog)

    def retranslateUi(self, WebDialog):
        _translate = QtCore.QCoreApplication.translate
        WebDialog.setWindowTitle(_translate("WebDialog", "Basket"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packageFiles), _translate("WebDialog", "Package Files"))
        self.noconnection.setText(_translate("WebDialog", "AppInfo Server is not reachable\n"
"Please check your network connection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packageDetails), _translate("WebDialog", "Package Details"))
        self.packageName.setText(_translate("WebDialog", "Package Details"))

from PyQt5 import QtWebKitWidgets
