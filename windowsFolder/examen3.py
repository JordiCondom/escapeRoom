import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.final import Final

w = 900
h = 600


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
        self.caraMerce = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/examen2/enunciat2resposta.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        merce = QPixmap("./images/examen3/merce.jpg").scaled(135,135)
        self.caraMerce.setPixmap(merce)
        self.caraMerce.move(0.68*w, 0.07*h)
        self.caraMerce.hide()

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> -  Quin espectacle, quin show, quina exhibició de talent! I jo fent un examen de N*mèr**a... Tot i que haig de reconèixer que fins ara tot està anant prou bé, tinc una sensació estranya que no havia sentit mai...  una sensació com de... que m'estan sortint els exercicis. I tampoc em puc queixar, al cap i a la fi, està sent un examen de N*mèr**a. Tret del toc musical del primer exercici, la resta és prou coherent, de fet, ha sortit una matriu i tot. Mira, sembla que està entrant algú a la classe. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)
        self.textField.hide()

        self.inputPassword.setGeometry(0.67*w, 0.855*h, 0.06*w, 0.04*h)
        self.inputPassword.setMaxLength(5)
        self.inputPassword.hide()

        self.inputPasswordExercici2.setGeometry(0.78*w, 0.848*h, 0.2*w, 0.04*h)
        self.inputPasswordExercici2.setMaxLength(20)
        self.inputPasswordExercici2.setFrame(False)
        self.inputPasswordExercici2.show()

        self.checkButtonExercici2.move(0.82*w, 0.89*h)
        self.checkButtonExercici2.clicked.connect(self.checkAnswerSecondExercise)
        self.checkButtonExercici2.show()

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.textBubble.hide()
            self.textField.hide()
            self.nextButton.hide()
        except:
            pass
        self.nextButton.hide()

        self.checkButton.move(0.78*w, 0.85*h)
        self.checkButton.clicked.connect(self.checkAnswerThirdExercise)
        self.checkButton.hide()

        self.hide()
        self.show()
    
    def thirdExerciseFirst(self):
        self.hide()
        self.show()
        self.inputPasswordExercici2.hide()
        self.checkButtonExercici2.hide()
        self.previousButton.hide()

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)

        self.caraMerce.hide()

        self.textField.setText('''<p> - Home! La Morsè Oller! Que estrany, no me l'esperava, em pensava que havia dit que tenia un congrés de punts i ratlles a Colòmbia. <br> <b> Morsè Oller: <b> ...- .- -.  -.. --- ...  ... . --- .-. . ...  .--. --- .-.  .-.. .-  -.-. .- .-.. .-.. .  -.--  .- -. ---  .-.. .  .--. .-. . --. ..- -. - .-  .- .-..  --- - .-. --- ---···  .--. . .-. -.. --- -. . --··--     ..- ... - . -..  ... .- -... .  ... ..- -- .- .-. ··--··  -.--     . .-..  --- - .-. ---  .-. . ... .--. --- -. -.. . ---···  .... --- -- -... .-. .  .--. ..- . ...  -.-. .-.. .- .-. --- --··--  . .-..  -- . -.. .. - . .-. .-. .- -. . --- </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.thirdExerciseSecond)

    def thirdExerciseSecond(self):
        pixmap = QPixmap("./images/examen1/padro_cul.JPG").scaled(w,h)
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
        self.caraMerce.show()
        self.previousButton.show()

        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        
        self.previousButton.clicked.connect(self.thirdExerciseFirst)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.thirdExerciseQuestion)

    def thirdExerciseQuestion(self):
        pixmap = QPixmap("./images/examen3/enigma3.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()
        self.caraMerce.hide()

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