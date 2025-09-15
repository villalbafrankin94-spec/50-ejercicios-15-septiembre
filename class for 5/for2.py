class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

inventario = {
    "Arroz": Producto("Arroz", 2500, 10),
    "Aceite": Producto("Aceite", 8000, 5),
    "Huevos": Producto("Huevos", 500, 30)
}

for nombre, producto in inventario.items():
    print(f"{nombre}: ${producto.precio} x {producto.cantidad} unidades")
