class Evaluacion:
    def __init__(self, nota):
        self.nota = nota

    def resultado(self):
        if self.nota >= 3.0:
            print("Aprobado")
        else:
            print("Reprobado")


e = Evaluacion(2.8)
e.resultado()
