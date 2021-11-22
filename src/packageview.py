#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2010, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *

from pmutils import *
_translate = QCoreApplication.translate

class PackageView(QtWidgets.QTableView):
    updateRequested = pyqtSignal()
    dataChanged = pyqtSignal([QModelIndex,QModelIndex])
    
    def __init__(self, parent=None):
        super(PackageView, self).__init__(parent)
        #QtWidgets.QTableView.__init__(self, parent)

        self.select_all = QtWidgets.QCheckBox(_translate("Package Manager",'Select all packages in this group'), self)
        self.select_all.resize(parent.width(), 32)
        self.select_all.move(3,3)
        self.select_all.setStyleSheet('padding:8px;padding-left:4px;font-weight: bolder;border-bottom:1px solid #ccc')
        self.select_all.setAutoFillBackground(True)

        self.needs_select_all = True
        self.showComponents = False
        self.showIsA = False
        self.parent = parent
        
        
        
    def slotDataChanged(self,modelindex1,modelindex2):
        self.dataChanged[QModelIndex, QModelIndex].emit(modelindex1,modelindex2)

    def hideSelectAll(self):
        self.needs_select_all = False
        self.select_all.hide()
        self.setViewportMargins(0, 0, 0, 0)

    def resizeEvent(self, event):
        if event.isAccepted():
            QtWidgets.QTableView.resizeEvent(self, event)
            if self.needs_select_all:
                self.setViewportMargins(0, 32, 0, 0)
                self.select_all.resize(self.viewport().width(), 32)

    def isIndexHidden(self, index):
        return False

    def setPackages(self, packages):
        self.model().sourceModel().setPackages(packages)
        
    def selectedPackages(self):
        return self.model().sourceModel().selectedPackages()

    def extraPackages(self):
        return self.model().sourceModel().extraPackages()

    def selectedPackagesSize(self):
        return self.model().sourceModel().selectedPackagesSize()

    def extraPackagesSize(self):
        return self.model().sourceModel().extraPackagesSize()

    def packageCount(self):
        return len(self.selectedPackages()) + len(self.extraPackages())

    def isSelected(self):
        return bool(self.selectedPackages())

    def reverseSelection(self, packages):
        waitCursor()
        self.model().sourceModel().reverseSelection(packages)
        restoreCursor()

    def selectAll(self, packages):
        waitCursor()
        self.model().sourceModel().selectPackages(packages)
        restoreCursor()

    def resetMoreInfoRow(self):
        self.itemDelegate().reset()

    def search(self, text):
        return self.model().sourceModel().search(text)

    def requestUpdate(self):
        self.updateRequested.emit()

