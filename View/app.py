# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 668)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progress = QLabel(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setGeometry(QRect(10, 10, 71, 21))
        self.addSubject = QPushButton(self.centralwidget)
        self.addSubject.setObjectName(u"addSubject")
        self.addSubject.setGeometry(QRect(10, 400, 131, 21))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(750, 390, 256, 192))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(350, 390, 256, 192))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, 0, 20, 651))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(770, 410, 113, 25))
        self.subject1 = QLabel(self.centralwidget)
        self.subject1.setObjectName(u"subject1")
        self.subject1.setGeometry(QRect(10, 70, 67, 17))
        self.subject2 = QLabel(self.centralwidget)
        self.subject2.setObjectName(u"subject2")
        self.subject2.setEnabled(True)
        self.subject2.setGeometry(QRect(10, 130, 67, 17))
        self.subject3 = QLabel(self.centralwidget)
        self.subject3.setObjectName(u"subject3")
        self.subject3.setGeometry(QRect(10, 190, 67, 17))
        self.subject4 = QLabel(self.centralwidget)
        self.subject4.setObjectName(u"subject4")
        self.subject4.setGeometry(QRect(10, 250, 81, 16))
        self.subject5 = QLabel(self.centralwidget)
        self.subject5.setObjectName(u"subject5")
        self.subject5.setGeometry(QRect(10, 310, 67, 17))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(510, 590, 89, 25))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(10, 90, 118, 23))
        self.progressBar.setValue(24)
        self.progressBar_2 = QProgressBar(self.centralwidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(10, 150, 118, 23))
        self.progressBar_2.setValue(24)
        self.progressBar_3 = QProgressBar(self.centralwidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(10, 210, 118, 23))
        self.progressBar_3.setValue(24)
        self.progressBar_4 = QProgressBar(self.centralwidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(10, 270, 118, 23))
        self.progressBar_4.setValue(24)
        self.progressBar_5 = QProgressBar(self.centralwidget)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setGeometry(QRect(10, 330, 118, 23))
        self.progressBar_5.setValue(24)
        self.cal = QCalendarWidget(self.centralwidget)
        self.cal.setObjectName(u"cal")
        self.cal.setGeometry(QRect(280, 20, 581, 221))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 270, 131, 16))
        self.nearestEvent = QLabel(self.centralwidget)
        self.nearestEvent.setObjectName(u"nearestEvent")
        self.nearestEvent.setGeometry(QRect(430, 270, 421, 16))
        self.text_event = QTextEdit(self.centralwidget)
        self.text_event.setObjectName(u"text_event")
        self.text_event.setGeometry(QRect(870, 40, 181, 201))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1055, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.progress.setText(QCoreApplication.translate("MainWindow", u"Predmety", None))
        self.addSubject.setText(QCoreApplication.translate("MainWindow", u"Sekcia predmetov", None))
        self.subject1.setText(QCoreApplication.translate("MainWindow", u"AZA", None))
        self.subject2.setText(QCoreApplication.translate("MainWindow", u"Databazy", None))
        self.subject3.setText(QCoreApplication.translate("MainWindow", u"PSI", None))
        self.subject4.setText(QCoreApplication.translate("MainWindow", u"Bezpe\u010dnost", None))
        self.subject5.setText(QCoreApplication.translate("MainWindow", u"VAVA", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Najbli\u017e\u0161ie n\u00e1s \u010dak\u00e1: ", None))
        self.nearestEvent.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

