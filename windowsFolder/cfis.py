import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.examen1 import Examen1

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
        self.boto1 = QPushButton('Linux', self)
        self.boto2 = QPushButton('Windows', self)
        self.juanjo = QLabel(self)
        self.tigre = QLabel(self)
        self.motorista = QLabel(self)
        self.fotoAndreu = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap(resource_path("./images/cfis/salaCFIS.jpeg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon(resource_path('./images/icons/previous.png')))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap(resource_path("./images/icons/textBubble.png"))
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> - Per fi, ja hi som, després de tot el rebombori que hi ha hagut aquest matí per fi m'hi puc posar i imprimir el formulari. Ja semblo jo estudiant per finals, tant perdre el temps. Ara només falta entrar a l'ordinador, espero que avui funcioni la impresora que ja ens ho coneixem, que si Linux, que si Windows... No entenc perquè no hi posen el Windows<sup>xd</sup>, allò si que era un bon sistema operatiu.<p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.79*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.sistemaOperatiu)
        self.nextButton.show()

        self.checkButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
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

        self.error.setGeometry(0.38*w, 0.53*h, 0.4*w, 0.1*h)
        self.error.setStyleSheet("color: red;")
        self.error.hide()

        self.boto1.hide()
        self.boto2.hide()

    def sistemaOperatiu(self):
        pixmap = QPixmap(resource_path("./images/cfis/SO.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - Per fi, cinquè ordinador que obro, finalment algun funciona. Ara ve el gran dilema: "To Linux or not to Linux, this is the quesion". I ja són les 8:53, no tinc temps per equivocar-me de sistema operatiu, ves a saber si algun altre ordenador funcionarà. Haig de prendre una decisió, i l'haig de prendre ràpid. <p>''')
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

        self.boto1.move(0.4*w, 0.87*h)
        self.boto1.clicked.connect(self.linux)

        self.boto2.move(0.54*w, 0.87*h)
        self.boto2.clicked.connect(self.windows)
        
        self.boto1.show()
        self.boto2.show()

        self.nextButton.hide()
        self.icon.hide()

    def linux(self):
        linuxPixmap = QPixmap(resource_path("./images/icons/ubuntu.png")).scaled(70,70)
        self.icon.setPixmap(linuxPixmap)
        self.inicio()

    def windows(self):
        windowsPixmap = QPixmap(resource_path("./images/icons/windows.png")).scaled(70,70)
        self.icon.setPixmap(windowsPixmap)
        self.inicio()

    def inicio(self):
        pixmap = QPixmap(resource_path("./images/cfis/inicio.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - Almenys per ara funciona... Merda, usuari i contrasenya, no me'n recordo. Crec que tocarà obrir el bloc de notes amb els usuaris i contrassenyes dels meus "amics" CFIS, tants mesos de carrera fent-lis la pilota han valgut la pena. Sort que en Covit m'ha dit que vigilés amb les tecles, que sinó això seria pitjor que el primer cop que vaig escriure el <i>Hello World</i>.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.hide()
        self.show()
        self.boto1.hide()
        self.boto2.hide()
        self.tigre.hide()
        self.user.setText("Usuari CFIS")
        self.password.setText("Contrasenya")

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
        self.juanjo.hide()

        pixmap = QPixmap(resource_path("./images/cfis/tigre.png")).scaled(150,150)
        self.tigre.setPixmap(pixmap)
        self.tigre.move(0.42*w, 0.14*h)
        self.tigre.show()

        self.user.setText("ivet.acosta@estudiant.uoc.edu")
        self.user.adjustSize()
        self.password.setText("satisfye")
        self.password.adjustSize()

        self.textField.setText('''<p> - Merda, m'estàs dient que no funciona la r? Només em faltava això. Haurien de portar algun Mates-Info que arreglés aquests ordinadors, perquè de veritat que això és intolerable. No sé perquè però, tinc la sensació de que encara que hagúes funcionat la r no m'hauria acceptat aquesta contrasenya. Anem a provar amb la d'algú altre...</p>''')
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
        self.tigre.hide()
        self.motorista.hide()

        pixmap = QPixmap(resource_path("./images/cfis/juanjo.png")).scaled(150,150)
        self.juanjo.setPixmap(pixmap)
        self.juanjo.move(0.42*w, 0.14*h)
        self.juanjo.show()

        self.user.setText("iñaki.gaido@estudiant.1ESO.edu")
        self.user.adjustSize()
        self.password.setText("juanjo")
        self.password.adjustSize()

        self.textField.setText('''<p> - És veritat, "rué" també porta r. Llàstima, amb lo bé que l'imita. Se'm comencen a acabar les possibilitats, siusplau, que n'hi hagi alguna que no porti r.</p>''')
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
        self.juanjo.hide()

        pixmap = QPixmap(resource_path("./images/cfis/motorista.png")).scaled(150,150)
        self.motorista.setPixmap(pixmap)
        self.motorista.move(0.42*w, 0.14*h)
        self.motorista.show()

        pixmap = QPixmap(resource_path("./images/cfis/inicio.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.user.setText("mac.heault@estudiant.uvic.edu")
        self.user.adjustSize()
        self.password.setText("ecoolt")
        self.password.adjustSize()

        self.textField.setText('''<p> - Un altre cop!? No hi ha ningú en tot el CFIS amb una contrasenya sense r!? Ostres! Ja ho tinc! Em sembla que la de l'Andreu té només Xifres, per algún motiu... El problema és que no la tinc apuntada al bloc de notes, però l'Andreu em va dir alguns trucs molt senzills per recordar-la... </p>''')
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
        self.motorista.hide()

        pixmap = QPixmap(resource_path("./images/cfis/monedes.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - El primer truc és la partida clandestina de cara-o-creu que va tenir lloc el 14 de març de l'any passat al lavabo CFIS. En aquell llegendari esdeveniment es van enfrentar els tres campions nacionals de cara-o-creu: Andreu Huguet, la Casanellas i El Barrero, d'on va sortir victoriosa Marta Casanellas, coneguda com Àlgebra amb diapositives. Tres eminències que han deixat una herència de jugades inversemblants i màgiques com no s'ha vist mai. No conec tots els detalls de la partida, però per sort recordo algunes jugades i propietats, vaig a apuntar-les a un paper.</p>''')
        # self.textField.setText('''<p> - Per algun motiu sempre que li pregunto per la contrasenya a l'Andreu, em recorda aquella partida de monedes que va jugar amb en Barrero i la Casanellas. Però no recordo tot el que va passar, només algunes propietats interessants. Les hauré d'anotar en un fullaviam si ho puc reconstriuir. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

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
        pixmap = QPixmap(resource_path("./images/cfis/bingo.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - El segon truc per recordar la contrasenya de l'Andreu és la partida de bingo de l'última festa de Nadal. Quina partida, quina muntanya russa d'emocions, encara no me n'he recuperat. La victòria de l'Andreu on va treure l'última meitat del cartró tot seguit és tema de debat al Claustre de la UPC, l'anomenen el cartró del 5.0. I no només va guanyar el bingo, sinó que també va cantar línia el primer, de 5 paraules. Sort que tinc fotos dels cartrons de l'Andreu, del Barja, del Narciso i del Jaume Franch. El problema és que no me'n recordo de qui era cada cadascun. </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.andreu1)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.andreu3)
        self.nextButton.show()

    def andreu3(self):
        self.fotoAndreu.hide()

        pixmap = QPixmap(resource_path("./images/cfis/tetris.png")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - I finalment, la partida de tetris. Sempre comenta que el millor que pots fer quan surts a Apolo és posar-te a jugar al tetris al ritme de la música. Òbviament, els resultats són desastrosos, però qui recriminarà una mala partida de tetris quan l'has fet al mig d'Apolo i després de beure molta aigua. Ningú, però ell sempre diu que hi va haver una partida especial, ningú sap perquè encara. Si no recordo malament, la va passar per Piki-Piki, anem a veure-la...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

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
        pixmap = QPixmap(resource_path("./images/cfis/inicio.jpg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        pixmap = QPixmap(resource_path("./images/cfis/andreu.png")).scaled(150,150)
        self.fotoAndreu.setPixmap(pixmap)
        self.fotoAndreu.move(0.42*w, 0.14*h)
        self.fotoAndreu.show()

        self.user.show()
        self.checkButton.show()
        self.icon.show()
        self.inputPassword.show()

        self.textField.setText('''<p> - Doncs esclar! Si casibé és més senzill recordar aquests tres trucs que no pas la contrasenya. S'hauria d'estar cec per no veure-la! No entenc com la falla tantes vegades, suposo que el tema machine-learning i Dades l'està afectant una miqueta.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.user.setText("delegat.huguet@cfis.com")
        self.user.adjustSize()

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
        elif not is_numeric(p):
            self.error.setText("La contrasenya només ha de contenir xifres")
            self.error.show()
        else:
            p = p.replace('0', '*')
            p = p.replace('1', '0')
            p = p.replace('2', '1')
            p = p.replace('3', '2')
            p = p.replace('4', '3')
            p = p.replace('5', '4')
            p = p.replace('6', '5')
            p = p.replace('7', '6')
            p = p.replace('8', '7')
            p = p.replace('9', '8')
            p = p.replace('*', '9')
            self.error.setText("La contrasenya " + p + " és incorrecta")
            self.error.show()

    def solved(self):
        self.fotoAndreu.hide()

        pixmap = QPixmap(resource_path("./images/cfis/cfisFormulari.jpeg")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textField.setText('''<p> - Per fi el tinc! Espero que em serveixi per aprovar l'examen. Deuria revisar a veure que diu, però no tinc temps. No passa res, el Batet mai es deixa res, i aquest cop he portat la lupa de casa, així que no crec que hi hagi cap problema. Ostres, són les 08:59! Vull dir, les 08:59. Igualment, m'haig d'afanyar o no podré agafar lloc a primera fila!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

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

        self.previousButton.hide()

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.examen)
        self.nextButton.show()


    def examen(self):
        self.examen1 = Examen1()
        self.close()

def is_number(c):
    numeric = False
    if c == "0": numeric = True
    if c == "1": numeric = True
    if c == "2": numeric = True
    if c == "3": numeric = True
    if c == "4": numeric = True
    if c == "5": numeric = True
    if c == "6": numeric = True
    if c == "7": numeric = True
    if c == "8": numeric = True
    if c == "9": numeric = True
    return numeric

def is_numeric(s):
    numeric = True
    if not is_number(s[0]): numeric = False
    if not is_number(s[1]): numeric = False
    if not is_number(s[2]): numeric = False
    if not is_number(s[3]): numeric = False
    if not is_number(s[4]): numeric = False
    if not is_number(s[5]): numeric = False
    return numeric

