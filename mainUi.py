from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys


class main_ui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(main_ui, self).__init__()

        uic.loadUi("mainScreen.ui", self)
        self.parent = parent

        #connect buttons to code
        self.create_button = self.findChild(QtWidgets.QPushButton, 'CreateButton')
        self.browse_button = self.findChild(QtWidgets.QPushButton, 'browseButton')

        #connect buttons to functions
        self.browse_button.clicked.connect(self.browse_button_clicked)
        self.create_button.clicked.connect(self.create_button_clicked)

    def create_button_clicked(self):
        print("fuck")

    def browse_button_clicked(self):
        print("shit")
        self.parent.display_browse_screen()
        self.hide()

    def show_screen(self):
        self.show()
