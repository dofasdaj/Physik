import mathe

class Engine():
    def __init__(self):
        self.gravitations_konst = 1
    def check_physics(self,objects):            # objects: Liste aller Objekte

        """

        check_physics soll Alle physikaltischen Abfragen aufrufen. Bspw.: Gravitationsberechnung

        Anwendung in der "main_loop" zum update der ganzen Physik_Engine

        Idee: Liste an Funktionen welche abgerufen werden sollen?

        """

        self.check_gravitation(objects)
    def check_gravitation(self,objects):
        for obj1 in objects:
            applied_forces = [] # Liste aller wirkenden Gravitationskräfte
            for obj2 in objects:
                if obj1 != obj2:
                    applied_forces.append(obj1.gravitation(obj2))   # jede Kraft wird in Liste "applied_forces" hinzugefügt

            gravitational_force = ((0,0),0)

            for force in applied_forces:
                gravitational_force = (mathe.normalize(mathe.add_vectors(gravitational_force[0],force[0])),mathe.add_vectors(gravitational_force[0],force[0])[0]/mathe.normalize(mathe.add_vectors(gravitational_force[0],force[0]))[0])
                # gibt ein Array = (vector, vectorstärke)
            obj1.velocity = gravitational_force[1]
            obj1.direction = gravitational_force[0]