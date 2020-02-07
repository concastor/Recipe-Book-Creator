from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore
import sys


class createUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(createUi, self).__init__()
        self.window = uic.loadUi("UiForms/createScreen.ui", self)
        self.parent = parent


        self.create_base()

    def create_base(self):
        Hlayout = QGridLayout()
        AddVLayout = QVBoxLayout()
        displayV = QVBoxLayout()

        #create the input for the ingredients
        ingInput = QLineEdit(self)
        ingInput.setPlaceholderText("Please enter an ingredient")
        ingInput.setMaximumWidth(self.window.width()/2)
        ingInput.setMinimumWidth(self.window.width()/3)

        btn = QLabel(self)
        addBtn = QPushButton(self)
        addBtn.setText("add")
        btn.setText("holy shit")

        # Hlayout.addWidget(ingInput)
        # Hlayout.addWidget(btn)
        # print(self.window.width())

        Hlayout.setRowMinimumHeight(0, 20)
        Hlayout.addWidget(ingInput, 1, 0, QtCore.Qt.AlignCenter)
        Hlayout.addWidget(btn, 1, 1,  QtCore.Qt.AlignCenter)
        Hlayout.addWidget(addBtn, 2, 0)

        #set the horizontal layout as main
        widget = QWidget(self)
        widget.setLayout(Hlayout)
        self.window.setCentralWidget(widget)

