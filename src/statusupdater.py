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

from PyQt5.QtCore import QThread, pyqtSignal
from pmutils import humanReadableSize as humanize

class StatusUpdater(QThread):
    selectedInfoChanged = pyqtSignal([int, str, int, str],[str])
    def __init__(self):
        QThread.__init__(self)
        self.model = None
        self.needsUpdate = False
        self.calculate_deps = True

    def setModel(self, model):
        self.model = model

    def run(self):
        packages = len(self.model.selectedPackages())
        packagesSize = humanize(self.model.selectedPackagesSize())
        try:
            extraPackages = 0
            extraPackagesSize = ''
            if self.calculate_deps:
                extraPackages = len(self.model.extraPackages())
                extraPackagesSize = humanize(self.model.extraPackagesSize())
            self.selectedInfoChanged[int, str, int, str].emit(packages, packagesSize, extraPackages, extraPackagesSize)
        except Exception, e:
            self.selectedInfoChanged[str].emit(unicode(e))

