import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.final import Final

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


# def secondExerciseQuestion(self):
#         self.videoWidget.hide()
#         self.nextNewButton.hide()

#         pixmap = QPixmap("./images/examen2/enunciat2resposta.png").scaled(w,h)
#         self.backgroundImage.setPixmap(pixmap)

#         self.textBubble.hide()
#         self.textField.hide()
#         self.nextButton.hide()

#         self.inputPassword.show()
#         self.checkButton.show()

#         self.previousButton.move(0.12*w, 0.845*h)
#         self.previousButton.clicked.disconnect()
#         self.previousButton.clicked.connect(self.videoScreen)
    
#     def checkAnswerSecondExercise(self):
#         p = self.inputPassword.text()
#         if p == "729":
#             self.solved()
        
        
#     def solved(self):
#         self.examen3 = Examen3()
#         self.close()

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
        self.inputPasswordExercici2 = QLineEdit(self)
        self.checkButtonExercici2 = QPushButton('QED', self)
        self.checkButton = QPushButton('QED', self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap(resource_path("./images/examen2/huganawar.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon(resource_path('./images/icons/previous.png')))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap(resource_path("./images/icons/textBubble.png"))
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)
        self.textBubble.show()

        self.textField.setText('''<p> <b> Lázaro:</b> BRAVO! Espectacular! Qué luego digan que las clases de N*mèr**a son aburridas. Que opinas tu Carles? Qué? Como que hoy no hay clase? Que hoy es el examen!? Y yo sin enterarme... Entonces les has puesto un examen tuyo? Menos mal porque yo no tenia nada preparado. Bueno, pues lo que iba deciendo, que ya podeis seguir con vuestros problemas, no os molesto más. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)
        self.textField.show()

        self.inputPassword.setGeometry(0.67*w, 0.855*h, 0.06*w, 0.04*h)
        self.inputPassword.setMaxLength(5)
        self.inputPassword.hide()

        self.inputPasswordExercici2.setGeometry(0.78*w, 0.848*h, 0.06*w, 0.04*h)
        self.inputPasswordExercici2.setMaxLength(5)
        self.inputPasswordExercici2.setFrame(False)
        self.inputPasswordExercici2.hide()

        self.checkButtonExercici2.move(0.85*w, 0.843*h)
        self.checkButtonExercici2.clicked.connect(self.checkAnswerSecondExercise)
        self.checkButtonExercici2.hide()

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.thirdExerciseZero)
        self.nextButton.show()

        self.checkButton.move(0.78*w, 0.85*h)
        self.checkButton.clicked.connect(self.checkAnswerThirdExercise)
        self.checkButton.hide()

        self.hide()
        self.show()

    def thirdExerciseZero(self):
        self.hide()
        self.show()
        self.inputPasswordExercici2.show()
        self.checkButtonExercici2.show()
        self.previousButton.show()

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()

        pixmap = QPixmap(resource_path("./images/examen2/enunciat2resposta.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        self.previousButton.clicked.connect(self.initWindow)
    
    def thirdExerciseFirst(self):
        self.hide()
        self.show()
        self.inputPasswordExercici2.hide()
        self.checkButtonExercici2.hide()
        self.previousButton.hide()

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        pixmap = QPixmap(resource_path("./images/examen2/lazaro.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)

        self.textField.setText('''<p> -  Quin espectacle, quin show, quina exhibició de talent! I jo fent un examen de N*mèr**a... Tot i que haig de reconèixer que fins ara tot està anant prou bé, tinc una sensació estranya que no havia sentit mai...  una sensació com de... que m'estan sortint els exercicis. I tampoc em puc queixar, al cap i a la fi, està sent un examen de N*mèr**a. Tret del toc musical del primer exercici, la resta és prou coherent, de fet, ha sortit una matriu i tot. Mira, sembla que està entrant algú a la classe. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.thirdExercisePi)

    def thirdExercisePi(self):
        pixmap = QPixmap(resource_path("./images/examen3/merceClasse.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> - Home! La Morsè Oller! Que estrany, no me l'esperava, em pensava que havia dit que tenia un congrés de punts i ratlles a Colòmbia. <br> <b> Morsè Oller: <b> ...- .- -.  -.. --- ...  ... . --- .-. . ...  .--. --- .-.  .-.. .-  -.-. .- .-.. .-.. .  -.--  .- -. ---  .-.. .  .--. .-. . --. ..- -. - .-  .- .-..  --- - .-. --- ---···  .--. . .-. -.. --- -. . --··--     ..- ... - . -..  ... .- -... .  ... ..- -- .- .-. ··--··  -.--     . .-..  --- - .-. ---  .-. . ... .--. --- -. -.. . ---···  .... --- -- -... .-. .  .--. ..- . ...  -.-. .-.. .- .-. --- --··--  . .-..  -- . -.. .. - . .-. .-. .- -. . --- </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.thirdExerciseFirst)

        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.thirdExerciseSecond)

    def thirdExerciseSecond(self):
        pixmap = QPixmap(resource_path("./images/examen3/merceClasse.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - JAJAJAJAJA, tan de la broma com sempre la Morsè, sort que vaig anar a la xerrada de morse de la franja cultural del mes passat, des d'aleshores he entès totes les classes de N*mèr**a. Vinga va, prou de perdre el temps i anem a centrar-nos en el tercer i últim exercici, que haig d'anar a estudiar per les recuperacions. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.79*h)

        self.inputPassword.hide()
        self.checkButton.hide()

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()
        self.previousButton.show()

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.thirdExercisePi)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.thirdExerciseQuestion)

    def thirdExerciseQuestion(self):
        pixmap = QPixmap(resource_path("./images/examen3/enigma3.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()

        self.inputPassword.show()
        self.checkButton.show()

        self.previousButton.move(0.12*w, 0.845*h)
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.thirdExerciseSecond)

    def solved(self):
        self.final = Final()
        self.close()
    
    def checkAnswerThirdExercise(self):
        p = self.inputPassword.text()
        if p == "432":
            self.solved()

    def checkAnswerSecondExercise(self):
        p = self.inputPasswordExercici2.text()
        if p == "729":
            self.thirdExerciseFirst()