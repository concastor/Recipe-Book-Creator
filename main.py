from PyQt5.QtWidgets import QApplication
from PyQt5 import uic, QtWidgets
from mainUi import main_ui
import sys
from SplashUI import SplashUi
from BrowseScreen import BrowseScreen
from createUi import createUi


class Main:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.splash = SplashUi(parent=self)
        self.main_screen = main_ui(parent=self)
        self.browse_screen = BrowseScreen(parent=self)
        self.crete_screen = createUi(parent=self)

        #displays the splash screen
        self.splash.setFixedSize(self.splash.size())
        self.app.exec_()

    def display_main_screen(self):
        self.main_screen.show()

    def display_browse_screen(self):
        self.browse_screen.show()

    def display_create_screen(self):
        self.crete_screen.show()



main = Main()





