import sys
import time
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from windowsFolder.examen3 import Examen3
from windowsFolder.videoExamen2 import videoFinal

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

path = str(os.getcwd()) + "/test.mp4"
videoAcabat = False

class Examen2(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap(resource_path("./images/examen1/padro_cul.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon(resource_path('./images/icons/previous.png')))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap(resource_path("./images/icons/textBubble.png"))
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> - Primer exercici acabat, tot i que té pinta que això serà com el qüestionari de topologia, un cop respons una pregunta, no pots tirar endarrere. No passa res, ara m'haig de centrar en dues coses: el cul del Padró i el segon exercici. Tot i que si m'haig de sincerar, diré que l'últim exercici no m'ha semblat gaire de N*mèr**a, perdoneu, però algú ho havia de dir. Esperem que el següent s'adapti una mica més al que hem fet a classe. Mira! Aquí ve per fi en Lázaro!</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)
        self.textField.show()

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon(resource_path('./images/icons/next.png')))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
            self.textBubble.show()
            self.textField.show()
            self.nextButton.show()
        except:
            pass
        self.nextButton.clicked.connect(self.secondExerciseSecond)

        self.hide()
        self.show()

    def secondExerciseSecond(self):

        pixmap = QPixmap(resource_path("./images/examen2/lazaro.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

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
        pixmap = QPixmap(resource_path("./images/examen2/lazaro.JPG")).scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.show()

        self.textField.setText('''<p> <b> Lázaro:</b> de hecho, justo ahora venían de resaca de la fiesta de Rosalia y Bad Bunny en Sant Esteve Sesrovires. Pero mirad lo increíbles que son, que aún con resaca han aceptado mi solicitud. Y óbviamente os preguntaréis, ¿qué nos importa a nosotros lo que les haya pedido este senyor a estas celebridades en medio de un final de N*mèr**a? Pues os importa, y mucho, porque será la única cosa interesante que os pasará hoy, el mejor espectáculo de vuestras vidas. Chicos y chicas, Carles Padró; hoy tengo la gran suerte y el gran honor de poder presentaros al gran dúo.... (redoble de tambores)... Hugana War!  </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.76*h)

        
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.secondExerciseSecond)

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.videoScreen)
    
    def videoScreen(self):

        self.videoFinal = videoFinal()
        self.close()


class VideoPlayer(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Arial", 7))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.statusBar.showMessage("Ready")

    def play(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            print(1)
            self.mediaPlayer.pause()
        else:
            print(2)
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            print(3)
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            print(4)
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        print(5)
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        print(6)
        self.positionSlider.setRange(0, duration)
        

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
        print(self.mediaPlayer.errorString())