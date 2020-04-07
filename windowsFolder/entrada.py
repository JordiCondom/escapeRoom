from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.bar import Bar

w = 900
h = 600

class Entrada(QWidget):
    def __init__(self):
        super(Entrada, self).__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.initWindow()

    def initWindow(self):
        #palette = self.palette()
        #palette.setColor(self.backgroundRole(), Qt.black)
        #self.setPalette(palette)
        pixmap = QPixmap("./images/black.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        bubblePM = QPixmap("./images/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText("hola aquesta és la primera pestanya")
        self.textField.adjustSize()
        self.textField.move(0.15*w, 0.8*h)

        self.nextButton.move(0.85*w,0.85*h)
        self.nextButton.setIcon(QIcon('./images/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.arribadaFme)

        self.show()

    def arribadaFme(self):
        pixmap = QPixmap("./images/entradafme3.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.textField.setText("hola aquesta és la segona")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.entradaFme)

        self.show()

    def entradaFme(self):
        pixmap = QPixmap("./images/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("i aquesta és la tercera, que més tard es separarà en dues diferents")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.rellotge)

    def rellotge(self):
        pixmap = QPixmap("./images/hora.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        #self.nextButton.hide()

        self.passwordField = QTextEdit(self)
        self.passwordField.setPlaceholderText("Introduce la respuesta")
        self.passwordField.setGeometry(0.1*w,0.75*h,0.8*w,0.2*h)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.checkAnswer)


    def checkAnswer(self):
        password = "guapo"
        #print(password)
        answer = self.passwordField.toPlainText()
        if answer == password:
            self.enigmaSolved()

    def enigmaSolved(self):
        self.bar = Bar()
        self.close()