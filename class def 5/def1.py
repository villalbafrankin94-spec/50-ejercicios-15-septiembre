class Contador:
    def __init__(self, n):
        self.n = n

    def contar(self):
        for i in range(1, self.n + 1):
            print(i)

contador = Contador(5)
contador.contar()