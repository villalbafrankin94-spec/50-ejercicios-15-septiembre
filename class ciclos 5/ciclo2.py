class Sumador:
    def __init__(self):
        self.suma = 0

    def sumar(self):
        while True:
            num = int(input("Ingrese un número (0 para terminar): "))
            if num == 0:
                break
            self.suma += num
        print("Suma total:", self.suma)

# Uso
sumador = Sumador()
sumador.sumar()