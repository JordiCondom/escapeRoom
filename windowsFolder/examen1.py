import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

w = 900
h = 600

class Examen1(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0,0,w,h)
        self.backgroundImage = QLabel(self)
        self.textBubble = QLabel(self)
        self.previousButton = QPushButton(self)
        self.nextButton = QPushButton(self)
        self.textField = QLabel(self)
        self.checkButton = QPushButton('Comprova', self)
        self.noteInput = NoteInput()
        self.notesQuery = QLabel(self)
        self.initWindow()

        self.show()

    def initWindow(self):
        pixmap = QPixmap("./images/examen1/padro.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.previousButton.move(0.12*w, 0.83*h)
        self.previousButton.setIcon(QIcon('./images/icons/previous.png'))
        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.hide()

        bubblePM = QPixmap("./images/icons/textBubble.png")
        self.textBubble.setPixmap(bubblePM)
        self.textBubble.move(0.1*w, 0.75*h)

        self.textField.setText('''<p> - Ja hi som. Al final no he tingut temps de repassar res de res, se me n'ha anat tot el matí en orris. Almenys he pogut imprimir el formulari, serà el meu salvavides en aquest examen. <br>
        <b> - Alumne random de N*mèr**a: </b> Què és aquest full que portes? És un formulari? <br>
        - Sí, me l'acabo d'imprimir al CFIS. Ara mateix és l'única esperança que tinc per aquest examen. <br> 
        <b> - Alumne random de N*mèr**a: </b> Vaja... No sé com dir-te això però... This is N*mèr**a! No es pot portar formulari...</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.77*h)
        self.textField.show()

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
        self.nextButton.clicked.connect(self.firstExerciseFirst)

        self.checkButton.move(0.8*w, 0.86*h)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.noteInput.move(0.45*w, 0.75*h)
        self.noteInput.setParent(self)
        self.noteInput.hide()

        self.notesQuery.setPixmap(QPixmap("./images/examen1/notesQuery.png").scaled(350, 100))
        self.notesQuery.move(0.07*w, 0.8*h)
        self.notesQuery.hide()

        self.hide()
        self.show()

    def firstExerciseFirst(self):
        pixmap = QPixmap("./images/examen1/dog.jpg").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)
        self.textBubble.hide()
        self.textField.hide()

        self.previousButton.show()
        try:
            self.previousButton.clicked.disconnect()
        except:
            pass
        self.previousButton.setStyleSheet("QPushButton{}")
        self.previousButton.clicked.connect(self.initWindow)

        self.nextButton.setStyleSheet("QPushButton{}")
        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.firstExerciseSecond)

    def firstExerciseSecond(self):
        pixmap = QPixmap("./images/examen1/jordis.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

        self.textField.setText('''<p> - Em falta això :'( </p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()
        self.previousButton.move(0.12*w, 0.83*h)

        self.noteInput.hide()
        self.checkButton.hide()
        self.notesQuery.hide()

        self.previousButton.setStyleSheet("QPushButton{background: transparent;}")
        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.firstExerciseFirst)

        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.disconnect()
        self.nextButton.clicked.connect(self.firstExerciseCriba)

    def firstExerciseCriba(self):
        pixmap = QPixmap("./images/examen1/partitura.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()

        self.noteInput.show()
        self.checkButton.show()
        self.notesQuery.show()
        self.previousButton.show()
        self.previousButton.move(0.035*w, 0.87*h)

        self.previousButton.clicked.disconnect()
        self.previousButton.clicked.connect(self.firstExerciseSecond)

    def secondExerciseFirst(self):
        pixmap = QPixmap("./images/examen1/padro.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

        self.textBubble.show()
        self.textField.show()
        self.nextButton.show()

        self.previousButton.hide()
        self.noteInput.hide()
        self.checkButton.hide()
        self.notesQuery.hide()

        self.textField.setText('''<p> - Segon exercici</p>''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.8*h)
        

    def checkAnswer(self):
        n1 = self.noteInput.note1.notes.currentIndex()
        n2 = self.noteInput.note2.notes.currentIndex()
        n3 = self.noteInput.note3.notes.currentIndex()
        n4 = self.noteInput.note4.notes.currentIndex()
        if n1 == 0 and n2 == 1 and n3 == 3 and n4 == 8:
            self.secondExerciseFirst()

class NoteInput(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.note1 = NoteSelector()
        self.note2 = NoteSelector()
        self.note3 = NoteSelector()
        self.note4 = NoteSelector()

        layout.addWidget(self.note1)
        layout.addWidget(self.note2)
        layout.addWidget(self.note3)
        layout.addWidget(self.note4)

        layout.setSpacing(0)

        self.setLayout(layout)


class NoteSelector(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        up = QPushButton()
        up.setIcon(QIcon('./images/icons/up.png'))
        up.setStyleSheet("QPushButton{background: transparent;}")
        up.clicked.connect(self.upgrade)

        down = QPushButton()
        down.setIcon(QIcon('./images/icons/down.png'))
        down.setStyleSheet("QPushButton{background: transparent;}")
        down.clicked.connect(self.downgrade)

        self.notes = QStackedWidget()

        for i in range(1,14):
            note = QLabel()
            note.setPixmap(QPixmap("./images/notes/" + str(i) + ".png"))
            self.notes.addWidget(note)

        layout.addWidget(up)
        layout.addWidget(self.notes)
        layout.addWidget(down)

        layout.setSpacing(0)

        self.setLayout(layout)

    def upgrade(self):
        n = self.notes.count()
        index = self.notes.currentIndex()
        newIndex = index + 1
        if newIndex == n: newIndex = 0

        self.notes.setCurrentIndex(newIndex)

    def downgrade(self):
        n = self.notes.count()
        index = self.notes.currentIndex()
        newIndex = index - 1
        if newIndex == -1: newIndex = n-1

        self.notes.setCurrentIndex(newIndex)


