from PySide2 import QtWidgets
from ApkaNaSkolu.View import app


class MyWindow(app.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def changeTextLabel(self):
        self.time.setText('Ahoj ako sa mas')


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyWindow()
    qt_app.show()
    qt_app.changeTextLabel()
    app.exec_()