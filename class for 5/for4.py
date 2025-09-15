class Diccionario:
    def __init__(self):
        self.definiciones = {}

    def agregar(self, palabra, definicion):
        self.definiciones[palabra] = definicion

    def mostrar_todo(self):
        for palabra, definicion in self.definiciones.items():
            print(f"{palabra}: {definicion}")


dicc = Diccionario()
dicc.agregar("Python", "Lenguaje de programación interpretado.")
dicc.agregar("Clase", "Estructura que define objetos en programación.")
dicc.agregar("Diccionario", "Estructura que almacena pares clave-valor.")

dicc.mostrar_todo()
