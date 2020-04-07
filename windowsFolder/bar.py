import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.pati import Pati

w = 900
h = 600

class Bar(QWidget):
    def __init__(self):
        super(Bar, self).__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/bar/sergio.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText("mmmmm crec que em demanaré un café amb llet i un croissant salat, que em sembla que fan oferta")
        self.textField.adjustSize()
        self.textField.move(0.15*w, 0.8*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.piratas)

    def piratas(self):
        pixmap = QPixmap("./images/bar/piratas.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.textField.setText("- ARRRRRR! Som els pirates del bar")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.piratas2)

    def piratas2(self):
        self.textField.setText("2 de piratas perquè suposo que va pa rato")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.enigma)

    def enigma(self):
        pixmap = QPixmap("./images/bar/bandera.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("aquí hi haurà l'enigma suposadament")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.luis)

    def luis(self):
        pixmap = QPixmap("./images/bar/luis.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("superbé! has resolt l'enigma, ets tan bo com la nova comi menjar!")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.ruben)

    def ruben(self):
        pixmap = QPixmap("./images/bar/ruben.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("surto al pati, aviam si em trobo algun Covit amb intencions de fer NP")
        self.textField.adjustSize()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.pati)

    def pati(self):
        pati = Pati()
        self.close()

