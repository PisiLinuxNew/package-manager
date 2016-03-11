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
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QActionGroup
from PyQt5.QtGui import QKeySequence

from PyQt5.QtCore import *

from ui_mainwindow import Ui_MainWindow

from mainwidget import MainWidget
from pdswidgets import PMessageBox
from statemanager import StateManager
from settingsdialog import SettingsDialog

from pds.qprogressindicator import QProgressIndicator
from tray import Tray
from pmutils import *

import backend
import config
import helpdialog
import localedata
import os
import pds

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app = None):
        #QMainWindow.__init__(self, None)
        super(MainWindow, self).__init__(None)
        self.setupUi(self)

        self.app = app
        self.iface = backend.pm.Iface()

        self.busy = QProgressIndicator(self)
        self.busy.setFixedSize(QSize(20, 20))

        self.setWindowIcon(QIcon(":/data/package-manager.png"))

        self.setCentralWidget(MainWidget(self))
        self.cw = self.centralWidget()

        self.settingsDialog = SettingsDialog(self)

        self.initializeActions()
        self.initializeStatusBar()
        self.initializeTray()
        self.connectMainSignals()

        self.pdsMessageBox = PMessageBox(self)

    def connectMainSignals(self):
        self.cw.connectMainSignals()
        
        move_shortcut=QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Tab),self)
        move_shortcut.activated.connect(lambda: self.moveTab('next'))
        QShortcut(QKeySequence(Qt.SHIFT + Qt.CTRL + Qt.Key_Tab),self).activated.connect(lambda: self.moveTab('prev'))
        QShortcut(QKeySequence(Qt.CTRL + Qt.Key_F),self).activated.connect(self.cw.searchLine.setFocus)
        QShortcut(QKeySequence(Qt.Key_F3),self).activated.connect(self.cw.searchLine.setFocus)

        self.settingsDialog.generalSettings.packagesChanged.connect(self.cw.initialize)
        self.settingsDialog.generalSettings.packageViewChanged.connect(self.cw.updateSettings)
        self.settingsDialog.generalSettings.traySettingChanged.connect(self.tray.settingsChanged)
        self.cw.state.repositoriesChanged.connect(self.tray.populateRepositoryMenu)
        self.cw.repositoriesUpdated.connect(self.tray.updateTrayUnread)
        

    def moveTab(self, direction):
        new_index = self.cw.stateTab.currentIndex() - 1
        if direction == 'next':
            new_index = self.cw.stateTab.currentIndex() + 1
        if new_index not in range(self.cw.stateTab.count()):
            new_index = 0
        self.cw.stateTab.setCurrentIndex(new_index)

    def initializeTray(self):
        self.tray = Tray(self, self.iface)
        self.cw.operation.finished[str].connect(self.trayAction)
        self.cw.operation.finished[str].connect(self.tray.stop)
        self.cw.operation.operationCancelled.connect(self.tray.stop)
        self.cw.operation.started[str].connect(self.tray.animate)
        self.tray.showUpdatesSelected.connect(self.trayShowUpdates)         # buraya dikkat

    def trayShowUpdates(self):
        self.showUpgradeAction.setChecked(True)

        self.cw.switchState(StateManager.UPGRADE)

        KApplication.kApplication().updateUserTimestamp()

        self.show()
        self.raise_()

    def trayAction(self, operation):
        if not self.isVisible() and operation in ["System.Manager.updateRepository", "System.Manager.updateAllRepositories"]:
            self.tray.showPopup()
        if self.tray.isVisible() and operation in ["System.Manager.updatePackage",
                                                   "System.Manager.installPackage",
                                                   "System.Manager.removePackage"]:
            self.tray.updateTrayUnread()

    def initializeStatusBar(self):
        self.cw.mainLayout.insertWidget(0, self.busy)
        self.statusBar().addPermanentWidget(self.cw.actions, 1)
        self.statusBar().show()

        self.updateStatusBar('')

        self.cw.selectionStatusChanged[str].connect(self.updateStatusBar)
        self.cw.updatingStatus.connect(self.statusWaiting)

    def initializeActions(self):
        self.initializeOperationActions()

    def initializeOperationActions(self):

        self.showAllAction = QAction(KIcon(("applications-other", "package_applications")), i18n("All Packages"), self)
        self.showAllAction.triggered.connect(lambda:self.cw.switchState(StateManager.ALL))
        self.cw.stateTab.addTab(QWidget(), KIcon(("applications-other", "package_applications")), i18n("All Packages"))

        self.showInstallAction = QAction(KIcon(("list-add", "add")), i18n("Installable Packages"), self)
        self.showInstallAction.triggered.connect(lambda:self.cw.switchState(StateManager.INSTALL))
        self.cw.stateTab.addTab(QWidget(), KIcon(("list-add", "add")), i18n("Installable Packages"))

        self.showRemoveAction = QAction(KIcon(("list-remove", "remove")), i18n("Installed Packages"), self)
        self.showRemoveAction.triggered.connect(lambda:self.cw.switchState(StateManager.REMOVE))
        self.cw.stateTab.addTab(QWidget(), KIcon(("list-remove", "remove")), i18n("Installed Packages"))

        self.showUpgradeAction = QAction(KIcon(("system-software-update", "gear")), i18n("Updates"), self)
        self.showUpgradeAction.triggered.connect(lambda:self.cw.switchState(StateManager.UPGRADE))
        self.cw.stateTab.addTab(QWidget(), KIcon(("system-software-update", "gear")), i18n("Updates"))

        self.showPreferences = QAction(KIcon(("preferences-system", "package_settings")), i18n("Settings"), self)
        self.showPreferences.triggered.connect(self.settingsDialog.exec_)

        self.actionHelp = QAction(KIcon("help"), i18n("Help"), self)
        self.actionHelp.setShortcuts(QKeySequence.HelpContents)
        self.actionHelp.triggered.connect(self.showHelp)

        self.actionQuit = QAction(KIcon("exit"), i18n("Quit"), self)
        self.actionQuit.setShortcuts(QKeySequence.Quit)
        self.actionQuit.triggered.connect(qApp.exit)

        self.cw.menuButton.setMenu(QMenu('MainMenu', self.cw.menuButton))
        self.cw.menuButton.setIcon(KIcon(("preferences-system", "package_settings")))
        self.cw.menuButton.menu().clear()

        self.cw.contentHistory.hide()

        self.cw.menuButton.menu().addAction(self.showPreferences)
        self.cw.menuButton.menu().addSeparator()
        self.cw.menuButton.menu().addAction(self.actionHelp)
        self.cw.menuButton.menu().addAction(self.actionQuit)

        self.cw._states = {self.cw.state.ALL    :(0, self.showAllAction),
                           self.cw.state.INSTALL:(1, self.showInstallAction),
                           self.cw.state.REMOVE :(2, self.showRemoveAction),
                           self.cw.state.UPGRADE:(3, self.showUpgradeAction)}

        self.showAllAction.setChecked(True)
        self.cw.checkUpdatesButton.hide()
        self.cw.checkUpdatesButton.setIcon(KIcon(("view-refresh", "reload")))
        self.cw.showBasketButton.clicked.connect(self.cw.showBasket)

        # Little time left for the new ui
        self.menuBar().setVisible(False)
        self.cw.switchState(self.cw.state.ALL)

    def statusWaiting(self):
        self.updateStatusBar(i18n('Calculating dependencies...'), busy = True)

    def showHelp(self):
        self.Pds = pds.Pds()
        self.lang = localedata.setSystemLocale(justGet = True)
        
        if self.lang in os.listdir("/usr/share/package-manager/help"):
            pass
        else:
            self.lang = "en"

        
        if self.Pds.session == pds.Kde3 :
            os.popen("khelpcenter /usr/share/package-manager/help/%s/main_help.html" %(self.lang))
        else:
            helpdialog.HelpDialog(self,helpdialog.MAINAPP)


    def updateStatusBar(self, text, busy = False):
        if text == '':
            text = i18n("Currently your basket is empty.")
            self.busy.hide()
            self.cw.showBasketButton.hide()
        else:
            self.cw.showBasketButton.show()

        if busy:
            self.busy.busy()
            self.cw.showBasketButton.hide()
        else:
            self.busy.hide()

        self.cw.statusLabel.setText(text)
        self.cw.statusLabel.setToolTip(text)

    def queryClose(self):
        if config.PMConfig().systemTray():
            self.hide()
            return False
        return True

    def queryExit(self):
        if not self.iface.operationInProgress():
            if self.tray:
                del self.tray.notification
            return True
        return False

    def CloseEvent(self,event):
        if self.iface.operationInProgress():
            return
