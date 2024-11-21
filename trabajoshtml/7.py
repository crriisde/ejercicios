print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}.")

# Crear una instancia y usar los métodos
persona = Estudiante("Harvard")
persona.carrera("Ingeniería mecatrónica")
persona.datos("Mike", 19)
