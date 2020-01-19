from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys


class main_ui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(main_ui, self).__init__()

        uic.loadUi("mainScreen.ui", self)
        self.parent = parent
        # self.show()

    def show_screen(self):
        self.show()
