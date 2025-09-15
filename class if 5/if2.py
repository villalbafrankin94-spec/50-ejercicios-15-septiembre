class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def puede_votar(self):
        if self.edad >= 18:
            print(f"{self.nombre} puede votar.")
        else:
            print(f"{self.nombre} no puede votar.")


p = Persona("Carlos", 16)
p.puede_votar()
