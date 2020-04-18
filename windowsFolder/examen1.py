import sys
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

        self.textField.setText('''-Examen de numèrica yuhuuuuu + Sisi, crec que aquest any ho hem acoseguit i hem posat un examen de 100% numèrica. ''')
        self.textField.setAlignment(Qt.AlignJustify)
        self.textField.setWordWrap(True)
        self.textField.resize(600, 200)
        self.textField.move(0.167*w, 0.78*h)

        self.nextButton.move(0.85*w,0.83*h)
        self.nextButton.setIcon(QIcon('./images/icons/next.png'))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        try:
            self.nextButton.clicked.disconnect()
        except:
            pass
        self.nextButton.clicked.connect(self.criba)

        self.checkButton.move(0.8*w, 0.86*h)
        self.checkButton.clicked.connect(self.checkAnswer)
        self.checkButton.hide()

        self.noteInput.move(0.45*w, 0.75*h)
        self.noteInput.setParent(self)
        self.noteInput.hide()

    def criba(self):
        pixmap = QPixmap("./images/examen1/partitura.png").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.textBubble.hide()
        self.textField.hide()
        self.nextButton.hide()

        self.noteInput.show()
        self.checkButton.show()

    def checkAnswer(self):
        n1 = self.noteInput.note1.notes.currentIndex()
        n2 = self.noteInput.note2.notes.currentIndex()
        n3 = self.noteInput.note3.notes.currentIndex()
        n4 = self.noteInput.note4.notes.currentIndex()
        if n1 == 0 and n2 == 1 and n3 == 3 and n4 == 8:
            self.solved()

    def solved(self):
        pixmap = QPixmap("./images/examen1/padro.JPG").scaled(w,h)
        self.backgroundImage.setPixmap(pixmap)

        self.hide()
        self.show()

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


