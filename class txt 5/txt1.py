class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def guardar(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(self.contenido)


n = Nota("Esta es una nota importante.")
n.guardar("nota.txt")
