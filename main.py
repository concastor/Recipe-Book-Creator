from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
import sys
from SplashUI import splash_ui

class Main:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = splash_ui()

        #displays the splash screen
        self.window.setFixedSize(self.window.size())
        self.app.exec_()

main = Main()





