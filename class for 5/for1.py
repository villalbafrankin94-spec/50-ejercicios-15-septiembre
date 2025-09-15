class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones  

    def promedio(self):
        return sum(self.calificaciones.values()) / len(self.calificaciones)


grupo = [
    Estudiante("Ana", {"Mate": 4.5, "Historia": 3.8}),
    Estudiante("Luis", {"Mate": 3.9, "Historia": 4.2}),
    Estudiante("Sofía", {"Mate": 5.0, "Historia": 4.7})
]

for estudiante in grupo:
    print(f"{estudiante.nombre} tiene un promedio de {estudiante.promedio():.2f}")
