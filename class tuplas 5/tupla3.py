class Caja:
    def __init__(self, dimensiones):
        self.largo, self.ancho, self.alto = dimensiones

    def volumen(self):
        return self.largo * self.ancho * self.alto


caja = Caja((2, 3, 4))
print(f"Volumen: {caja.volumen()} unidades cúbicas")
