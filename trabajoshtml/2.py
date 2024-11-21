print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Crear una instancia de Persona con datos ingresados por el usuario
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
p = Persona(nombre, edad)

# Incrementar la edad dos veces
p.cumpleaños()
p.cumpleaños()

# Imprimir los resultados
print(f"{p.nombre} cumple {p.edad} años")
