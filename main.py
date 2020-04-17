import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from windowsFolder.entrada import *
from windowsFolder.bar import *
from windowsFolder.pati import *
from windowsFolder.senyorGrane import *
from windowsFolder.cfis import *
from windowsFolder.examen1 import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    entrada = Entrada()
    #bar = Bar()
    #pati = Pati()
    #senyorGrane = SenyorGrane()
    #cfis = Cfis()
    #examen1 = Examen1()

    sys.exit(app.exec_())