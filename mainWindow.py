import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from windows import *

# Abraçades!

w = 1000
h = 600

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mainLayout = QStackedLayout()

        self.setWindowTitle("Escape Room")
        self.setFixedSize(w,h)

        mario = Mario()

        mainLayout.addWidget(mario)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # self.window.showFullScreen()
        # self.window.showMaximized()