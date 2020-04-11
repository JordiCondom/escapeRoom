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
        self.icon = QLabel(self)
        self.inputPassword = QLineEdit(self)
        self.error = QLabel(self)
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

        self.icon.setGeometry(0.05*w, 0.05*h, 70, 70)
        self.icon.hide()

        self.inputPassword.setGeometry(0.36*w, 0.48*h, 0.2*w, 0.04*h)
        self.inputPassword.setMaxLength(20)
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.inputPassword.setFrame(False)
        self.inputPassword.hide()

        self.error.setGeometry(0.38*w, 0.48*h, 0.27*w, 0.2*h)
        self.error.setStyleSheet("color: red;")
        self.error.hide()

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
        self.icon.hide()

    def linux(self):
        linuxPixmap = QPixmap("./images/icons/ubuntu.png").scaled(70,70)
        self.icon.setPixmap(linuxPixmap)
        self.inicio()

    def windows(self):
        windowsPixmap = QPixmap("./images/icons/windows.png").scaled(70,70)
        self.icon.setPixmap(windowsPixmap)
        self.inicio()

    def inicio(self):
        pixmap = QPixmap("./images/cfis/inicio.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

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
        self.icon.show()

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
        pixmap = QPixmap("./images/cfis/inicio.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.user.setText("marc.herault@cfis.com")
        self.user.adjustSize()
        self.password.setText("ecoolt")
        self.password.adjustSize()

        self.textField.setText('''<p>- De veritat no hi ha ningú en tot el CFIS amb una contrasenya sense r!? Ostres! Ja ho tinc! Em sembla que la de l'Andreu té només Xifres, per algún motiu... El problema és que no recordo quines eren exactament. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.user.show()
        self.password.show()
        self.checkButton.show()
        self.icon.show()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.rafah)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.andreu1)
        self.nextButton.show()

    def andreu1(self):
        pixmap = QPixmap("./images/cfis/monedes.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p>- Per algun motiu sempre que li pregunto per la contrasenya a l'Andreu, em recorda aquella partida de monedes que va jugar amb en Barrero i la Casanellas. Però no recordo tot el que va passar, només algunes propietats interessants. Les hauré d'anotar en un fullaviam si ho puc reconstriuir. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.user.hide()
        self.password.hide()
        self.checkButton.hide()
        self.icon.hide()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.marc)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.andreu2)
        self.nextButton.show()

    def andreu2(self):
        pixmap = QPixmap("./images/cfis/bingo.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p>- I després em treu el tema del bingo aquell que va guanyar l'última festa de Nadal. Encara tinc a la motxilla el seu cartró, el meu, el de A, el de B, el de C i el de D, però no recordo quin era el seu. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.andreu1)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.andreu3)
        self.nextButton.show()

    def andreu3(self):
        pixmap = QPixmap("./images/cfis/tetris.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        self.textField.setText('''<p>- Sempre em diu que entre tot allò juntament amb aquella partida de tetris que va jugar tan malament, s'hauria d'estar cec per veure la seva contrasenya. Suposo que vol dir per no veure-la, però em fa molta gràcia perquè sempre s'equivoca. Com quan va triar carrera. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.user.hide()
        self.password.hide()
        self.checkButton.hide()
        self.icon.hide()
        self.inputPassword.hide()
        self.error.hide()

        try:
            self.checkButton.clicked.disconnect()
        except:
            pass

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.andreu2)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)
        self.nextButton.show()

    def resposta(self):
        pixmap = QPixmap("./images/cfis/inicio.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.user.show()
        self.password.show()
        self.checkButton.show()
        self.icon.show()
        self.inputPassword.show()

        try:
            self.checkButton.clicked.disconnect()
        except:
            pass
        self.checkButton.clicked.connect(self.checkAnswer)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.andreu3)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)
        self.nextButton.hide()

    def checkAnswer(self):
        p = self.inputPassword.text()
        if p == "417203":
            self.solved()
        elif len(p) != 6:
            self.error.setText("La contrasenya ha de tenir 6 caràcters")
            self.error.show()
        else:
            p = p.replace('0', 'a')
            p = p.replace('1', '0')
            p = p.replace('2', '1')
            p = p.replace('3', '2')
            p = p.replace('4', '3')
            p = p.replace('5', '4')
            p = p.replace('6', '5')
            p = p.replace('7', '6')
            p = p.replace('8', '7')
            p = p.replace('9', '8')
            p = p.replace('a', '9')
            self.error.setText("La contrasenya " + p + " és incorrecta")
            self.error.show()

    def solved(self):
        self.examen1 = Examen1()
        self.close()

