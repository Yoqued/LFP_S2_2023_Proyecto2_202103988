from Abstract.abstract import Expression

class Min(Expression):
        def __init__(self, elemento, fila, columna):
            self.elemento = elemento
            super().__init__(fila, columna)

        def operar(self, arbol):
            return self.elemento

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()