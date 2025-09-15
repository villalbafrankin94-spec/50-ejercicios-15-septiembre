class Semaforo:
    def __init__(self, color):
        self.color = color

    def accion(self):
        if self.color == "rojo":
            print("Detente")
        elif self.color == "amarillo":
            print("Prepárate")
        elif self.color == "verde":
            print("Avanza")
        else:
            print("Color inválido")


s = Semaforo("verde")
s.accion()
