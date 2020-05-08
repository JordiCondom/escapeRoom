import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 900
h = 600

class Examen3(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.inputPassword = QLineEdit(self)
        self.checkButton = QPushButton('Comprova', self)
        self.caraMerce = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        merce = QPixmap("./images/examen3/merce.jpg").scaled(135,135)
        self.caraMerce.setPixmap(merce)
        self.caraMerce.move(0.68*w, 0.07*h)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> - Tercer exercici de l'examen </p>''')
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
        self.nextButton.clicked.connect(self.thirdExerciseFirst)

        self.checkButton.move(0.82*w, 0.89*h)
        self.checkButton.clicked.connect(self.checkAnswerThirdExercise)
        self.checkButton.hide()

        self.hide()
        self.show()
    
    def thirdExerciseFirst(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> Aquí va el tercer exercici de l'examen</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.initWindow)
    
    def checkAnswerThirdExercise(self):
        pass