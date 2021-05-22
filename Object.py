from PyQt5.QtCore import Qt, QRect
import mathe

class Objekt():
    def __init__(self, form):
        self.velocity = 0
        self.position = (30, 30)
        if form == "Rechteck":
            self.direction = (1, 1)
            self.rect = QRect(self.position[0], self.position[1], 100, 100)
        self.vec_x = 30
        self.vec_y = 30

        self.force = 0

    def gravitation(self, obj):
        vector = (obj.vec_x - self.vec_x, obj.vec_y - self.vec_y)
        # print(mathe.normalize(vector),",",self)
        # print(self, "  ", "x:", mathe.normalize(vector)[0], "y: ", mathe.normalize(vector)[1])
        return (mathe.normalize(vector), 1)

    def changepos(self):
        current_coords = self.position  # !gibt nur INTs aus. Unterscheide zwischen Pixel und Koordinaten!
        print(current_coords[0])
        self.vec_x = current_coords[0] + self.velocity * self.direction[0]
        self.vec_y = current_coords[1] + self.velocity * self.direction[1]
        self.position = (self.vec_x, self.vec_y)
        print(self, "  ", "x:", self.vec_x, "y: ", self.vec_y, "vec_x:", self.direction[0], "vec_y:", self.direction[1],
              "vel", self.velocity, "cur: ", current_coords)

    def draw(self):
        try:
            print(round(self.vec_x, 0))
            self.rect.moveTo(round((self.vec_x)), round(float(self.vec_y)))
        except:
            pass

    def update(self):
        self.changepos()
        self.draw()