from PySide2.QtCore import *
from PySide2.QtGui import QTextCharFormat, QDesktopServices
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QThread
from PySide2.QtCore import SIGNAL, QObject

import repackage

from ApkaNaSkolu.Controler.Subject_section import OtherWindow

repackage.up(2)

from ApkaNaSkolu.Model.loadFromdatabases import *
from ApkaNaSkolu.Model.calendarEvents import *
from ApkaNaSkolu.View import app, scenes


class Scennes(scenes.Ui_Form, QtWidgets.QStackedWidget):
    def __init__(self):
        super(Scennes, self).__init__()
        self.setupUi(self)

        # self.thread = QThread()
        # self.thread.started.connect(self.new_thread)
        # self.thread.start()

        # section with setting label with subject part
        self.subject1.installEventFilter(self)
        self.subject2.installEventFilter(self)
        self.subject3.installEventFilter(self)
        self.subject4.installEventFilter(self)
        self.subject5.installEventFilter(self)
        self.subjects_with_status_bars = {self.subject1: self.progressBar, self.subject2: self.progressBar_2,
                                          self.subject3: self.progressBar_3, self.subject4: self.progressBar_4,
                                          self.subject5: self.progressBar_5}

        self.setting_calendar()

        self.todo = Databases()
        self.addSubject.clicked.connect(self.change_screen)
        self.event_types = self.todo.load_events_types()
        self.comboBox.addItems(self.event_types)

        self.label_5.setPixmap(
            '/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/View/Screenshot from 2021-01-21 14-39-23.png')

        self.pushButton.clicked.connect(self.add_item_toDo)
        self.pushButton_2.clicked.connect(self.delete_item_from_toDo)
        self.button_mainPage.clicked.connect(self.go_to_main_frame)

        window.start(self)
        self.button_cviko_link.clicked.connect(window.open_link)
        self.pushButton_6.clicked.connect(window.change_to_do)

        self.set_Subjects_progress_bar()
        self.set_subject()
        self.list_widget()

    def add_item_toDo(self):
        """add new item to to_do_list, reads it from text line"""
        item = QListWidgetItem(self.newItemToDo.toPlainText())
        self.listWidget.addItem(item)
        app.processEvents()
        self.whole_to_do.append(self.newItemToDo.toPlainText())
        self.todo.save_to_do_list(self.whole_to_do)

    def delete_item_from_toDo(self):
        """delete selected item from to_to_do_list"""
        if self.listWidget.currentItem().backgroundColor() == 'red':
            return
        item = self.listWidget.currentItem().text()
        self.whole_to_do = self.todo.delete_from_list(item, self.whole_to_do)
        self.listWidget.currentItem().setBackgroundColor('red')
        self.todo.save_to_do_list(self.whole_to_do)

    def setting_calendar(self):
        """method to set every events that is connected with calendar, such as color events"""
        self.cal.installEventFilter(self)
        self.calendar_events = CalendarEvents()
        self.print_calendar()
        self.nearestEvent = self.calendar_events.locate_nearest_event()
        # if there is nearest event then set text else nothing
        if self.nearestEvent != '0':
            self.nearestEvent_label.setText(self.calendar_events.events[self.nearestEvent][0])

        else:
            self.nearestEvent_label.setText('Nič')
        self.saveEvent.clicked.connect(self.save_new_event)

    def setting_pixmaps(self):
        """create legends with pictures"""

    def list_widget(self):
        """Show to do list"""
        self.whole_to_do = self.todo.load_list()
        self.listWidget.addItems(self.whole_to_do)

    def set_Subjects_progress_bar(self):
        """make every progress bar invisible on default"""
        self.progressBar.setVisible(False)
        self.progressBar_2.setVisible(False)
        self.progressBar_3.setVisible(False)
        self.progressBar_4.setVisible(False)
        self.progressBar_5.setVisible(False)

    def set_subject(self):
        """name every label with right name of subject"""
        subjects_label = list(self.subjects_with_status_bars.keys())
        for i in range(len(subjects_label)):
            subjects_label[i].setText(self.event_types[i])

    def eventFilter(self, object, event):
        """function to show progress bar by every subject"""
        if type(object) == QCalendarWidget and event.type() == QEvent.MouseButtonRelease:
            self.show_selected_event()

        if type(object) == QLabel:
            if event.type() == QEvent.Enter:
                self.subjects_with_status_bars[object].setVisible(True)

            elif event.type() == QEvent.Leave:
                self.subjects_with_status_bars[object].setVisible(False)

    def print_calendar(self):
        """Paint those dates that are booked"""
        format = QTextCharFormat()
        format.setBackground(Qt.yellow)

        for date in self.calendar_events.events.keys():
            date = date.split(',')
            date = QDate(int(date[0]), int(date[2]), int(date[1]))
            self.cal.setDateTextFormat(date, format)

    def show_selected_event(self):
        """Show booked event in current text field"""
        date = self.cal.selectedDate()
        date = date.toString("yyyy, d, M")

        if date in self.calendar_events.events.keys():
            self.text_event.setText(self.calendar_events.events[date][0])
            self.text_event_2.setText(self.calendar_events.events[date][2])

    def save_new_event(self):
        date = self.cal.selectedDate()
        date = date.toString("yyyy, d, M")

        text = self.text_event.toPlainText()
        type = self.comboBox.currentText()
        time = self.text_event_2.toPlainText()

        self.calendar_events.save_new_event(text, date, type, time)

    def change_screen(self):
        """set current screen to second"""
        print(self.currentIndex())
        self.stackedWidget.setCurrentIndex(1)

    def go_to_main_frame(self):
        """set current screen to main frame"""
        self.stackedWidget.setCurrentIndex(0)


# to work you have to create all scenes and connected classes together and in main
window = OtherWindow()

app = QtWidgets.QApplication()
qt_app = Scennes()
qt_app.show()
app.exec_()
