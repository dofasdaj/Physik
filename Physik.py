import mathe

class Engine():
    def __init__(self):
        self.gravitations_konst = 0.0001
    def check_physics(self,game,objects):            # objects: Liste aller Objekte

        """

        check_physics soll Alle physikaltischen Abfragen aufrufen. Bspw.: Gravitationsberechnung

        Anwendung in der "main_loop" zum update der ganzen Physik_Engine

        Idee: Liste an Funktionen welche abgerufen werden sollen?

        """

        self.check_gravitation(objects)
        self.check_collision(game)
    def check_collision(self, game):
        for obj1 in game.objects:
            for obj2 in game.objects:
                if obj1 != obj2:
                    dis = 50
                    if (((obj1.position[0] - obj2.position[0]) < dis) and (obj1.position[0] - obj2.position[0]) > (-1*dis)) and (((obj1.position[1] - obj2.position[1]) < dis) and ((obj1.position[1] - obj2.position[1]) > -1*dis)):
                        print(-dis)
                        x = 0
                        for i in game.objects:
                            if game.objects[x] == obj2:
                                print("Litauen")
                                obj1.mass += obj2.mass
                                obj1.velocity = mathe.add_vectors(obj1.velocity,obj2.velocity)
                                game.objects.pop(x)
                            x+=1

    def impuls(self,obj1,obj2):
        force = mathe.add_vectors(obj1.force,obj2.force)
        return force

    def check_gravitation(self,objects):
        for obj1 in objects:
            applied_forces = [] # Liste aller wirkenden Gravitationskräfte
            for obj2 in objects:
                if obj1 != obj2:
                    applied_forces.append(obj1.gravitation(obj2,self.gravitations_konst))   # jede Kraft wird in Liste "applied_forces" hinzugefügt

            gravitational_force = (0, 0)

            for force in applied_forces:
                # print(gravitational_force)
                # print(force[0], "force")
                gravitational_force = mathe.add_vectors(gravitational_force, force[1])
                # mathe.add_vectors(gravitational_force[0],force[0]*)/mathe.normalize(mathe.add_vectors(gravitational_force[0],force[0]))[0]
                # gibt ein Array = (vector, vectorstärke)
            #gravitational_force = (gravitational_force[0],gravitational_force[0][0]/mathe.normalize(gravitational_force[0])[0])
            obj1.gforce = gravitational_force # gravitational_force[0][0]/mathe.normalize(gravitational_force[0])[0]