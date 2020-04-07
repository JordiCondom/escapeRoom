import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from windowsFolder.entrada import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    entrada = Entrada()

    sys.exit(app.exec_())