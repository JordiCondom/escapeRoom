import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from mainWindow import MainWindow
from windowsFolder.entrada import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #mainWindow = MainWindow()
    #mainWindow.show()

    entrada = Entrada()

    sys.exit(app.exec_())