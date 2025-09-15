class Pelicula:
    def __init__(self, info):
        self.titulo, self.director, self.año = info

    def ficha(self):
        return f"'{self.titulo}' dirigida por {self.director} ({self.año})"

film = Pelicula(("El secreto de sus ojos", "Juan José Campanella", 2009))
print(film.ficha())
