class Lector:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer(self):
        with open(self.nombre_archivo, "r") as archivo:
            contenido = archivo.read()
        return contenido


l = Lector("nota.txt")
print(l.leer())
