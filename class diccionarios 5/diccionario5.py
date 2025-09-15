class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.historial = {}

    def agregar_visita(self, fecha, motivo):
        self.historial[fecha] = motivo

    def mostrar_historial(self):
        for fecha, motivo in self.historial.items():
            print(f"{fecha}: {motivo}")


firulais = Mascota("Firulais", "Perro")
firulais.agregar_visita("2025-09-01", "Vacuna anual")
firulais.agregar_visita("2025-09-10", "Chequeo general")
firulais.mostrar_historial()
