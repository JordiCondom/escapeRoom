import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 900
h = 600

class Pati(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)

        self.backgroundImage = QLabel(self)
        pixmap = QPixmap("./images/pati1.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        textLabel = QLabel(self)
        textLabel.setText("Pati")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)