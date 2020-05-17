import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 900
h = 600

class Final(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.caraMerce = QLabel(self)
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

        self.textField.setText('''<p> - I la resposta és... 432! Doncs crec que ja ho tindríem, primer exercici... segon exercici... i tercer! Tots acabats i en fulls separats, crec que va sent hora d'entregar aquest examen d'aquesta assignatura de merda, per fi me'n puc desfer, per fi podré no gastar l'hora i mitja de dilluns i divendres que els meus solidaris companys feien servir per restregar-me lo bé que s'ho passaven fent birres al bar. I tot això? Per a què? Per a que acabin traient la mateixa nota que jo, o millor? N'estic fart. <b> ( Silenci ) </b> Hola Morsè, et vinc a entregar el final de la millor assignatura que he fet en la meva vida, gràcies per tot</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.76*h)
        self.textField.show()

        merce = QPixmap("./images/examen3/merce.jpg").scaled(135,135)
        self.caraMerce.setPixmap(merce)
        self.caraMerce.move(0.68*w, 0.07*h)
        self.caraMerce.show()

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
        
        self.nextButton.clicked.connect(self.finalFirst)

        self.hide()
        self.show()

    def finalFirst(self):
        self.textField.setText('''<p> <b> Morsè Oller: </b> . ... -.-. --- .-.. - .-  -. --- ..  -. ---  .... .- ...  .--. --- ... .- -  .-. . ...  .-  .-.. ·----· .- .--. .- .-. - .- -  -.. ·----· .- ... ... .. --. -. .- - ..- .-. .- <br> - Que no he posat res a l'apartat d'assignatura?! (M'ha enxampat) És que... com t'explico això Morsè... resulta que aquesta part no me l'he pogut estudiar, tenia pensat fer-ho avui al matí però... al final m'he liat (toma aresta) i no he pogut... No tindries pas una pista per ajudar-me? De quina assignatura estem parlant?</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        try:
            self.previousButton.clicked.disconnect()
        except: 
            pass
        
        self.previousButton.clicked.connect(self.initWindow)