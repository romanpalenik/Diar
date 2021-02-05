import repackage

from ApkaNaSkolu.Model.loadFromdatabases import Databases

repackage.up(2)

from PySide2 import QtWidgets, QtGui
from ApkaNaSkolu.View.sekcia import *


class OtherWindow:

    def start(self, win):
        """this function is call fist to set attributes """
        self.win = win

    def open_link(self):
        """open url links in default browser"""
        link = "http://www.google.com"
        QDesktopServices.openUrl(QUrl(link))

    def change_to_do(self):
        pole = ['1', '2']
        self.win.listWidget_2.addItems(pole)