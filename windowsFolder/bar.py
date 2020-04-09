import sys
from PyQt5 import QtGui, QtWidgets
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
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/bar/sergio.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''Carai, no m'esperava tenir un començament de dia tan atrafegat. De fet, ara que hi penso, podria haver tret el mòbil i el regle i podria haver-ho solucionat tot molt més ràpid. Bé, què hi farem, ara no és moment de penedir-se del passat, s'ha de mirar al futur, haig de ser fort. Hmmm, em demanaré un café amb llet i un croissant, que em sembla que fan oferta.''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.piratas)

    def piratas(self):
        pixmap = QPixmap("./images/bar/piratas.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.previousButton.show()

        self.textField.setText('''ARRRRRRR! Què et passa a tu, mariner d'aigua UB? No et quedis com un estaquirot, digues el que vols tros de quòniam!''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        try: 
            self.previousButton.clicked.disconnect()
        except:
            pass
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.piratas2)

    def piratas2(self):
        self.textField.setText("2 de piratas perquè suposo que va pa rato")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.piratas)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)

    def resposta(self):
        pixmap = QPixmap("./images/bar/piratas.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("A sobre ens ha portat un bitllet de 100 amb el pergamino, i vol el canvi abans d'aquesta tarda. Ens pots dir quant li hem de tornar al pringat aquest? Vull dir al pirata aquest?")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.textField.show()
        self.textBubble.show()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.piratas2)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.enigma)

    def enigma(self):
        pixmap = QPixmap("./images/bar/enigmaBar.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.hide()
        self.textBubble.hide()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.resposta)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.luis)

    def luis(self):
        pixmap = QPixmap("./images/bar/luis.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.show()
        self.textBubble.show()
        self.previousButton.hide()

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
        self.pati = Pati()
        self.close()

