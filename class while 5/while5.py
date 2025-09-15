class Caminata:
    def __init__(self, pasos):
        self.pasos = pasos

    def avanzar(self):
        actual = 0
        while actual < self.pasos:
            print(f"Paso {actual + 1}")
            actual += 1


c = Caminata(4)
c.avanzar()
