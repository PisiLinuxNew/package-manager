#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *

from pmutils import *

import config
import backend

_translate = QCoreApplication.translate

class PTray:
    def __init__(self, iface):
        self.defaultIcon = QtGui.QIcon(":/data/tray-zero.png")
        self.countIcon = QtGui.QIcon(":/data/tray-count.png")
        self.clip = QtGui.QMovie(":/data/animated-tray.mng")
        self.lastIcon = self.defaultIcon
        self.setIcon(self.defaultIcon)
        self.lastUpgrades = []
        self.unread = 0
        self.iface = iface
        self.notification = None
        self.initializeTimer()
        self.initializePopup()
        self.settingsChanged()

    def animate(self):
        self.clip.frameChanged[int].connect(self.slotAnimate)
        self.clip.setCacheMode(QtGui.QMovie.CacheAll)
        self.clip.start()

    def stop(self):
        self.clip.stop()
        self.setIcon(self.lastIcon)

    def slotAnimate(self, scene):
        self.setIcon(QtGui.QIcon(self.clip.currentPixmap()))

    def initializeTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkUpdate)
        self.interval = config.PMConfig().updateCheckInterval()
        self.updateInterval(self.interval)

    def initializePopup(self):
        pass

    def populateRepositoryMenu(self):
        pass

    def _addAction(self, title, menu, repo, icon):
        action = QtWidgets.QAction(QtGui.QIcon(icon), unicode(title), self)
        action.setData(QVariant(unicode(repo)))
        menu.addAction(action)
        action.triggered.connect(self.updateRepo)

    def updateRepo(self):
        if not self.iface.operationInProgress():
            repoName = unicode(self.sender().data())
            if repoName == "all":
                self.iface.updateRepositories()
            else:
                self.iface.updateRepository(repoName)

    def checkUpdate(self):
        if not self.appWindow.isVisible() and not self.iface.operationInProgress():
            self.iface.updateRepositories()

    def _ready_to_popup(self):
        upgrades = self.iface.getUpdates()
        self.slotSetUnread(len(upgrades))

        if config.PMConfig().installUpdatesAutomatically():
            if not self.appWindow.isVisible() and not self.iface.operationInProgress():
                self.iface.upgradePackages(upgrades)
            return False

        newUpgrades = set(upgrades) - set(self.lastUpgrades)
        self.lastUpgrades = upgrades
        if not len(upgrades) or not newUpgrades:
            return False

        return True

    def updateInterval(self, min):
        # minutes to milliseconds conversion
        interval = min * 60 * 1000
        if not interval == self.interval:
            self.interval = interval
            self.timer.stop()
            if interval:
                self.timer.start(interval)

    def settingsChanged(self):
        cfg = config.PMConfig()
        if cfg.systemTray():
            self.show()
            QTimer.singleShot(1, self.updateTrayUnread)
        else:
            self.hide()
        QtWidgets.qApp.setQuitOnLastWindowClosed(not cfg.systemTray())
        self.updateInterval(cfg.updateCheckInterval())

    def updateTrayUnread(self):
        waitCursor()
        noUpgrades = len(self.iface.getUpdates())
        self.slotSetUnread(noUpgrades)
        restoreCursor()

    # stolen from Akregator
    def slotSetUnread(self, unread):
        print config.PMConfig().hideTrayIfThereIsNoUpdate()
        if config.PMConfig().hideTrayIfThereIsNoUpdate() and unread == 0:
            self.hide()
        elif config.PMConfig().systemTray():
            self.show()

        if self.unread == unread:
            return

        self.unread = unread

        if unread == 0:
            self.setIcon(self.defaultIcon)
            self.lastIcon = self.defaultIcon
        else:
            countStr = "%s" % unread
            f = QtGui.QFont(Pds.settings('font','Sans'))
            f.setBold(True)

            pointSize = f.pointSizeF()
            fm = QtGui.QFontMetrics(f)
            w = fm.width(countStr)
            if w > (19):
                pointSize *= float(19) / float(w)
                f.setPointSizeF(pointSize)

            overlayImg = QtGui.QPixmap(self.countIcon.pixmap(22))
            p = QtGui.QPainter(overlayImg)
            p.setFont(f)
            scheme = QtGui.QBrush()

            p.setBrush(scheme)
            p.setOpacity(0.6)
            p.setPen(QtGui.QColor('white'))
            # shadow
            for i in range(20,24):
                p.drawText(QRect(0, 0, i, i), Qt.AlignCenter, countStr)
            p.setOpacity(1.0)
            p.setPen(QtGui.QColor('black'))
            p.drawText(overlayImg.rect(), Qt.AlignCenter, countStr)

            p.end()
            self.lastIcon = QtGui.QIcon(overlayImg)
            self.setIcon(self.lastIcon)

class Tray(QtWidgets.QSystemTrayIcon, PTray):
    showUpdatesSelected= pyqtSignal()
    def __init__(self, parent, iface):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        self.appWindow = parent
        PTray.__init__(self, iface)

        self.activated.connect(self.__activated)
        self.showUpdatesSelected.emit()

    def __activated(self, reason):
        if not reason == QtWidgets.QSystemTrayIcon.Context:
            if self.appWindow.isVisible():
                self.appWindow.hide()
            else:
                self.appWindow.show()

    def initializePopup(self):
        self.setIcon(self.defaultIcon)
        self.actionMenu = QtWidgets.QMenu(_translate("Packaga Manager","Update"))
        self.populateRepositoryMenu()

    def populateRepositoryMenu(self):
        self.actionMenu.clear()
        for name, address in self.iface.getRepositories(only_active = True):
            self._addAction(_translate("Packaga Manager","Update {0} repository").format(name), self.actionMenu, name, "applications-system")
        self._addAction(_translate("Packaga Manager","Update All Repositories"), self.actionMenu, "all", "update-manager")
        self.setContextMenu(self.actionMenu)
        self.contextMenu().addSeparator()
        self.contextMenu().addAction(QtGui.QIcon.fromTheme("exit"), _translate("Packaga Manager","Quit"), QtWidgets.qApp.quit)

    def showPopup(self):
        if self._ready_to_popup():
            Pds.notify(_translate("Packaga Manager",'Updates'), _translate("Packaga Manager","There are {0} updates available!").format(self.unread))

