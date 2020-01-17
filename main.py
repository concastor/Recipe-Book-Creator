from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


class Main:

    def __init__(self):
        self.app = QApplication([])
        #loads ui from file
        Form, Window = uic.loadUiType("main page.ui")
        self.form = Form()
        self.window = Window()

    #Displays the main window of the program
    def show_window(self):
        self.form.setupUi(self.window)
        self.window.show()
        self.app.exec_()


main = Main()
main.show_window()