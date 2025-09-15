class Repetidor:
    def __init__(self, mensaje, veces):
        self.mensaje = mensaje
        self.veces = veces

    def repetir(self):
        actual = 0
        while actual < self.veces:
            print(self.mensaje)
            actual += 1


r = Repetidor("¡Hola mundo!", 3)
r.repetir()
