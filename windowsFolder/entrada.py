from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.bar import Bar

w = 1000
h = 600

class Entrada(QWidget):
    def __init__(self):
        super(Entrada, self).__init__()

        self.setGeometry(0,0,w,h)
        self.initWindow()

    def initWindow(self):
        textLabel = QLabel(self)
        textLabel.setText("Entrada")
        textLabel.setWordWrap(True)
        textLabel.move(0.4*w, h/3)
        textLabel.setAlignment(Qt.AlignCenter)

        backgroundImage = QLabel(self)
        pixmap = QPixmap("./images/entradafme.jpg").scaled(w,h)
        backgroundImage.setPixmap(pixmap)

        button = QPushButton('continua',self)
        button.move(w/3,h/3)
        button.clicked.connect(self.checkAnswer)

        self.passwordField = QTextEdit(self)
        self.passwordField.setPlaceholderText("Introduce la respuesta")
        self.passwordField.setGeometry(0,0.9*h,w,0.1*h)

        self.show()

    def checkAnswer(self):
        password = "guapo"
        print(password)
        answer = self.passwordField.toPlainText()
        if answer == password:
            self.enigmaSolved()

    def enigmaSolved(self):
        bar = Bar()
        #bar.show()
        alert = QMessageBox()
        alert.setText("abrasadas")
        alert.exec_()
        self.close()