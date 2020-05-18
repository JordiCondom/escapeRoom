import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from windowsFolder.entrada import *
from windowsFolder.bar import *
from windowsFolder.pati import *
from windowsFolder.senyorGrane import *
from windowsFolder.cfis import *
from windowsFolder.examen1 import *
from windowsFolder.examen2 import * 
from windowsFolder.final import * 
from windowsFolder.finalFinal import * 


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #entrada = Entrada()
    #bar = Bar()
    #pati = Pati()
    #senyorGrane = SenyorGrane()
    #cfis = Cfis()
    #examen1 = Examen1()
    #examen2 = Examen2()
    #examen3 = Examen3()
    #final = Final()
    finalfinal = FinalFinal()

    sys.exit(app.exec_())