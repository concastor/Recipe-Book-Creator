from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QLineEdit, QWidget, QLabel
from PyQt5 import uic, QtWidgets
import sys


class createUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(createUi, self).__init__()
        self.window = uic.loadUi("UiForms/createScreen.ui", self)
        self.parent = parent


        self.create_base()

    def create_base(self):
        Hlayout = QHBoxLayout()
        AddVLayout = QVBoxLayout()
        displayV = QVBoxLayout()

        ingInput = QLineEdit(self)
        ingInput.setPlaceholderText("please enter an ingredient")
        btn = QLabel(self)
        btn.setText("holy shit")

        Hlayout.addWidget(ingInput)
        Hlayout.addWidget(btn)

        # Hlayout.addLayout(displayV)
        # Hlayout.addLayout(AddVLayout)

        #set the horizontal layout as main
        widget = QWidget()
        widget.setLayout(Hlayout)
        self.window.setCentralWidget(widget)

