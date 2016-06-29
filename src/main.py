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

# Python Imports
import sys
import dbus
import signal
import traceback

# PyQt5 Imports
from PyQt5.QtCore import Qt, QItemSelectionModel, QTranslator
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
from pds.quniqueapp import QUniqueApplication

# Package Manager Specific Imports
import config
import backend

from pmlogging import logger
from mainwindow import MainWindow
from localedata import setSystemLocale

from pmutils import *

# Package Manager Main App
if __name__ == '__main__':

    # Catch signals
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Create a dbus mainloop if its not exists
    if not dbus.get_default_main_loop():
        from dbus.mainloop.pyqt5 import DBusQtMainLoop
        DBusQtMainLoop(set_as_default = True)

    #Use raster to make it faster
    #QApplication nın böyle bir özelliği yok
    #QApplication.setGraphicsSystem('raster')

    pid = os.fork()
    if pid:
        os._exit(0)

    app = QUniqueApplication(sys.argv, catalog='package-manager')
    setSystemLocale()
    
    lang=setSystemLocale(True)
    print "lang=",lang
    print os.path.isfile("/usr/share/package-manager/lang/{}.qm".format(lang))
    translator=QTranslator()
    translator.load("/usr/share/package-manager/lang/{}.qm".format(lang))
    app.installTranslator(translator)
    
    # Set application font from system
    font = Pds.settings('font','Sans,10').split(',')
    app.setFont(QFont(font[0], int(font[1])))

    manager = MainWindow(app)
    app.setMainWindow(manager)

    if config.PMConfig().systemTray():
        app.setQuitOnLastWindowClosed(False)

    if not config.PMConfig().systemTray() or "--show-mainwindow" in sys.argv:
        manager.show()
        if "--select-component" in sys.argv:      #direkt oyunları vs. açmak için düzenle
            selected_component=sys.argv[sys.argv.index("--select-component") + 1]
            if selected_component == "multimedia":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(3),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            elif selected_component == "programming":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(21),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            elif selected_component == "graphics":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(11),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            elif selected_component == "network":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(1),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            elif selected_component == "office":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(19),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            elif selected_component == "games":
                manager.cw.groupList.setCurrentItem(manager.cw.groupList.item(20),QItemSelectionModel.SelectCurrent | QItemSelectionModel.Toggle)
                manager.cw.initializePackageList()
            
            # groupList
            #==========         # uygulama başlatıcı sıramalasına göre
            #  3- multimedia 
            # 21- programming 
            # 11- graphics
            #  1- network
            # 19- office
            # 20- games
            
    # Set exception handler
    sys.excepthook = handleException

    # Run the Package Manager
    app.exec_()

