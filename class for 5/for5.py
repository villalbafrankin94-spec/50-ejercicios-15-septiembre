class Jugador:
    def __init__(self, nombre, stats):
        self.nombre = nombre
        self.stats = stats  

    def mostrar_stats(self):
        print(f"Jugador: {self.nombre}")
        for stat, valor in self.stats.items():
            print(f"  {stat}: {valor}")

jugadores = [
    Jugador("Leo", {"Fuerza": 80, "Velocidad": 90, "Resistencia": 85}),
    Jugador("Mia", {"Fuerza": 70, "Velocidad": 95, "Resistencia": 88})
]

for jugador in jugadores:
    jugador.mostrar_stats()
