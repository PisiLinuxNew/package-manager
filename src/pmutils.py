#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import sys
import pisi
import comar
import urllib
import socket
import unicodedata
import traceback

import backend

from pmlogging import logger

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QEventLoop,QCoreApplication

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication

from PyQt5.QtNetwork import QNetworkProxy

import pds
from pds.qiconloader import QIconLoader


Pds = pds.Pds('package-manager', debug = False)
#Force to use Default Session for testing
#Pds.session = pds.DefaultDe
#print 'Current session is : %s %s' % (Pds.session.Name, Pds.session.Version)

i18n = Pds.session.i18n
KIconLoader = QIconLoader(Pds)
KIcon = KIconLoader.icon

_translate = QCoreApplication.translate

class PM:
    def __init__(self, **kwds):
        #super(PM, self).__init__(**kwds)
        pass
        
    
    def connectOperationSignals(self):
        # Basic connections
        self.operation.exception[str].connect(self.exceptionCaught)
        self.operation.finished[str].connect(self.actionFinished)
        self.operation.started[str].connect(self.actionStarted)
        self.operation.operationCancelled.connect(self.actionCancelled)

        # ProgressDialog connections
        self.operation.started[str].connect(self.progressDialog.updateActionLabel)
        self.operation.progress[int].connect(self.progressDialog.updateProgress)
        self.operation.operationChanged[str,str].connect(self.progressDialog.updateOperation)
        self.operation.packageChanged[int,int,str].connect(self.progressDialog.updateStatus)
        self.operation.elapsedTime[str].connect(self.progressDialog.updateRemainingTime)
        self.operation.downloadInfoChanged[str,str,str].connect(self.progressDialog.updateCompletedInfo)

    def notifyFinished(self):
        if not self.operation.totalPackages:
            return
        Pds.notify(_translate("Package Manager",'Package Manager'), self.state.getSummaryInfo(self.operation.totalPackages))

    def exceptionCaught(self, message, package = '', block = False):
        self.runPreExceptionMethods()

        if any(warning in message for warning in ('urlopen error','Socket Error', 'PYCURL ERROR')):
            errorTitle = _translate("Package Manager","Network Error")
            errorMessage = _translate("Package Manager","Please check your network connections and try again.")
        elif "Access denied" in message or "tr.org.pardus.comar.Comar.PolicyKit" in message:
            errorTitle = _translate("Package Manager","Authorization Error")
            errorMessage = _translate("Package Manager","You are not authorized for this operation.")
        elif "HTTP Error 404" in message and not package == '':
            errorTitle = _translate("Package Manager","Pisi Error")
            errorMessage = unicode(_translate("Package Manager","Package <b>{0}</b> not found in repositories.<br>"\
                                        "It may be upgraded or removed from the repository.<br>"\
                                        "Please try upgrading repository informations.").format(package)) 
        elif "MIXING PACKAGES" in message:
            errorTitle = _translate("Package Manager","Pisi Error")
            errorMessage = _translate("Package Manager","Mixing file names and package names not supported yet.")
        elif "FILE NOT EXISTS" in message:
            errorTitle = _translate("Package Manager","Pisi Error")
            errorMessage = unicode(_translate("Package Manager","File <b>{0}</b> doesn't exists.").format(package)) 
        elif "ALREADY RUNNING" in message:
            errorTitle = _translate("Package Manager","Pisi Error")
            errorMessage = _translate("Package Manager","Another instance of PiSi is running. Only one instance is allowed.")
        else:
            errorTitle = _translate("Package Manager","Pisi Error")
            errorMessage = message

        self.messageBox = QMessageBox(QMessageBox.Critical,errorTitle, errorMessage, QMessageBox.Ok)

        if block:
            self.messageBox.exec_()
            self.runPostExceptionMethods()
        else:
            QTimer.singleShot(0, self.messageBox.exec_)
            self.messageBox.buttonClicked.connect(self.runPostExceptionMethods)

    def runPreExceptionMethods(self):
        if hasattr(self, '_preexceptions'):
            for method in self._preexceptions:
                method()

    def runPostExceptionMethods(self, *args):
        if hasattr(self, '_postexceptions'):
            for method in self._postexceptions:
                method()

def get_real_paths(packages):
    # If packages are not from repo or remote, find their absolute paths
    return map(lambda x: x if not x.endswith('.pisi') or '://' in x else os.path.abspath(x), packages)

def isAllLocal(packages):
    return all(map(lambda x: x.endswith('.pisi') and not '://' in x, packages))

def askForActions(packages, reason, title, details_title):
    msgbox = QMessageBox()
    msgbox.setText('<b>%s</b>' % reason)
    msgbox.setInformativeText(_translate("Package Manager","Do you want to continue ?"))
    msgbox.setDetailedText(details_title + '\n' + '-'*60 + '\n  - ' + '\n  - '.join(packages))
    msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    return msgbox.exec_() == QMessageBox.Yes

def waitCursor():
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

def restoreCursor():
    # According to the Qt Documentation it should be called twice to reset
    # cursor to the default if one use waitCursor twice.
    QApplication.restoreOverrideCursor()
    QApplication.restoreOverrideCursor()

def processEvents():
    QApplication.processEvents()

def set_proxy_settings():
    http = backend.pm.Iface().getConfig().get("general", "http_proxy")
    if http and not http == "None":
        items = parse_proxy(http)
        QNetworkProxy.setApplicationProxy(
                QNetworkProxy(QNetworkProxy.HttpProxy,
                            items['host'], int(items['port']),
                            items['user'] or '', items['pass'] or ''))

def reset_proxy_settings():
    QNetworkProxy.setApplicationProxy(QNetworkProxy())

def network_available():
    #return pisi.fetcher.Fetcher('http://appinfo.pisilinux.org').test()
    return pisi.fetcher.Fetcher('https://pisilinux.org').test()

def parse_proxy(line):
    settings = {'domain':None,'user':None,'pass':None,'host':None,'port':None}

    if '://' in line:
        line = line.replace('%s://' % line.split('://')[0], '', 1)

    if '\\' in line:
        settings['domain'] = line.split('\\')[0]
        line = line.replace('%s\\' % settings['domain'], '', 1)

    if '@' in line:
        auth = line.split('@')[0]
        settings['user'], settings['pass'] = auth.split(':')
        line = line.replace('%s@' % auth, '', 1)

    if ':' in line:
        settings['host'], settings['port'] = line.split(':')

    return settings

def repos_available(iface, check_repos = None):
    repos = iface.getRepositories(only_active = True, repos = check_repos)
    if not repos:
        return False

    for name, address in repos:
        if not pisi.fetcher.Fetcher('%s.sha1sum' % address).test():
            return False

    return True

def isPisiRunning():
    link = comar.Link()
    return any(operation.startswith('System.Manager') for operation in link.listRunning())

def handleException(exception, value, tb):
    """
    Exception Handler

    @param exception: exception object
    @param value: exception message
    @param tb: traceback log
    """
    logger.error("".join(traceback.format_exception(exception, value, tb)))

def humanReadableSize(size, precision=".1"):
    if not size:
        return 'N/A'

    symbols, depth = [' B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'], 0

    while size > 1000 and depth < 8:
        size = float(size / 1024)
        depth += 1

    if size == 0:
        return "0 B"

    fmt = "%%%sf %%s" % precision
    return fmt % (size, symbols[depth])

# Python regex sucks
# http://mail.python.org/pipermail/python-list/2009-January/523704.html
def letters():
    start = end = None
    result = []
    for index in xrange(sys.maxunicode + 1):
        c = unichr(index)
        if unicodedata.category(c)[0] == 'L':
            if start is None:
                start = end = c
            else:
                end = c
        elif start:
            if start == end:
                result.append(start)
            else:
                result.append(start + "-" + end)
            start = None
    return ''.join(result)
