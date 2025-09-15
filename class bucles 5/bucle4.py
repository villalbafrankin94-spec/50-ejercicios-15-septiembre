class Vehiculo:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo

class Garaje:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def filtrar_por_tipo(self, tipo):
        filtrados = []
        for v in self.vehiculos:
            if v.tipo == tipo:
                filtrados.append(v)
        return filtrados

garaje = Garaje()
garaje.agregar_vehiculo(Vehiculo("Toyota", "auto"))
garaje.agregar_vehiculo(Vehiculo("Honda", "moto"))
garaje.agregar_vehiculo(Vehiculo("Ford", "auto"))

autos = garaje.filtrar_por_tipo("auto")
for auto in autos:
    print(auto.marca)