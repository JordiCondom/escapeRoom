import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.senyorGrane import SenyorGrane

w = 900
h = 600

class Pati(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.checkButton = QPushButton('Comprova', self)
        self.inputAge = TextWithMaxSize2()
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/pati/pati1.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText("Tota aquesta gent farà NP? Sembla una festa de dia")
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
        self.nextButton.clicked.connect(self.covit)

        self.checkButton.move(0.75*w, 0.83*h)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.inputAge.setParent(self)
        self.inputAge.setGeometry(0.65*w,0.79*h,0.08*w,0.12*h)
        self.inputAge.hide()

    def covit(self):
        pixmap = QPixmap("./images/pati/covit.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("Mira! Hi ha el Covit. Que gran s'ha fet, sembla que tingui 19 anys. Tu no estaràs pensant també en fer NP no?")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.covit2)

    def covit2(self):
        self.textField.setText("Doncs sí, perquè no entenc res d'aquest formulari de l'Iñaki. Si almenys sapigués la resposta a una pregunta em presentaria")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.formulari)

    def formulari(self):
        pixmap = QPixmap("./images/pati/formulari.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("")
        self.textBubble.hide()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)

    def resposta(self):
        pixmap = QPixmap("./images/pati/covit.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("Tranquil Covit, la resposta de totes les preguntes de l'examen és:")
        self.textBubble.show()

        self.inputAge.show()
        self.checkButton.show()
        self.nextButton.hide()
        
        self.checkButton.show()

    def checkAnswer(self):
        if self.inputAge.toPlainText() == "39":
            self.inputAge.hide()
            self.checkButton.hide()
            self.gracies()

    def gracies(self):
        pixmap = QPixmap("./images/pati/covit2.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

        self.textField.setText("Uau merci, si imprimeixes algo al CFIS vigila amb les tecles!")

    def senyorGrane(self):
        self.senyorGrane = SenyorGrane()
        self.close()


class TextWithMaxSize2(QTextEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.limit)
        self.setFont(QFont("Times",52))

    def limit(self):
        s = self.toPlainText()
        if len(s) > 2:
            self.setPlainText("")


        