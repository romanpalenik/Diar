import repackage


from ApkaNaSkolu.Model.loadFromdatabases import Databases


repackage.up(2)

from PySide2 import QtWidgets, QtGui
from ApkaNaSkolu.View.sekcia import *


class OtherWindow(Ui_MainWindow2, QtWidgets.QMainWindow):
    def __init__(self):
        super(OtherWindow, self).__init__()
        self.setupUi(self)
        self.subject1.setWindowTitle('ahoj')
        self.pushButton_2.clicked.connect(self.on_addItemButton_clicked)

    def start(self):
        pass



    def on_addItemButton_clicked(self):
        item = QListWidgetItem("New Item")
        self.listWidget.addItem(item)




    def set_subject(self):
        self.database = Databases()
        subjects = self.database.load_events_types()
        subjects_label = list(self.subjects_with_status_bars.keys())
        for i in range(len(subjects_label)):
            subjects_label[i].setText(subjects[i])
