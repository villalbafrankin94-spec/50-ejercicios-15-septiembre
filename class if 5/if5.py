class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")
        else:
            print("Fondos insuficientes")


c = Cajero(50000)
c.retirar(60000)
