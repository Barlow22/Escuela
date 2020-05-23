#Programa de una escuela donde los alumnos rinden examenes y los profesores los toman y les dan una nota

class Alumnos():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nota_mate = 0
        self.nota_lengua = 0
        self.nota_geo = 0
        self.promedio = 0
        
    def dar_examen(self, desempeño):
        return desempeño


class Profesores(Alumnos):
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        Alumnos.__init__(self, nombre)

    def tomar_examen(self, desempeño):
        if desempeño >= 0 and desempeño <20:
            self.nota




