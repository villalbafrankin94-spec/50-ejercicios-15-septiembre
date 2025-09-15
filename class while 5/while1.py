class Temporizador:
    def __init__(self, tiempo):
        self.tiempo = tiempo

    def contar(self):
        while self.tiempo > 0:
            print(f"Tiempo restante: {self.tiempo}")
            self.tiempo -= 1


t = Temporizador(5)
t.contar()
