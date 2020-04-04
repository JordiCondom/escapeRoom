from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Primera prova PyQt5"
        #dimensionat
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()#crida la funció crear finestra


    def InitWindow(self):
        self.setWindowTitle(self.title)#inicialitzem la finestra amb el seu titol
        self.setGeometry(self.left, self.top, self.width, self.height)#seleccionem la geometria de la finestra
        vbox = QVBoxLayout() #alineació dels objectes 
        labelImage = QLabel(self)
        pixmap = QPixmap("protofy.png")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)

        self.button = QPushButton('Botó',self)
        self.button.setFont(QtGui.QFont("Sanserif",15))
        self.button.setToolTip('Aquest es un botó creat')
        self.button.move(500,70)
        self.button.clicked.connect(self.openDialog)

        self.show()

    def openDialog(self):
        self.SW = SecondWindow()
        self.SW.show()
    #    alert = QMessageBox()
    #    alert.setText("He estat clicat")
    #    alert.exec_()
        self.close()

    

class SecondWindow(QDialog):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.title = "Segona Finestra"
        #dimensionat
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.SecondWindow()#crida la funció crear finestra
    
    def SecondWindow(self):
        self.setWindowTitle(self.title)#inicialitzem la finestra amb el seu titol
        self.setGeometry(self.left, self.top, self.width, self.height)#seleccionem la geometria de la finestra
        vbox = QVBoxLayout() #alineació dels objectes 
        lbl = QLabel('Hola Toni', self)
        lbl.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        vbox.addWidget(lbl)

        self.setLayout(vbox)
        self.button = QPushButton('Home',self)
        self.button.setFont(QtGui.QFont("Sanserif",15))
        self.button.setToolTip('Aquest es un botó creat')
        self.button.clicked.connect(self.returnHome)

        self.show()

    def returnHome(self):
            self.FW = MainWindow()
            self.FW.show()
            self.close()


App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())