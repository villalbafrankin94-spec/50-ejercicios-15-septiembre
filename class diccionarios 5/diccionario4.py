class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = {}

    def agregar_item(self, descripcion, precio):
        self.items[descripcion] = precio

    def total(self):
        return sum(self.items.values())


factura = Factura("Empresa XYZ")
factura.agregar_item("Servicio de consultoría", 500000)
factura.agregar_item("Hosting anual", 120000)
print(f"Total a pagar por {factura.cliente}: ${factura.total():,.0f}")
