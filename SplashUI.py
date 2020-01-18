from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys


class splash_ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(splash_ui, self).__init__()
        uic.loadUi("main page.ui", self)
        #connect start_button
        self.start_button = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.start_button.clicked.connect(self.start_pressed)

        self.show()

    def start_pressed(self):
        print("fucklk")
