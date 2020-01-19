from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from mainUi import main_ui
import sys
from SplashUI import splash_ui


class Main:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.splash = splash_ui(parent=self)
        self.main = main_ui(parent=self)

        #displays the splash screen
        self.splash.setFixedSize(self.splash.size())
        self.app.exec_()

    def test(self):
        self.main.show()


main = Main()





