import sys
import os
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.pati import Pati

w = 900
h = 600

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Bar(QWidget):
    def __init__(self):
        super(Bar, self).__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.checkButton = QPushButton('Comprova', self)
        self.inputEuros = InputEuros()
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap(resource_path("./images/bar/preus.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon(resource_path('./images/icons/previous.png')))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap(resource_path("./images/icons/textBubble.png"))
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p>Carai, no m'esperava tenir un començament de dia tan atrafegat. De fet, ara que hi penso, podria haver tret el mòbil i el regle i podria haver-ho solucionat tot molt més ràpid. Bé, què hi farem, ara no és moment de penedir-se del passat, s'ha de mirar al futur, haig de ser fort. Hmmm, em demanaré un café amb llet i un croissant, que em sembla que fan oferta.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.piratas)

        self.checkButton.move(0.76*w, 0.83*h)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.inputEuros.setParent(self)
        self.inputEuros.setGeometry(0.53*w,0.79*h,0.23*w,0.12*h)
        self.inputEuros.hide()

    def piratas(self):
        pixmap = QPixmap(resource_path("./images/bar/piratas.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        
        self.previousButton.show()

        self.textField.setText('''<p>+ ARRRRRRR! ¿Qué conyo quieres, marinero de agua chucky? ¡Ojo al parche filibustero¡ Date prisa que hoy tenemos mucho trabajo, que sino no sé por qué retruécanos nos hemos quedado a dormir en el maldito barco y empezado a trabajar tan puto temprano. <br>
        - Hola...? M'agradaria un café amb llet i un croissant amb l'oferta siusplau. </p>''')
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
        self.textField.setText('''<p>+ A ver, ¿tú eres tonto? ¿Crees que te voy a servir esta mierda? Yo sólo sirvo ron. Y además, ¿no ves que estamos ocupados con un pedido? Nos ha llegado este pergamino anónimo y no sabemos qué caralho nos está pidiendo, deben ser los truhanes de la UB, que siempre andan con sus bromitas de carrera. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.piratas)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.resposta)

    def resposta(self):
        pixmap = QPixmap(resource_path("./images/bar/piratas.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> + Junto con el pergamino venía un billete de 100 euros y quieren el cambio antes de esta tarde, ¿se puede saber cómo voy a saber yo qué quiere esta gente? Mira zagal, qué te pareceria tener un croissant y un café con leche gratis (casi). Si nos dices cuanto le debemos a este tal anónimo te invitamos. Aquí tienes el pergamino.</p>''')
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
        pixmap = QPixmap(resource_path("./images/bar/enigmaBar.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.hide()
        self.textBubble.hide()
        self.nextButton.show()

        self.inputEuros.hide()
        self.checkButton.hide()

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.resposta)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.answer)

    def answer(self):
        pixmap = QPixmap(resource_path("./images/bar/piratas.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.show()
        self.textBubble.show()
        self.nextButton.hide()

        self.inputEuros.show()
        self.checkButton.show()

        self.textField.setText("- Tranquils bucaneros, és ben senzill, només heu de tornar:")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(300, 200)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.enigma)

    def checkAnswer(self):
        if self.inputEuros.euros.toPlainText() == "17" and self.inputEuros.cents.toPlainText() == "89":
            self.inputEuros.hide()
            self.checkButton.hide()
            self.luis()

    def luis(self):
        pixmap = QPixmap(resource_path("./images/bar/luis.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

        self.nextButton.show()
        self.previousButton.hide()

        self.textField.setText("+ ¡Me cago en la puta, 21 lomoquesos! Luís SinBarbanegra, saca la espátula, vamos a pasear unos cuantos cerdos por la plancha. Aquí tienes, un croissant y un café con leche, serán 2,10 euros. ¿Te creías que te iba a invitar? En tus sueños xaval, venga paga, pa-ya-so.")
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.ruben)

    def ruben(self):
        pixmap = QPixmap(resource_path("./images/bar/ruben.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p>- 21 lomoquesos, qui carai vol 21 lomoquesos? Què farà, alimentar joves famèlics per les tardes? Ves a saber tu, un afortunat deu ser, no tothom paga amb bitllets de 100. Aniré a repassar una estona al pati, que ja s'apropa l'hora de l'examen, ara si que si, ja no em distreuré més i em posaré a estudiar.<br>
        <b>Veu en off de Rubén:</b> ¿Ese desgraciao me está pisando la silla?<p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.pati)

    def pati(self):
        self.pati = Pati()
        self.close()

class InputEuros(QLabel):
    def __init__(self):
        super(InputEuros, self).__init__()
        self.setFont(QFont("Times",45))
        hora = QWidget()
        layout = QHBoxLayout()

        self.euros = TextWithMaxSize2()
        self.cents = TextWithMaxSize2()

        coma = QLabel()
        coma.setFont(QFont("Times",45))
        coma.setText(",")
        coma.setScaledContents(True)

        euro = QLabel()
        euro.setFont(QFont("Times",45))
        euro.setText("€")
        euro.setScaledContents(True)

        layout.addWidget(self.euros)
        layout.addWidget(coma)
        layout.addWidget(self.cents)
        layout.addWidget(euro)

        self.setLayout(layout)

class TextWithMaxSize2(QTextEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.limit)
        self.setFont(QFont("Times",45))

    def limit(self):
        s = self.toPlainText()
        if len(s) > 2:
            self.setPlainText("")
