class Contador:
    def __init__(self, limite):
        self.numero = 1
        self.limite = limite

    def mostrar(self):
        while self.numero <= self.limite:
            print(self.numero)
            self.numero += 1


c = Contador(5)
c.mostrar()
