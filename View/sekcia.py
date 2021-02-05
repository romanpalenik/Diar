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
        self.tabWidget.setGeometry(QRect(0, 20, 1041, 461))
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
        self.label = QLabel(self.subject5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(910, 10, 67, 16))
        self.label_2 = QLabel(self.subject5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(790, 10, 67, 16))
        self.label_3 = QLabel(self.subject5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 67, 17))
        self.label_4 = QLabel(self.subject5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 10, 111, 16))
        self.label_5 = QLabel(self.subject5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 10, 161, 16))
        self.pushButton = QPushButton(self.subject5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 360, 89, 25))
        self.comboBox = QComboBox(self.subject5)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 325, 86, 25))
        self.label_6 = QLabel(self.subject5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 330, 67, 17))
        self.line = QFrame(self.subject5)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 40, 1041, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.subject5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(580, 80, 71, 16))
        self.listWidget = QListWidget(self.subject5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(240, 190, 256, 192))
        self.pushButton_3 = QPushButton(self.subject5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(110, 360, 89, 25))
        self.textEdit = QTextEdit(self.subject5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(580, 110, 451, 271))
        self.label_8 = QLabel(self.subject5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(420, 0, 121, 16))
        self.label_9 = QLabel(self.subject5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(580, 0, 67, 17))
        self.button_prednaska_link = QPushButton(self.subject5)
        self.button_prednaska_link.setObjectName(u"button_prednaska_link")
        self.button_prednaska_link.setGeometry(QRect(420, 20, 89, 25))
        self.button_cviko_link = QPushButton(self.subject5)
        self.button_cviko_link.setObjectName(u"button_cviko_link")
        self.button_cviko_link.setGeometry(QRect(580, 20, 89, 25))
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
        self.label.setText(QCoreApplication.translate("MainWindow2", u"email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow2", u"meno", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow2", u"Kedy v rozvrhu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow2", u"Link na is s predmetom", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow2", u"Pridat ulohu", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow2", u"Sablony", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow2", u"poznamky", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow2", u"Odobrat", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow2", u"link na prednasku", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow2", u"cviko", None))
        self.button_prednaska_link.setText(QCoreApplication.translate("MainWindow2", u"prednaska", None))
        self.button_cviko_link.setText(QCoreApplication.translate("MainWindow2", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.subject5), QCoreApplication.translate("MainWindow2", u"VAVA", None))
    # retranslateUi

