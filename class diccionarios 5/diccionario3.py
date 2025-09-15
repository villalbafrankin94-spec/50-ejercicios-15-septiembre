class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.titulo] = libro.autor

    def buscar_por_autor(self, autor):
        return [titulo for titulo, a in self.catalogo.items() if a == autor]


biblio = Biblioteca()
biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))
biblio.agregar_libro(Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez"))
print(biblio.buscar_por_autor("Gabriel García Márquez"))
