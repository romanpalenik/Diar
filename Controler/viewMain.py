from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from ApkaNaSkolu.Model.toDoList import *
from ApkaNaSkolu.View import app



class MyWindow(app.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.list_widget()
        self.progressBar.setVisible(False)
        self.progressBar_2.setVisible(False)
        self.progressBar_3.setVisible(False)
        self.progressBar_4.setVisible(False)
        self.progressBar_5.setVisible(False)
        self.subject1.installEventFilter(self)
        self.subject2.installEventFilter(self)
        self.subject3.installEventFilter(self)
        self.subject4.installEventFilter(self)
        self.subject5.installEventFilter(self)
        self.subject_with_status_bars = {self.subject1: self.progressBar, self.subject2: self.progressBar_2, self.subject3: self.progressBar_3, self.subject4: self.progressBar_4, self.subject5: self.progressBar_5}
        self.cal.installEventFilter(self)

    def list_widget(self):
        """Show to do list"""
        todo = ToDoList()
        items = todo.load_list()
        self.listWidget.addItems(items)

    def eventFilter(self, object, event):
        """function to show progress bar by every subject"""
        if type(object) == QCalendarWidget and event.type() == QEvent.MouseButtonRelease:
            print('kliknuty datum')

        if type(object) == QLabel:
            if event.type() == QEvent.Enter:
                self.subject_with_status_bars[object].setVisible(True)

            elif event.type() == QEvent.Leave:
                self.subject_with_status_bars[object].setVisible(False)

    def print_calendar(self):
        date = self.cal.selectedDate()
        print(date)

    def mouseDoubleClickEvent(self, event):
        print("Mouse Double Click Event")


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyWindow()
    qt_app.show()
    app.exec_()
