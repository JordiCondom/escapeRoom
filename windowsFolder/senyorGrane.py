import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.cfis import Cfis

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

class SenyorGrane(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.boto1 = QPushButton('Anar al bar per dintre', self)
        self.boto2 = QPushButton('Anar al bar per fora', self)
        self.checkButton = QPushButton('Comprova', self)
        self.X = QLabel(self)
        self.inputLomoquesos = TextWithMaxSize2()
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap(resource_path("./images/senyorGrane/passadissensegrane.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon(resource_path('./images/icons/previous.png')))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap(resource_path("./images/icons/textBubble.png"))
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> <i>Wild Senyor Grané appeared!</i> <br> 
        - Bon dia Senyor Grané! <br>
        <b>Senyor Grané: </b> Ja tornes a estar donant voltes? Vols fer el favor d'estudiar, sempre et veig jugant a cartes amb els teus amiguets o fent el burro pels passadissos, el dia que et vegi estudiant farem una festa de dia a la FME. Escolta jove, no em faries pas un favor tu? Oi que si? Genial doncs, mira t'explico. Ep, no corris, que no et donaré més galetes eh!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.graneFirst)

        self.checkButton.move(0.57*w, 0.855*h)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.inputLomoquesos.setParent(self)
        self.inputLomoquesos.setGeometry(0.4*w,0.855*h,0.14*w,0.05*h)
        self.inputLomoquesos.hide()

        self.boto1.hide()
        self.boto2.hide()

    def graneFirst(self):
        self.textField.setText('''<p> <b>Senyor Grané: </b> Resulta que aquests dies farem unes proves de matemàtiques aquí a la facultat i necessito alimentar un exèrcit de joves famèlics. Ja he fet unes quantes comandes, una abans d'ahir d'1, una ahir d'11 i una altra avui de 21, de la qual encara no m'han tornat el canvi, suposo que el pergamí que els hi vaig enviar no era tan de la ESO com semblava. I et preguntaràs, de què són les comandes? De lomoquesos, ÒBVIAMENT. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.previousButton.show()
        try:
            self.previousButton.disconnect()
        except:
            pass
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.graneSecond)

    def graneSecond(self):
        self.boto1.hide()
        self.boto2.hide()

        self.textField.setText('''<p> - De fet, ja n'he fet dues més, una de 1211 lomoquesos per demà i una altra de 111221 lomoquesos per demà passat. Encara em falta una comanda per demà passat no l'altre, però em fa bastanta mandra anar fins al bar a fer-la, així que hi aniràs tu, que ets ben jove. I si no vols, t'aguantes i hi vas igualment.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)


        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.graneFirst)

        self.nextButton.show()
        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.graneThird)

    def graneThird(self):
        self.boto1.hide()
        self.boto2.hide()

        self.textField.setText('''<p> - No es preocupi, no em fa res passar un segon pel bar, de quants lomoquesos ha de ser la comanda? <br>
        <b>Senyor Grané: </b>Com que de quants lomoquesos ha de ser la comanda? Ja pots comptar que t'ho diré, ja t'he dit tot el que necessites saber. <br>
        - Però Senyor Grané, i si faig una comanda amb un nombre incorrecte de lomoquesos? Hi haurà mini-matemàtics que es quedaran sense provar aquesta delícia.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)


        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.graneFirst)

        self.nextButton.show()
        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.graneFourth)

    def graneFourth(self):
        pixmap = QPixmap(resource_path("./images/senyorGrane/passadissensegrane.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> <b>Senyor Grané: </b>No et preocupis, jo confio en tu. Segueix el teu cor, quan trobis el nombre correcte de lomoquesos sabràs que és el correcte, confia en els teus instints i en la FME jove. Diga'ls-hi que ja passaré a pagar <b>en algun moment </b>posterior a la realització de la comanda. Molta sort. I vols fer el favor d'estudiar'? Que només et veig marejant la perdiu! <br>
        </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.graneThird)

        
        self.boto1.move(0.34*w, 0.875*h)
        self.boto1.clicked.connect(self.graneBar)
        self.boto1.show()

        self.boto2.move(0.54*w, 0.875*h)
        self.boto2.clicked.connect(self.graneBar)
        self.boto2.show()
        
        self.nextButton.hide()
        self.inputLomoquesos.hide()
        self.checkButton.hide()
        self.X.hide()

    def graneBar(self):
        pixmap = QPixmap(resource_path("./images/bar/piratas.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.boto1.hide()
        self.boto2.hide()
        self.nextButton.hide()
        self.hide()
        self.show()

        self.textField.setText('''<p> + ¡Hombreee! ¿Otra vez tú por aquí? A ver, ¿qué mierdas quieres ahora? <br>
        - Venia a fer una comanda de { X }  lomoquesos de part del Senyor Grané, ha dit que passaria a pagar aquesta tarda.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.X.setText('''X = ''')
        self.X.resize(20, 20)
        self.X.move(0.37*w, 0.86*h)
        self.X.show()

        self.inputLomoquesos.show()
        self.checkButton.show()

        self.previousButton.disconnect()
        self.previousButton.clicked.connect(self.graneFourth)

    def checkAnswer(self):
        if self.inputLomoquesos.toPlainText() == "312211":
            self.inputLomoquesos.hide()
            self.checkButton.hide()
            self.X.hide()
            self.previousButton.hide()
            self.hide()
            self.show()
            self.solved()
        else: 
            QMessageBox.about(self, "Error", "Sents una esgarrifança, pot ser que aquesta no sigui la resposta correcta.")

    def solved(self):
        self.textField.setText('''<p> + Perfecto, marchando un pedido de 312211 lomoquesos. ¡Luís Sinbarbanegra! ¡Deja los 39 pedidos que tienes y ponte a trabajar de verdad, que sólo te veo holgazaneando! Y tú, vete a la mierda, sal de mi vista. <br>
        - Adéu adéu. Uf, haig d'anar cagant llets a imprimir el formulari de N*mèr**a, que ja s'apropa l'hora de l'examen i encara no he ni començat a repassar. Què faré si a l'examen surt un exercici de SVD? O pitjor, de Gauss? </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.nextButton.show()
        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.cfisScreen)
    
    def cfisScreen(self):
        self.cfis = Cfis()
        self.close()

class TextWithMaxSize2(QTextEdit):
    def __init__(self):
        super().__init__()
        self.textChanged.connect(self.limit)
        self.setFont(QFont("Times",20))

    def limit(self):
        s = self.toPlainText()
        if len(s) > 9:
            self.setPlainText("")

