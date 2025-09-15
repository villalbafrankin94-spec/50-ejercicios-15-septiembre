class Cancion:
    def __init__(self, atributos):
        self.titulo, self.artista, self.duracion = atributos

    def info(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} min)"

track = Cancion(("Bohemian Rhapsody", "Queen", 6))
print(track.info())
