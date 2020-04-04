import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 1000
h = 600

class Entrada(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)

        textLabel = QLabel(self)
        textLabel.setText("Entrada")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)

        backgroundImage = QLabel(self)
        pixmap = QPixmap("./images/entradafme.jpg").scaled(w,h)
        backgroundImage.setPixmap(pixmap)