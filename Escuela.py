#Programa de una escuela donde los alumnos rinden examenes y los profesores los toman y les dan una nota

class Alumnos():
    def __init__(self, nombre):
        self.nombre_alumno = nombre
        self.notas = {'matematica' : 0, 'lengua' : 0, 'geografia' : 0}
        self.promedio = 0
        self.rendimiento = ''
    def dar_examen(self, rendimiento):
        if rendimiento == 'malo':
            self.rendimiento = 'malo'
        if rendimiento == 'bueno':
            self.rendimiento = 'bueno'
        if rendimiento  == 'muy bueno':
            self.rendimiento = 'muy bueno'
        if rendimiento == 'excelente':
            self.rendimiento = 'excelente'
        print('Tu rendimiento fue ', self.rendimiento)


class Profesores(Alumnos):
    def __init__(self, nombre, materia, Alumnos):
        self.nombre_profesor = nombre
        self.materia = materia
        Alumnos.__init__(self)

    def tomar_examen(self):
        if self.rendimiento == 'muy bueno':
            self.notas[self.materia] = self.notas[self.materia : 10]
        print('El alumno ' + self.nombre_alumno  +' se saco un ' + str(self.notas[self.materia]) + ' en ' + self.materia)

alumno_juan = Alumnos('juan')
alumno_juan.dar_examen('muy bueno')

prof_pedro = Profesores('Pedro', 'matematica', alumno_juan)
prof_pedro.tomar_examen()