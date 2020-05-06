import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.examen3 import Examen3

w = 900
h = 600

class Examen2(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.checkButton = QPushButton('Comprova', self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> - Primer exercici acabat, tot i que té pinta que això serà com el qüestionari de topologia, un cop respons una pregunta, no pots tirar endarrere. No passa res, ara m'haig de centrar en dues coses: el cul del Padró i el segon exercici. Tot i que si m'haig de sincerar, diré que l'últim exercici no m'ha semblat gaire de N*mèr**a, perdoneu, però algú ho havia de dir. Esperem que el següent s'adapti una mica més al que hem fet a classe. Mira! Aquí ve per fi la Morsé!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)
        self.textField.show()

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
            self.textBubble.show()
            self.textField.show()
            self.nextButton.show()
        except:
            pass
        self.nextButton.clicked.connect(self.secondExerciseSecond)

        self.checkButton.move(0.8*w, 0.86*h)
        self.checkButton.clicked.connect(self.checkAnswerSecondExercise)
        self.checkButton.hide()

        self.hide()
        self.show()

    def secondExerciseSecond(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> Aquí va el segon exercici de l'examen</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.initWindow)
    
    def checkAnswerSecondExercise():
        pass