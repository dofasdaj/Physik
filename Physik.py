class Engine():
    def __init__(self):
        pass
    def check_physics(self,objects):            # objects: Liste aller Objekte

        """

        check_physics soll Alle physikaltischen Abfragen aufrufen. Bspw.: Gravitationsberechnung

        Anwendung in der "main_loop" zum update der ganzen Physik_Engine

        Idee: Liste an Funktionen welche abgerufen werden sollen?

        """

        self.check_gravitation(objects)
    def check_gravitation(self,objects):
        for obj1 in objects:
            for obj2 in objects:
                if obj1 != obj2:
                    force = obj1.gravitation(obj2)

                    obj1.velocity = force[1]
                    obj1.direction = force[0]