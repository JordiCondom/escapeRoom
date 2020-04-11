import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.examen1 import Examen1

w = 900
h = 600

class Cfis(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.checkButton = QPushButton(self)
        self.user = QLabel(self)
        self.password = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/cfis/salaCFIS.jpeg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p>- Per fi al CFIS, crec que encara tinc temps de imprimir el formulari. <p>''')
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
        self.nextButton.clicked.connect(self.sistemaOperatiu)
        self.nextButton.show()

        self.checkButton.setIcon(QIcon('./images/icons/next.png'))
        self.checkButton.setStyleSheet("QPushButton{background: transparent;}")
        self.checkButton.move(0.64*w, 0.48*h)
        #self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.user.setText("Usuari CFIS")
        self.user.move(0.36*w, 0.42*h)
        self.user.hide()

        self.password.setText("Contrasenya")
        self.password.move(0.36*w, 0.485*h)
        self.password.hide()

    def sistemaOperatiu(self):
        pixmap = QPixmap("./images/cfis/SO.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p>- Oh no amb quin sistema operatiu entro? Tothom sap que la impresora només funciona amb un dels dos, però va canviant cada dia el bo. Als programadors els hi devia semblar molt divertit, però no tinc temps d'equivocar-me. <p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.user.hide()
        self.password.hide()
        self.checkButton.hide()

        self.previousButton.show()
        try:
            self.previousButton.disconnect()
        except:
            pass
        self.previousButton.clicked.connect(self.initWindow)

        self.boto1 = QPushButton('Linux', self)
        self.boto1.move(0.4*w, 0.85*h)
        self.boto1.clicked.connect(self.linux)

        self.boto2 = QPushButton('Windows', self)
        self.boto2.move(0.54*w, 0.85*h)
        self.boto2.clicked.connect(self.windows)
        
        self.boto1.show()
        self.boto2.show()

        self.nextButton.hide()

    def linux(self):
        pixmap = QPixmap("./images/cfis/linux.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        self.inicio()

    def windows(self):
        pixmap = QPixmap("./images/cfis/windows.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        self.inicio()

    def inicio(self):
        self.textField.setText('''<p>- Bueno ara haig d'entrar, només cal que vagi en compte amb les tecles girades i tot anirà bé. Una llàstima que no sigui CFIS, però per sort crec que recordo la contrasenya d'algun dels meus companys...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.hide()
        self.show()
        self.boto1.hide()
        self.boto2.hide()

        self.user.show()
        self.password.show()
        self.checkButton.show()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.sistemaOperatiu)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.ivet)
        self.nextButton.show()

    def ivet(self):
        self.user.setText("ivet.acosta@cfis.com")
        self.user.adjustSize()
        self.password.setText("satisfye")
        self.password.adjustSize()

        self.textField.setText('''<p>- Merda, què li passa? No funciona la r! Ara què faig? Aviam si recordo la contrasenya d'algú altre...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.inicio)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.rafah)
        self.nextButton.show()

    def rafah(self):
        self.user.setText("rafah.hajjar@cfis.com")
        self.user.adjustSize()
        self.password.setText("ab")
        self.password.adjustSize()

        self.textField.setText('''<p>- Vale tampoc, també havia de tenir una r... La del Condom ni la provo que en té dues. Ah espera, me'n sé una altra!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.ivet)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.marc)
        self.nextButton.show()

    def marc(self):
        self.user.setText("marc.herault@cfis.com")
        self.user.adjustSize()
        self.password.setText("ecoolt")
        self.password.adjustSize()

        self.textField.setText('''<p>- De veritat no hi ha ningú en tot el CFIS amb una contrasenya sense r!? Ostres! Ja ho tinc! Em sembla que la de l'Andreu té només Xifres, per algún motiu... El problema és que no recordo quines eren exactament. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.rafah)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.marc)
        self.nextButton.show()