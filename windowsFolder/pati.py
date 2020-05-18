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

        self.textField.setText('''<p>- Què esta passant, què fa tanta gent al pati? Perdona, que m'he perdut alguna cosa? Què és tota aquesta gent? <br>
        <b>Estudiant anònim de 8è: </b> No home no, tranquil, és que avui hi ha examen d'EDE's i hem quedat per fer NP i celebrar-ho. Apuntat-hi, a les 9:00 farem un comunicat i a les 9:30 toquen lectures de finals d'altres anys.<p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

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

        self.textField.setText('''<p>- Home Covit! Com portes EDE's? Vergonyós lo d'aquesta gent eh, sembla una festa de dia això. Haurien de venir els de Festes del 99 i tothom aniria directe a l'examen. Espera, no estaràs pas pensant en fer NP no?<br>
        <b>Covit:</b> Doncs mira, és que he tingut un problema...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.previousButton.show()
        try:
            self.previousButton.disconnect()
        except:
            pass
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.covit2)

    def covit2(self):
        pixmap = QPixmap("./images/pati/covit.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p><b>Covit:</b> Portava EDE's perfecte, fins i tot millor que Algorísmia en el seu moment, t'he explicat mai que vaig treure un 8.25 al final del pràctic? Però resulta que m'he imprès aquest formulari que l'Iñaki va fer a l'ordinador del CFIS i no entenc res de res. Pel que es veu va tenir algun problema mentre el feia i no m'ha explicat com desxifrar-lo. Sense aquest formulari no puc assegurar el punt del teorema xinès del residu i així és impossible que aprobi. Si vols fes-li una ullada però t'asseguro que no en treuràs pas res. Crec que només estan bé les majúscules...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.textBubble.show()

        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.covit)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.formulari)

    def formulari(self):
        pixmap = QPixmap("./images/pati/formulari.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("")
        self.textBubble.hide()

        self.inputAge.hide()
        self.checkButton.hide()
        self.nextButton.show()

        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.covit2)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)

    def resposta(self):
        pixmap = QPixmap("./images/pati/covit.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText("- Mira Covit, la resposta a totes les preguntes de l'examen, i en particular, a la pregunta més important de totes, la del teorema xinès del residu és:")
        self.textField.resize(400, 200)
        self.textField.move(0.167*w, 0.8*h)
        self.textBubble.show()

        self.inputAge.show()
        self.checkButton.show()
        self.nextButton.hide()

        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.formulari)
        
        self.checkButton.show()

    def checkAnswer(self):
        if self.inputAge.toPlainText() == "39":
            self.inputAge.hide()
            self.checkButton.hide()
            self.gracies()

    def gracies(self):
        pixmap = QPixmap("./images/pati/covit2.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.previousButton.hide()
        self.hide()
        self.show()

        self.textField.setText('''<p> <b>Covit:</b> Ostres, moltes gràcies! És veritat, ara me'n recordo que el professor va dir que la resposta seria sempre l'edat del segurata! M'has salvat, si algun dia vaig a Barrokos et convido a un cubata! <br>
        - Si no ha sigut res home, et deixo que he recordat que també haig d'imprimir el formulari de N*mèr**a, molta sort amb EDE's! <br>
        <b>Covit: </b> Igualment amb N*mèr**a! I per cert, recorda vigilar amb les tecles, no ensopeguem dos cops amb la mateixa pedra!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.nextButton.show()
        self.nextButton.disconnect()
        self.nextButton.clicked.connect(self.senyorGrane)

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


        