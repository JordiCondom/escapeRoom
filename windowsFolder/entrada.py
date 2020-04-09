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
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.clockField = InputHora()
        self.checkButton = QPushButton('Comprova', self)
        self.inputLength = TextWithMaxSize2()
        self.initWindowFirst()

        self.show()

    def initWindowFirst(self):
        pixmap = QPixmap("./images/entrada/black.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p>Mínims quadrats, P*A=L*U, error absolut, error relatiu,... va, no et preocupis, has estudiat molt per aquest examen, has anat cada dilluns i cada divendres a classe en comptes  d'anar a la bolera com els  irresponsables dels teus companys, és impossible que suspenguis.</p>''')
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
        self.nextButton.clicked.connect(self.initWindowSecond)

        self.checkButton.hide()
        self.previousButton.hide()

        self.clockField.setParent(self)
        self.clockField.setGeometry(0.3*w,0.775*h,0.4*w,0.15*h)
        self.clockField.hide()

        self.inputLength.setParent(self)
        self.inputLength.setGeometry(0.48*w,0.79*h,0.08*w,0.12*h)
        self.inputLength.hide()

    def initWindowSecond(self):
        pixmap = QPixmap("./images/entrada/black.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> I el més important de tot, ja és l'últim, un cop acabat ja podràs començar a pensar en tot el que disfrutaràs i suaràs (literalment) les recus. A més, has vingut aviat per a poder prendre el cafè tranquil·lament i fer l'última repassadeta de Doolittle i de la descomposició SVD. N*mèr**a és apassionant.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.arribadaFme)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.clicked.connect(self.initWindowFirst)
        self.previousButton.show()

    def arribadaFme(self):
        pixmap = QPixmap("./images/entrada/entradafme3.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.textField.setText('''<p> Mira, ja es veu l'entrada. Quina sensació més estranya però, quanta tranquil·litat. M'atreviria a dir que sembla com si la FME estigués tancada. T'imagines? Per una pandèmia mundial o algo així, segur que en sortirien bons memes.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.initWindowSecond)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.entradaFmeFirst)

    def entradaFmeFirst(self):
        pixmap = QPixmap("./images/entrada/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p><b>Veu en off:</b> et sorprens, a davant de l'FME hi ha una persona estirada mig inconscient, només mou el peu dret. Et pica la curiositat. Després de donar-hi moltes voltes, arribes a l'única conclusió possible, ha anat a Apolo. Decideixes ajudar ja que com bé diu la frase, <i>"Simio ayuda a simio"</i>.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.arribadaFme)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.entradaFmeSecond)

    def entradaFmeSecond(self):
        self.textField.setText('''<p>Es confirma la teoria, ve d'Apolo. Ara bé, no es tracta d'una persona qualsevol, és el segurata de la FME. Pel que es veu li va semblar bona idea sortir a Apolo quan l'endemà tenia responsabilitats. Com era d'esperar, la FME seguia tancada, ningú l'havia obert."</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.entradaFmeFirst)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.entradaFmeTercer)

    def entradaFmeTercer(self):
        pixmap = QPixmap("./images/entrada/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.checkButton.hide()
        self.clockField.hide()

        self.textField.show()
        self.nextButton.show()

        self.textField.setText('''<p>El segurata s'explica: si t'haig de ser sincer, ho vaig petar bastant. Va sonar <i>Yo Perreo Sola</i> 10 cops i 10 van ser els cops que el meu cul va fregar el terra d'Apolo. Ara bé, tota acció té les seves conseqüències, el "perreo" va ser tan intens que vaig trencar el rellotge. Ara no sé quina hora és i no sé si haig d'obrir la FME o no, em podries ajudar? </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.entradaFmeSecond)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.clock)

    def clock(self):
        pixmap = QPixmap("./images/entrada/hora.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.hide()
        self.nextButton.hide()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.entradaFmeTercer)

        self.checkButton.show()
        self.checkButton.move(0.7*w, 0.83*h)
        self.checkButton.clicked.connect(self.checkAnswer)

        self.clockField.show()

    def checkAnswer(self):
        num1 = self.clockField.slot1.toPlainText()
        num2 = self.clockField.slot2.toPlainText()
        num3 = self.clockField.slot3.toPlainText()
        num4 = self.clockField.slot4.toPlainText()
        if num1 == '0' and num2 == '7' and num3 == '1' and num4 == '5':
            self.clockEnigmaSolvedFirst()


    def clockEnigmaSolvedFirst(self):
        self.checkButton.hide()
        self.clockField.hide()
        self.previousButton.hide()
        self.backgroundImage.clear()

        self.hide()
        self.show()
        
        pixmap = QPixmap("./images/entrada/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.show()
        self.nextButton.show()

        self.textField.setText('''<p>Verge Santa dels set dolors! Són les 07:15! Ja hauria d'haver obert la FME fa quinze minuts! Moltes gràcies, has sigut de gran ajuda. Ara només queda obrir la FME... Oh no!  Durant el "perreo" intens no només se m'ha trencat el rellotge, també se m'ha trencat el regle i ara no puc obrir la FME!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.clockEnigmaSolvedSecond)

    def clockEnigmaSolvedSecond(self):
        self.inputLength.hide()
        self.textField.show()
        self.nextButton.show()

        pixmap = QPixmap("./images/entrada/entradafme2.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.checkButton.hide()

        self.textField.setText('''<p>I ara et preguntaràs, per a què carai necessita el segurata de la FME un regle per obrir-la? Doncs la resposta és molt senzilla, veus aquest dibuix de la porta? La contrasenya per entrar a la FME correspon a la <i>segment blau</i> en mil·límetres. Normalment puc mesurar-ho amb el regle, però avui ho veig complicat, per un tema. Tu que en saps tant de números, no em donaries un cop de mà? Jo no en sé gaire d'aquestes coses, només et puc dir que l'àrea d'un cercle és 1587*pi.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.previousButton.show()
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.clockEnigmaSolvedFirst)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.enigma)

    def enigma(self):
        pixmap = QPixmap("./images/entrada/enigma.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)


        self.textField.move(0.167*w, 0.8*h)
        self.textField.hide()
        self.nextButton.hide()

        self.inputLength.show()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.clockEnigmaSolvedSecond)

        self.checkButton.show()
        self.checkButton.clicked.disconnect()
        self.checkButton.clicked.connect(self.checkSecondAnswer)

    def checkSecondAnswer(self):
        if self.inputLength.toPlainText() == "69":
            self.heEntrat()

    def heEntrat(self):
        pixmap = QPixmap("./images/entrada.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

        self.checkButton.hide()
        self.inputLength.hide()
        self.previousButton.hide()


        self.textField.show()
        self.textField.setText("Genial, hem entrat! I ara on vaig?")

        self.boto1 = QPushButton('Al bar per dintre', self)
        self.boto1.move(0.4*w, 0.79*h)
        self.boto1.clicked.connect(self.bar)

        self.boto2 = QPushButton('Al bar per fora', self)
        self.boto2.move(0.4*w, 0.85*h)
        self.boto2.clicked.connect(self.bar)
        
        self.boto1.show()
        self.boto2.show()

    def bar(self):
        self.bar = Bar()
        self.close()


class InputHora(QLabel):
    def __init__(self):
        super(InputHora, self).__init__()
        self.setFont(QFont("Times",52))
        hora = QWidget()
        layout = QHBoxLayout()

        self.slot1 = TextWithMaxSize1()
        self.slot2 = TextWithMaxSize1()
        self.slot3 = TextWithMaxSize1()
        self.slot4 = TextWithMaxSize1()
        points = QLabel()
        points.setFont(QFont("Times",30))
        points.setText(":")
        points.setScaledContents(True)

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

    def limit(self):
        s = self.toPlainText()
        if len(s) > 1:
            self.setPlainText(s[0])

class TextWithMaxSize2(QTextEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.limit)
        self.setFont(QFont("Times",52))

    def limit(self):
        s = self.toPlainText()
        if len(s) > 2:
            self.setPlainText("")