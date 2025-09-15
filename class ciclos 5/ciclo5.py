import time

class ContadorRegresivo:
    def __init__(self, inicio):
        self.inicio = inicio

    def iniciar(self):
        for i in range(self.inicio, 0, -1):
            print(i)
            time.sleep(1)
        print("¡Tiempo terminado!")


contador = ContadorRegresivo(5)
contador.iniciar()