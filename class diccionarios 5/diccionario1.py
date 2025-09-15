class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_calificacion(self, materia, nota):
        self.calificaciones[materia] = nota

    def promedio(self):
        return sum(self.calificaciones.values()) / len(self.calificaciones)


juan = Estudiante("Juan")
juan.agregar_calificacion("Matemáticas", 4.5)
juan.agregar_calificacion("Historia", 3.8)
print(f"Promedio de {juan.nombre}: {juan.promedio():.2f}")
