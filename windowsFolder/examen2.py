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
        self.inputPassword = QLineEdit(self)
        self.checkButton = QPushButton('QED', self)
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

        self.textField.setText('''<p> - Primer exercici acabat, tot i que té pinta que això serà com el qüestionari de topologia, un cop respons una pregunta, no pots tirar endarrere. No passa res, ara m'haig de centrar en dues coses: el cul del Padró i el segon exercici. Tot i que si m'haig de sincerar, diré que l'últim exercici no m'ha semblat gaire de N*mèr**a, perdoneu, però algú ho havia de dir. Esperem que el següent s'adapti una mica més al que hem fet a classe. Mira! Aquí ve per fi en Lázaro!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)
        self.textField.show()

        self.inputPassword.setGeometry(0.78*w, 0.848*h, 0.2*w, 0.04*h)
        self.inputPassword.setMaxLength(20)
        self.inputPassword.setFrame(False)
        self.inputPassword.hide()

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

        self.checkButton.move(0.82*w, 0.89*h)
        self.checkButton.clicked.connect(self.checkAnswerSecondExercise)
        self.checkButton.hide()

        self.hide()
        self.show()

    def secondExerciseSecond(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        self.inputPassword.hide()
        self.checkButton.hide()

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> <b> Lázaro:</b> vale ya estoy aquí, perdón por el retraso. Es que uno se lia... y al final acaba pues, mirando vídeos de focas tirandose pedos a las 3 de la mañana, los pedos de las focas, no mios. Aunque tengo que decir que no he llegado tarde por esto, sería patético. Mirad, como sé que os interesa, os lo explico. Resulta que estaba viniendo al examen y me he encontrado con dos personas que todos conocéis muy bien. No solo porque hagan mates, sinó por las millones de visitas que tienen en Youtube, menudo temazo que sacaron el año pasado, madre mía. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.secondExerciseThird)
    
    def secondExerciseThird(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        self.inputPassword.hide()
        self.checkButton.hide()

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> <b> Lázaro:</b> de hecho, justo ahora venían de resaca de la fiesta de Rosalia y Bad Bunny en Sant Esteve Sesrovires. Pero mirad lo increíbles que son, que aún con resaca han aceptado mi solicitud. Y óbviamente os preguntaréis, ¿qué nos importa a nosotros lo que les haya pedido este senyor a estas celebridades en medio de un final de N*mèr**a? Pues os importa, y mucho, porque será la única cosa interesante que os pasará hoy, el mejor espectáculo de vuestras vidas. Chicos y chicas, Carles Padró; hoy tengo la gran suerte y el gran honor de poder presentarles al gran dúo.... (redoble de tambores)... Hugana War!  </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.76*h)

        
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.secondExerciseSecond)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.secondExerciseQuestion)

    def secondExerciseQuestion(self):
        pixmap = QPixmap("./images/examen2/enunciat2resposta.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()

        self.inputPassword.show()
        self.checkButton.show()

        self.previousButton.move(0.12*w, 0.845*h)
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.secondExerciseThird)
    
    def checkAnswerSecondExercise(self):
        p = self.inputPassword.text()
        if p == "729":
            self.solved()
        
        
    def solved(self):
        self.examen3 = Examen3()
        self.close()