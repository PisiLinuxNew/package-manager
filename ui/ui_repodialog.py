# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/repodialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RepoDialog(object):
    def setupUi(self, RepoDialog):
        RepoDialog.setObjectName("RepoDialog")
        RepoDialog.resize(373, 168)
        RepoDialog.setMinimumSize(QtCore.QSize(373, 168))
        RepoDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(RepoDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(RepoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.repoName = QtWidgets.QLineEdit(RepoDialog)
        self.repoName.setObjectName("repoName")
        self.gridLayout.addWidget(self.repoName, 1, 0, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(RepoDialog)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(RepoDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.repoAddress = QtWidgets.QComboBox(RepoDialog)
        self.repoAddress.setEditable(True)
        self.repoAddress.setObjectName("repoAddress")
        self.repoAddress.addItem("")
        self.repoAddress.setItemText(0, "")
        self.gridLayout.addWidget(self.repoAddress, 3, 0, 1, 1)

        self.retranslateUi(RepoDialog)
        self.buttonBox.accepted.connect(RepoDialog.accept)
        self.buttonBox.rejected.connect(RepoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RepoDialog)

    def retranslateUi(self, RepoDialog):
        _translate = QtCore.QCoreApplication.translate
        RepoDialog.setWindowTitle(_translate("RepoDialog", "Add New Repository"))
        self.textLabel1.setToolTip(_translate("RepoDialog", "Name of the repository, e.g <b>pardus-devel</b>"))
        self.textLabel1.setText(_translate("RepoDialog", "Repository Name"))
        self.label.setText(_translate("RepoDialog", "Repository Address"))

