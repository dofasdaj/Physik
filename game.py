from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

import Object
import Physik

class Game(QWidget):
    def __init__(self, UI):
        super().__init__()
        self.title = "Game"
        self.top = 150
        self.left = 150
        self.width = UI.windowWidth
        self.height = UI.windowHeight
        self.InitWindow()

        self.x = 40
        self.y = 40
        self.timerSetup()

        self.objects = []
        self.rectangle = Object.Objekt("Rechteck")
        self.rectangle2 = Object.Objekt("Rechteck")
        self.rectangle3 = Object.Objekt("Rechteck")
        self.rectangle2.position = (300,300)
        self.rectangle3.position = (100,300)
        self.rectangle3.mass = 5000
        self.rectangle2.velocity = 2
        self.objects.append(self.rectangle)
        self.objects.append(self.rectangle2)
        self.objects.append(self.rectangle3)

        self.physik_engine = Physik.Engine()    # Erzeugt die Physik_Engine auf

    def timerSetup(self):
        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.game)
        self.timer.start()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def game(self):
        for obj in self.objects:
            obj.update()
        self.update()
        self.physik_engine.check_physics(self.objects)          # ruft ein update der Physik_Engine auf

    """def changepos(self):
        self.x += 1
        self.y += 1
        self.update()"""

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        #painter.drawRect(self.rectangle.rect)
        #painter.drawEllipse(self.obj.pos[0], self.obj.pos[1], 100, 100)
        for obj in self.objects:
            painter.drawEllipse(obj.rect)
