class Multiplo:
    def __init__(self, base, cantidad):
        self.base = base
        self.cantidad = cantidad

    def generar(self):
        contador = 1
        while contador <= self.cantidad:
            print(self.base * contador)
            contador += 1


m = Multiplo(7, 5)
m.generar()
