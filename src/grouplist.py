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

import backend

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import *
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QListWidgetItem
from pds import qiconloader

from pmutils import *
from statemanager import StateManager

_translate = QCoreApplication.translate

class GroupList(QListWidget):
    groupChanged = pyqtSignal()
    def __init__(self, parent=None):
        super(GroupList, self).__init__(parent)
        #QListWidget.__init__(self, parent)
        self.iface = backend.pm.Iface()
        #self.defaultIcon = KIcon(('applications-other', 'unknown'), KIconLoader.SizeSmallMedium)
        self.defaultIcon= QIcon('/usr/share/package-manager/data/application-x-pisi.svg')
        self.itemClicked[QListWidgetItem].connect(self.slotGroupChanged)
        self.itemSelectionChanged.connect(self.slotGroupChanged)
        self._list = {}

    def setState(self, state):
        self.state = state

    def addGroups(self, groups):
        if groups:
            for name in groups:
                self.createGroupItem(name)
        else:
            self.createGroupItem('all',
                    (_translate("Package Manager",'All'), 'media-optical', len(self.state.packages())))
        self.sortItems()
        self.moveAllToFirstLine()
        self.setCurrentItem(self.item(0))

    def createGroupItem(self, name, content = None):
        if not content:
            group = self.iface.getGroup(name)
            localName, icon_path = unicode(group.localName), group.icon
            package_count = len(self.state.groupPackages(name))
            if package_count <= 0:
                return
        else:
            localName, icon_path = content[0], content[1]
            package_count = content[2]

        #icon = QIcon.fromTheme(icon_path)
        icon = QIcon("/usr/share/pixmaps/icons/%s" % icon_path)
        if icon.isNull():
            icon = self.defaultIcon
        text = "%s (%d)" % (localName, package_count)
        item = QListWidgetItem(icon, text, self)
        item.setToolTip(localName)
        item.setData(Qt.UserRole, QVariant(unicode(name)))
        item.setSizeHint(QSize(0, QIconLoader.SizeMedium))
        self._list[name] = item

    def moveAllToFirstLine(self):
        if not self.count():
            return

        for i in range(self.count()):
            key = self.item(i).data(Qt.UserRole)
            if key == "all":
                item = self.takeItem(i)
                self.insertItem(0, item)

    def currentGroup(self):
        if not self.count():
            return
        if self.currentItem():
            return unicode(self.currentItem().data(Qt.UserRole))

    def slotGroupChanged(self):
        self.groupChanged.emit()

