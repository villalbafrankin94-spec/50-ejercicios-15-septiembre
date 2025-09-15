class Cancion:
    def __init__(self, titulo, letra):
        self.titulo = titulo
        self.letra = letra

    def guardar_letra(self):
        with open(f"{self.titulo}.txt", "w") as archivo:
            archivo.write(self.letra)


c = Cancion("MiCancion", "Esta es la letra de mi canción\nLínea dos\nLínea tres")
c.guardar_letra()
