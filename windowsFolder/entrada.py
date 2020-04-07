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
        self.passwordField = InputHora()
        self.initWindow()

    def initWindow(self):
        #palette = self.palette()
        #palette.setColor(self.backgroundRole(), Qt.black)
        #self.setPalette(palette)
        pixmap = QPixmap("./images/entrada/black.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText("hola aquesta és la primera pestanya")
        self.textField.adjustSize()
        self.textField.move(0.15*w, 0.8*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.arribadaFme)

        self.passwordField.setParent(self)
        #self.passwordField.setPlaceholderText("Introduce la respuesta")
        self.passwordField.setGeometry(0.3*w,0.774*h,0.4*w,0.15*h)
        self.passwordField.hide()

        self.show()

    def arribadaFme(self):
        pixmap = QPixmap("./images/entrada/entradafme3.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.textField.setText("hola aquesta és la segona")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.entradaFme)

    def entradaFme(self):
        pixmap = QPixmap("./images/entrada/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("i aquesta és la tercera, que més tard es separarà en dues diferents")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.rellotge)

    def rellotge(self):
        pixmap = QPixmap("./images/entrada/hora.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.hide()
        self.nextButton.move(0.7*w,0.83*h)

        self.passwordField.show()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.checkAnswer)


    def checkAnswer(self):
        num1 = self.passwordField.slot1.toPlainText()
        num2 = self.passwordField.slot2.toPlainText()
        num3 = self.passwordField.slot3.toPlainText()
        num4 = self.passwordField.slot4.toPlainText()
        if num1 == '0' and num2 == '7' and num3 == '1' and num4 == '5':
            self.enigmaSolved()

    def enigmaSolved(self):
        self.bar = Bar()
        self.close()

class InputHora(QLabel):
    def __init__(self):
        super(InputHora, self).__init__()
        hora = QWidget()
        layout = QHBoxLayout()

        self.slot1 = TextWithMaxSize1()
        self.slot2 = TextWithMaxSize1()
        self.slot3 = TextWithMaxSize1()
        self.slot4 = TextWithMaxSize1()
        points = QLabel()
        pm = QPixmap(".images/icons/colon.png")
        points.setPixmap(pm)

        layout.addWidget(self.slot1)
        layout.addWidget(self.slot2)
        layout.addWidget(points)
        layout.addWidget(self.slot3)
        layout.addWidget(self.slot4)

        self.setLayout(layout)

class TextWithMaxSize1(QTextEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.limit)
        #self.setAlignment(Qt.AlignCenter)
        #self.setFontPointSize(50)

    def limit(self):
        if len(self.toPlainText()) > 1:
            self.setPlainText("")
        

