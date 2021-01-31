# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sekcia_predmetov.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        if not MainWindow2.objectName():
            MainWindow2.setObjectName(u"MainWindow2")
        MainWindow2.resize(1054, 600)
        self.centralwidget = QWidget(MainWindow2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1041, 461))
        self.subject1 = QWidget()
        self.subject1.setObjectName(u"subject1")
        self.tabWidget.addTab(self.subject1, "")
        self.subject2 = QWidget()
        self.subject2.setObjectName(u"subject2")
        self.tabWidget.addTab(self.subject2, "")
        self.subject3 = QWidget()
        self.subject3.setObjectName(u"subject3")
        self.tabWidget.addTab(self.subject3, "")
        self.subject4 = QWidget()
        self.subject4.setObjectName(u"subject4")
        self.tabWidget.addTab(self.subject4, "")
        self.subject5 = QWidget()
        self.subject5.setObjectName(u"subject5")
        self.tabWidget.addTab(self.subject5, "")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1054, 22))
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow2)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow2)
    # setupUi

    def retranslateUi(self, MainWindow2):
        MainWindow2.setWindowTitle(QCoreApplication.translate("MainWindow2", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject1), QCoreApplication.translate("MainWindow2", u"AZA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject2), QCoreApplication.translate("MainWindow2", u"Databazy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject3), QCoreApplication.translate("MainWindow2", u"PSI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject4), QCoreApplication.translate("MainWindow2", u"Bezpecnost", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject5), QCoreApplication.translate("MainWindow2", u"VAVA", None))
    # retranslateUi

