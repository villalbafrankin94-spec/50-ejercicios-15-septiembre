class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def exportar(self):
        with open("usuario.txt", "w") as archivo:
            archivo.write(f"Nombre: {self.nombre}\nCorreo: {self.correo}")


u = Usuario("Camila", "camila@email.com")
u.exportar()
