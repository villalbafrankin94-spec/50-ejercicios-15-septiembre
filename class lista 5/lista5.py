class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def ordenar_por_anio(self):
        self.libros.sort(key=lambda libro: libro.anio)

    def mostrar_libros(self):
        for libro in self.libros:
            print(f"{libro.titulo} ({libro.anio}) - {libro.autor}")

biblio = Biblioteca()
biblio.agregar_libro(Libro("1984", "George Orwell", 1949))
biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 1967))
biblio.agregar_libro(Libro("El principito", "Antoine de Saint-Exupéry", 1943))

biblio.ordenar_por_anio()
biblio.mostrar_libros()