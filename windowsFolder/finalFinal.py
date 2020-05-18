import sys
import time
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

w = 900
h = 600

class FinalFinal(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.textField = QLabel(self)
        self.final = QPushButton('The End', self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.78*h)

        self.textField.setText('''<p> Esperem que us ho hagueu passat molt bé, hagueu passat una bona estona amb la gang i hagueu pogut desconnectar una mica de tot el que està passant i dels examens. Cuideu-vos i molta sort amb aquest final de curs!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.82*h)
        self.textField.show()

        self.final.move(0.45*w, 0.9*h)
        self.final.clicked.connect(self.close)

        try:
            self.textBubble.show()
            self.textField.show()
            self.nextButton.show()
        except:
            pass

        self.hide()
        self.show()