print (" ")
print (" Cristian David Salas De La O 3-W")
print (" ")
class Marino:
    def hablar(self):
        print("Hola soy un animal marino!")

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")

class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)

# Crear instancias y usar los métodos
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola soy una foca!")
