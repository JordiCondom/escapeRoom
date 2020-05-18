import sys
import time
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from windowsFolder.finalFinal import FinalFinal

w = 900
h = 600


path = str(os.getcwd()) + "/images/videos/AGN.mp4"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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
        # self.video = VideoPlayer(self)
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

        self.textField.setText('''<p> - I la resposta és... 432! Doncs crec que ja ho tindríem, primer exercici... segon exercici... i tercer! Tots acabats i en fulls separats, crec que va sent hora d'entregar aquest examen d'aquesta assignatura de merda, per fi me'n puc desfer, per fi podré no gastar l'hora i mitja de dilluns i divendres que els meus solidaris companys feien servir per restregar-me lo bé que s'ho passaven fent birres al bar. I tot això? Per a què? Per a que acabin traient la mateixa nota que jo, o millor? N'estic fart. <b> ( Silenci ) </b> Hola Morsè, et vinc a entregar el final de la millor assignatura que he fet en la meva vida, gràcies per tot.</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.76*h)
        self.textField.show()

        self.inputPassword.setGeometry(0.2*w, 0.83*h, 0.2*w, 0.04*h)
        self.inputPassword.setMaxLength(20)
        self.inputPassword.setFrame(False)
        self.inputPassword.hide()

        self.checkButton.move(0.45*w, 0.83*h)
        self.checkButton.clicked.connect(self.checkAnswerSecondExercise)
        self.checkButton.hide()

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

        # self.video.resize(w, h)
        # self.video.hide()

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

        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.videoFinal)
    
    def videoFinal(self):
        self.nextButton.hide()
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoWidget = QVideoWidget(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))

        self.videoWidget.show()
        self.videoWidget.resize(w, h)

        self.textField.hide()
        self.textBubble.hide()
        self.backgroundImage.hide()
        self.caraMerce.hide()

        self.nextNewButton = QPushButton(self)
        self.nextNewButton.setStyleSheet("QPushButton{background-color: white;}")
        # self.nextNewButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextNewButton.move(0.85*w,0.83*h)
        self.nextNewButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextNewButton.show()

        self.mediaPlayer.play()

        # self.video.show()

        try:
            self.nextNewButton.clicked.disconnect()
        except:
            pass

        self.nextNewButton.clicked.connect(self.finalAnswer)

    def finalAnswer(self):
        self.nextNewButton.hide()
        self.videoWidget.hide()
        self.textField.setText('''<p> - Finalment, de quina assignatura ha sigut l'examen que has fet avui? </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.inputPassword.show()
        self.checkButton.show()

        self.textField.show()
        self.textBubble.show()

    def checkAnswerSecondExercise(self):
        self.finalFinal = FinalFinal()
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
            
            self.mediaPlayer.pause()
        else:
            
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.close()
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        
        self.positionSlider.setRange(0, duration)
        

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
        print(self.mediaPlayer.errorString())