from Abstract.abstract import Expression

class ContarSi(Expression):
        def __init__(self, elemento, valor, fila, columna):
            self.elemento = elemento
            self.valor = valor
            super().__init__(fila, columna)

        def operar(self, arbol):
            return self.elemento, self.valor

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()