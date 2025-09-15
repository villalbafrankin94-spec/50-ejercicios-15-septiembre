class Factorial:
    def __init__(self, n):
        self.n = n

    def calcular(self):
        resultado = 1
        i = 1
        while i <= self.n:
            resultado *= i
            i += 1
        return resultado


fact = Factorial(5)
print("Factorial:", fact.calcular())