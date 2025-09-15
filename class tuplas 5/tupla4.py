class Partido:
    def __init__(self, datos):
        self.equipo_local, self.equipo_visitante, self.fecha = datos

    def resumen(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} el {self.fecha}"

juego = Partido(("Millonarios", "Santa Fe", "15/09/2025"))
print(juego.resumen())
