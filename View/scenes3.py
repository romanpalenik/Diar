# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1066, 681)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1045, 668))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(870, 190, 71, 31))
        self.label_5.setStyleSheet(u"")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(870, 60, 67, 17))
        self.newItemToDo = QTextEdit(self.page)
        self.newItemToDo.setObjectName(u"newItemToDo")
        self.newItemToDo.setGeometry(QRect(290, 500, 161, 31))
        self.saveEvent = QPushButton(self.page)
        self.saveEvent.setObjectName(u"saveEvent")
        self.saveEvent.setGeometry(QRect(870, 160, 89, 25))
        self.subject5 = QLabel(self.page)
        self.subject5.setObjectName(u"subject5")
        self.subject5.setGeometry(QRect(10, 290, 67, 17))
        self.subject3 = QLabel(self.page)
        self.subject3.setObjectName(u"subject3")
        self.subject3.setGeometry(QRect(10, 170, 67, 17))
        self.subject4 = QLabel(self.page)
        self.subject4.setObjectName(u"subject4")
        self.subject4.setGeometry(QRect(10, 230, 81, 16))
        self.addSubject = QPushButton(self.page)
        self.addSubject.setObjectName(u"addSubject")
        self.addSubject.setGeometry(QRect(10, 380, 131, 21))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 250, 131, 16))
        self.cal = QCalendarWidget(self.page)
        self.cal.setObjectName(u"cal")
        self.cal.setGeometry(QRect(280, 0, 581, 221))
        self.text_event = QTextEdit(self.page)
        self.text_event.setObjectName(u"text_event")
        self.text_event.setGeometry(QRect(870, 20, 171, 31))
        self.subject2 = QLabel(self.page)
        self.subject2.setObjectName(u"subject2")
        self.subject2.setEnabled(True)
        self.subject2.setGeometry(QRect(10, 110, 67, 17))
        self.text_event_2 = QTextEdit(self.page)
        self.text_event_2.setObjectName(u"text_event_2")
        self.text_event_2.setGeometry(QRect(870, 80, 171, 31))
        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(870, 120, 181, 31))
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 0, 67, 17))
        self.progress = QLabel(self.page)
        self.progress.setObjectName(u"progress")
        self.progress.setGeometry(QRect(20, 0, 71, 21))
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 540, 81, 31))
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 500, 81, 31))
        self.subject1 = QLabel(self.page)
        self.subject1.setObjectName(u"subject1")
        self.subject1.setGeometry(QRect(10, 50, 67, 17))
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 540, 161, 31))
        self.line = QFrame(self.page)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(260, -20, 20, 651))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.nearestEvent_label = QLabel(self.page)
        self.nearestEvent_label.setObjectName(u"nearestEvent_label")
        self.nearestEvent_label.setGeometry(QRect(430, 250, 421, 16))
        self.listWidget = QListWidget(self.page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(290, 290, 256, 192))
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(950, 200, 67, 17))
        self.deleteEvent = QPushButton(self.page)
        self.deleteEvent.setObjectName(u"deleteEvent")
        self.deleteEvent.setGeometry(QRect(960, 160, 89, 25))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.button_mainPage = QPushButton(self.page_2)
        self.button_mainPage.setObjectName(u"button_mainPage")
        self.button_mainPage.setGeometry(QRect(20, 470, 111, 21))
        self.button_prednaska_link = QPushButton(self.page_2)
        self.button_prednaska_link.setObjectName(u"button_prednaska_link")
        self.button_prednaska_link.setGeometry(QRect(420, 60, 89, 25))
        self.email_prednaska = QLabel(self.page_2)
        self.email_prednaska.setObjectName(u"email_prednaska")
        self.email_prednaska.setGeometry(QRect(880, 40, 161, 16))
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(420, 40, 121, 16))
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(580, 120, 71, 16))
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 400, 89, 25))
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(580, 150, 451, 271))
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(580, 40, 111, 16))
        self.listWidget_2 = QListWidget(self.page_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(240, 230, 321, 191))
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 70, 67, 17))
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 400, 89, 25))
        self.line_2 = QFrame(self.page_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 80, 1041, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 330, 67, 17))
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 40, 171, 16))
        self.name_prednaska = QLabel(self.page_2)
        self.name_prednaska.setObjectName(u"name_prednaska")
        self.name_prednaska.setGeometry(QRect(740, 40, 151, 16))
        self.button_cviko_link = QPushButton(self.page_2)
        self.button_cviko_link.setObjectName(u"button_cviko_link")
        self.button_cviko_link.setGeometry(QRect(580, 60, 89, 25))
        self.comboBox_2 = QComboBox(self.page_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(110, 330, 86, 25))
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(190, 50, 161, 16))
        self.line_3 = QFrame(self.page_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 30, 1041, 16))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 10, 89, 25))
        self.pushButton_7 = QPushButton(self.page_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(110, 10, 89, 25))
        self.pushButton_8 = QPushButton(self.page_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(210, 10, 89, 25))
        self.pushButton_9 = QPushButton(self.page_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(310, 10, 89, 25))
        self.pushButton_10 = QPushButton(self.page_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(410, 10, 89, 25))
        self.open_file = QPushButton(self.page_2)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setGeometry(QRect(918, 100, 101, 31))
        self.label_backround = QLabel(self.page_2)
        self.label_backround.setObjectName(u"label_backround")
        self.label_backround.setGeometry(QRect(10, -10, 1039, 651))
        self.label_backround.setAutoFillBackground(False)
        self.button_dokumentovyserver = QPushButton(self.page_2)
        self.button_dokumentovyserver.setObjectName(u"button_dokumentovyserver")
        self.button_dokumentovyserver.setGeometry(QRect(340, 470, 151, 31))
        self.name_cviko = QLabel(self.page_2)
        self.name_cviko.setObjectName(u"name_cviko")
        self.name_cviko.setGeometry(QRect(740, 60, 67, 17))
        self.email_cviko = QLabel(self.page_2)
        self.email_cviko.setObjectName(u"email_cviko")
        self.email_cviko.setGeometry(QRect(880, 60, 161, 16))
        self.it_was_copied = QLabel(self.page_2)
        self.it_was_copied.setObjectName(u"it_was_copied")
        self.it_was_copied.setGeometry(QRect(880, 10, 91, 21))
        self.newItemToDo_2 = QTextEdit(self.page_2)
        self.newItemToDo_2.setObjectName(u"newItemToDo_2")
        self.newItemToDo_2.setGeometry(QRect(10, 360, 161, 31))
        self.cviko = QLabel(self.page_2)
        self.cviko.setObjectName(u"cviko")
        self.cviko.setGeometry(QRect(10, 60, 171, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.label_backround.raise_()
        self.button_mainPage.raise_()
        self.button_prednaska_link.raise_()
        self.email_prednaska.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.pushButton_4.raise_()
        self.textEdit.raise_()
        self.label_15.raise_()
        self.listWidget_2.raise_()
        self.label_9.raise_()
        self.pushButton_3.raise_()
        self.line_2.raise_()
        self.label_12.raise_()
        self.label_10.raise_()
        self.name_prednaska.raise_()
        self.button_cviko_link.raise_()
        self.comboBox_2.raise_()
        self.label_11.raise_()
        self.line_3.raise_()
        self.pushButton_5.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.open_file.raise_()
        self.button_dokumentovyserver.raise_()
        self.name_cviko.raise_()
        self.email_cviko.raise_()
        self.it_was_copied.raise_()
        self.newItemToDo_2.raise_()
        self.cviko.raise_()

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"15", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u010cas", None))
        self.saveEvent.setText(QCoreApplication.translate("Form", u"Ulozit", None))
        self.subject5.setText(QCoreApplication.translate("Form", u"VAVA", None))
        self.subject3.setText(QCoreApplication.translate("Form", u"PSI", None))
        self.subject4.setText(QCoreApplication.translate("Form", u"Bezpe\u010dnost", None))
        self.addSubject.setText(QCoreApplication.translate("Form", u"Sekcia predmetov", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Najbli\u017e\u0161ie n\u00e1s \u010dak\u00e1: ", None))
        self.subject2.setText(QCoreApplication.translate("Form", u"Databazy", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Akcia", None))
        self.progress.setText(QCoreApplication.translate("Form", u"Predmety", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Odstanit", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Prida\u0165 ", None))
        self.subject1.setText(QCoreApplication.translate("Form", u"subject1", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u010cerven\u00e9 sa vyma\u017e\u00fa", None))
        self.nearestEvent_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Akcia", None))
        self.deleteEvent.setText(QCoreApplication.translate("Form", u"Odstranit", None))
        self.button_mainPage.setText(QCoreApplication.translate("Form", u"Hlavna strana", None))
        self.button_prednaska_link.setText(QCoreApplication.translate("Form", u"Predn\u00e1\u0161ka", None))
        self.email_prednaska.setText(QCoreApplication.translate("Form", u"email", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"link na predn\u00e1\u0161ku", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"poznamky", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Odobrat", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"link na cvi\u010denie", None))
        self.label_9.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Pridat ulohu", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Sablony", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kedy v rozvrhu", None))
        self.name_prednaska.setText(QCoreApplication.translate("Form", u"meno", None))
        self.button_cviko_link.setText(QCoreApplication.translate("Form", u"Cvi\u010denie", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Link na is s predmetom", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.open_file.setText(QCoreApplication.translate("Form", u"Otvorit s\u00fabor", None))
        self.label_backround.setText(QCoreApplication.translate("Form", u"Backround", None))
        self.button_dokumentovyserver.setText(QCoreApplication.translate("Form", u"Dokumentovy server", None))
        self.name_cviko.setText(QCoreApplication.translate("Form", u"meno", None))
        self.email_cviko.setText(QCoreApplication.translate("Form", u"email", None))
        self.it_was_copied.setText(QCoreApplication.translate("Form", u"Skop\u00edrovan\u00e9", None))
        self.cviko.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

