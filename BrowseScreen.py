from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys


class BrowseScreen(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(BrowseScreen, self).__init__()
        uic.loadUi("UiForms/BrowseScreen.ui", self)
        self.parent = parent
        self.labelArr = []

        self.testArr = ["steak", "sausage", "pizza", "Curry", "pork chops", "cookies"]

        #connect buttons and functions
        self.breakfast = self.findChild(QtWidgets.QPushButton, 'breakfastButton')
        self.lunch = self.findChild(QtWidgets.QPushButton, 'lunchButton')
        self.dinner = self.findChild(QtWidgets.QPushButton, 'dinnerButton')
        self.snack = self.findChild(QtWidgets.QPushButton, 'snackButton')
        self.search = self.findChild(QtWidgets.QPushButton, 'searchButton')

        self.breakfast.clicked.connect(self.breakfast_pressed)
        self.lunch.clicked.connect(self.lunch_pressed)
        self.dinner.clicked.connect(self.dinner_pressed)
        self.snack.clicked.connect(self.snack_pressed)
        self.search.clicked.connect(self.search_pressed)

        #connect labels
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel1'))
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel2'))
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel3'))
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel4'))
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel5'))
        self.labelArr.append(self.findChild(QtWidgets.QPushButton, 'rLabel6'))

    def breakfast_pressed(self):
        for i in range(len(self.labelArr)):
            self.labelArr[i].setText(self.testArr[i])

    def lunch_pressed(self):
        self.labelArr[1].setText("hello")

    def dinner_pressed(self):
        self.labelArr[2].setText("hello")

    def snack_pressed(self):
        self.labelArr[3].setText("hello")

    def search_pressed(self):
        self.labelArr[4].setText("darling")




