class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if p.nombre == nombre]

inv = Inventario()
inv.agregar_producto(Producto("Camisa", 20))
inv.agregar_producto(Producto("Pantalón", 30))
inv.agregar_producto(Producto("Camisa", 25))

camisas = inv.buscar_por_nombre("Camisa")
for c in camisas:
    print(f"{c.nombre} - ${c.precio}")