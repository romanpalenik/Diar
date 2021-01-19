import calendar

from PyQt5.QtWidgets import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class dateCalendar(QCalendarWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(self.palette().color(QPalette.Highlight))
        self.color.setAlpha(150)
        # self.selectionChanged.connect(self.updateCells)
        self.dateList = []

    def paintCell(self, painter, rect, date):
        # calling original paintCell to draw the actual calendar
        QCalendarWidget.paintCell(self, painter, rect, date)

        # highlight a particular date
        if date in self.dateList:
            painter.fillRect(rect, self.color)

    def selectDates(self, qdatesList):
        self.dateList = qdatesList
        # this redraws the calendar with your updated date list
        self.updateCells()
