class ListaNombres:
    def __init__(self):
        self.nombres = []

    def agregar_nombre(self, nombre):
        self.nombres.append(nombre)

    def mostrar_nombres(self):
        for nombre in self.nombres:
            print(nombre)


lista = ListaNombres()
lista.agregar_nombre("Ana")
lista.agregar_nombre("Luis")
lista.agregar_nombre("Marta")
lista.mostrar_nombres()