from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys


class BrowseScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(BrowseScreen, self).__init__()
        uic.loadUi("BrowseScreen.ui", self)
        self.parent = parent

        #connect start_button
        # self.start_button = self.findChild(QtWidgets.QPushButton, 'startButton')
        # self.start_button.clicked.connect(self.start_pressed)

        # self.show()

    def start_pressed(self):
        self.parent.display_main_screen()
        self.hide()



