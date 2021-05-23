from PyQt5.QtCore import Qt, QRect
import mathe
import math

class Objekt():
    def __init__(self, form):
        # self.velocity = 0
        self.mass = 500
        self.radius = round(self.mass/20)
        self.position = (30, 30)
        if form == "Rechteck":
            self.velocity = (0, 0)
            self.rect = QRect(self.position[0], self.position[1], self.radius, self.radius)
        self.vec_x = 30
        self.vec_y = 30

        self.force = 0
        self.gforce = (0,0)

    def gravitation(self, obj, gkonst):
        vector = mathe.normalize((obj.vec_x - self.vec_x, obj.vec_y - self.vec_y))
        try:
            gforce = vector*abs(gkonst*(self.mass*obj.mass)/math.sqrt((self.vec_x-obj.vec_x)**2+(self.vec_y-obj.vec_y)**2))
        except:
            gforce = (0,0)

        vector = (vector[0]*gforce,vector[1]*gforce)
        # print(mathe.normalize(vector),",",self)
        # print(self, "  ", "x:", mathe.normalize(vector)[0], "y: ", mathe.normalize(vector)[1])
        return (vector, gforce)
    def check_size(self):
        self.rect=QRect(self.rect.getCoords()[0],self.rect.getCoords()[1],self.radius,self.radius)
    def check_forces(self):
        self.force = self.gforce        # addition aller wirkenden kräfte (als vector!)

    def check_vel(self):
        # print(self.force, " check_vel")
        self.velocity = (self.velocity[0]+self.force[0]/self.mass, self.velocity[1]+self.force[1]/self.mass)   # v = a*t   a = F/m


    def changepos(self):
        current_coords = self.position # !gibt nur INTs aus. Unterscheide zwischen Pixel und Koordinaten!
        # print(current_coords[0])
        self.vec_x = current_coords[0] + self.velocity[0]
        self.vec_y = current_coords[1] + self.velocity[1]
        self.position = (self.vec_x, self.vec_y)
        # print(self, "  ", "x:", self.vec_x, "y: ", self.vec_y, "vec_x:", self.direction[0], "vec_y:", self.direction[1], "vel", self.velocity, "cur: ", current_coords)

    def draw(self):
        try:
            # print(round(self.vec_x, 0))
            self.rect.moveTo(round((self.vec_x)), round(float(self.vec_y)))
        except:
            pass

    def update(self):
        self.check_forces()
        self.check_vel()
        self.changepos()
        self.draw()
        self.check_size()
