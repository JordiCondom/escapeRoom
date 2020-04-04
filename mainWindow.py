import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windowsFolder.entrada import *

# Abraçades!

w = 1000
h = 600

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mainLayout = QStackedLayout()

        self.setWindowTitle("Escape Room")
        self.setFixedSize(w,h)

        entrada = Entrada()

        mainLayout.addWidget(entrada)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # self.window.showFullScreen()
        # self.window.showMaximized()