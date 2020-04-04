import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 1000
h = 600

class Mario(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)

        backgroundLabel = QLabel(self)
        backgroundLabel.setScaledContents(True)
        backgroundPixmap = QPixmap('./images/marioBackground.jpg').scaled(w, h)
        backgroundLabel.setPixmap(backgroundPixmap)
        #backgroundLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # self.setStyleSheet("QLabel {font: 80pt Comic Sans MS}")
        textLabel = QLabel(self)
        textLabel.setText("<h1><span style='color: red; font-size: 80px'>Oh, Hello there! It's me, Mario!&nbsp;</span></h1>")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)

        pictureLabel = QLabel(self)
        testPixmap = QPixmap('./images/icon.png').scaled(100, 100)
        pictureLabel.setPixmap(testPixmap)
        pictureLabel.move(w/100, h/60)
        pictureLabel.resize(w/10, h/6)

class BarFme(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)

        backgroundLabel = QLabel(self)
        backgroundLabel.setScaledContents(True)
        backgroundPixmap = QPixmap('./images/marioBackground.jpg').scaled(w, h)
        backgroundLabel.setPixmap(backgroundPixmap)