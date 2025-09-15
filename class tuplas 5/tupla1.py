class Persona:
    def __init__(self, datos):
        self.nombre, self.edad, self.ciudad = datos

    def mostrar(self):
        return f"{self.nombre}, {self.edad} años, vive en {self.ciudad}"


p = Persona(("Laura", 28, "Bogotá"))
print(p.mostrar())
