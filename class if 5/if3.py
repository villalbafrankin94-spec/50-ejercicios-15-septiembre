class Termostato:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def estado(self):
        if self.temperatura < 18:
            print("Encender calefacción")
        elif self.temperatura > 26:
            print("Encender aire acondicionado")
        else:
            print("Temperatura ideal")

t = Termostato(30)
t.estado()
