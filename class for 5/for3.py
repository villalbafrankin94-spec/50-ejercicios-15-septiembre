class Receta:
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes  

    def mostrar(self):
        print(f"Receta: {self.nombre}")
        for ingrediente, cantidad in self.ingredientes.items():
            print(f" - {ingrediente}: {cantidad}")

torta = Receta("Torta de chocolate", {
    "Harina": "2 tazas",
    "Cacao": "1 taza",
    "Huevos": "3 unidades",
    "Azúcar": "1 taza"
})

torta.mostrar()
