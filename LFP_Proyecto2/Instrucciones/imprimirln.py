from Abstract.abstract import Expression

class Imprimirln(Expression):

        def __init__(self, texto, fila, columna):
            self.texto = texto
            super().__init__(fila, columna)

        def operar(self, arbol):
            return self.texto

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()