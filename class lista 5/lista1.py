class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


estudiantes = [
    Estudiante("Ana", 20),
    Estudiante("Luis", 22),
    Estudiante("Marta", 19)
]

for e in estudiantes:
    print(e)