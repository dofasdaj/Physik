from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtCore import QTimer
#import numpy as np
import mathe
import Object
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.InitWindow()

        self.x = 40
        self.y = 40
        self.timerSetup()

        self.objects = []
        self.rectangle = Object.Objekt("Rechteck")
        self.rectangle2 = Object.Objekt("Rechteck")
        self.rectangle2.position = (300,300)
        self.objects.append(self.rectangle)
        self.objects.append(self.rectangle2)

    def timerSetup(self):
        self.timer = QTimer(self)
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.game)
        self.timer.start()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def check_gravitation(self):
        for obj1 in self.objects:
            for obj2 in self.objects:
                if obj1 != obj2:
                    force = obj1.gravitation(obj2)

                    obj1.velocity = force[1]
                    obj1.direction = force[0]

                    #print(self, "  ", "x:", mathe.normalize(vector)[0], "y: ", mathe.normalize(vector)[1])
                    #print(obj1.direction)
                    #print(obj1.velocity)

    def game(self):
        for obj in self.objects:
            obj.update()
        self.update()
        self.check_gravitation()

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
        painter.drawEllipse(self.rectangle.rect)
        painter.drawEllipse(self.rectangle2.rect)


def main():
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    App = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(App.exec())

if __name__ == '__main__':
    main()
