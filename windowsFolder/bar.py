import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 1000
h = 600

class Bar(QWidget):
    def __init__(self):
        super(Bar, self).__init__()

        self.setGeometry(0,0,w,h)
        self.initWindow()

    def initWindow(self):
        textLabel = QLabel(self)
        textLabel.setText("Bar")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)
<<<<<<< HEAD
=======

        backgroundImage = QLabel(self)
        pixmap = QPixmap("./images/LuisDelBar.jpg").scaled(w,h)
        backgroundImage.setPixmap(pixmap)

        self.show()
>>>>>>> 3a7a098e330f77296a4b685757a1659696891ac1
