import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 900
h = 600

class Examen1(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)

        textLabel = QLabel(self)
        textLabel.setText("Examen1")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)