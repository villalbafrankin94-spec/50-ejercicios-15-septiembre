class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto):
        self.inventario[producto.nombre] = producto

    def mostrar_inventario(self):
        for nombre, prod in self.inventario.items():
            print(f"{nombre}: ${prod.precio} x {prod.cantidad} unidades")


tienda = Tienda()
tienda.agregar_producto(Producto("Pan", 1500, 20))
tienda.agregar_producto(Producto("Leche", 3000, 10))
tienda.mostrar_inventario()
