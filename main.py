from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from mainUi import main_ui
import sys
from SplashUI import SplashUi
from BrowseScreen import BrowseScreen


class Main:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.splash = SplashUi(parent=self)
        self.main_screen = main_ui(parent=self)
        self.browse_screen = BrowseScreen(parent=self)

        #displays the splash screen
        self.splash.setFixedSize(self.splash.size())
        self.app.exec_()

    def display_main_screen(self):
        self.main_screen.show()

    def display_browse_screen(self):
        self.browse_screen.show()


main = Main()





