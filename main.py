from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtCore import QTimer
#import numpy as np
import mathe
import sys


class Objekt():
    def __init__(self, form):
        self.velocity = 0
        self.position = (30,30)
        if form == "Rechteck":
            self.direction = (1, 1)
            self.rect = QRect(self.position[0], self.position[1], 100, 100)
        self.vec_x = 30
        self.vec_y = 30

    def gravitation(self, obj):
        vector = (obj.vec_x-self.vec_x,obj.vec_y-self.vec_y)
        #print(mathe.normalize(vector),",",self)
        #print(self, "  ", "x:", mathe.normalize(vector)[0], "y: ", mathe.normalize(vector)[1])
        return (mathe.normalize(vector),1)


    def changepos(self):
        current_coords = self.position  # !gibt nur INTs aus. Unterscheide zwischen Pixel und Koordinaten!
        print(current_coords[0])
        self.vec_x = current_coords[0] + self.velocity*self.direction[0]
        self.vec_y = current_coords[1] + self.velocity*self.direction[1]
        self.position = (self.vec_x,self.vec_y)
        print(self, "  ", "x:", self.vec_x, "y: ", self.vec_y, "vec_x:", self.direction[0],"vec_y:", self.direction[1],"vel", self.velocity,"cur: ",current_coords)

    def draw(self):
        try:
            print(round(self.vec_x,0))
            self.rect.moveTo(round((self.vec_x)), round(float(self.vec_y)))
        except:
            pass


    def update(self):
        self.changepos()
        self.draw()

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
        self.rectangle = Objekt("Rechteck")
        self.rectangle2 = Objekt("Rechteck")
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
