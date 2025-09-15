class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def completar(self):
        self.completada = True

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, descripcion):
        nuevas_tareas = []
        for t in self.tareas:
            if t.descripcion != descripcion:
                nuevas_tareas.append(t)
        self.tareas = nuevas_tareas

    def mostrar_tareas(self):
        for t in self.tareas:
            estado = "✓" if t.completada else "✗"
            print(f"{estado} {t.descripcion}")

lista = ListaTareas()
lista.agregar_tarea(Tarea("Comprar leche"))
lista.agregar_tarea(Tarea("Estudiar Python"))
lista.mostrar_tareas()