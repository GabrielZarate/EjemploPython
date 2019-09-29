import math
class Etiqueta:

    def __init__(self):
        self.Nombre   =     "NULL"
        self.Valor    =     "NULL"
        self.Aparciones  =      0
        self.Numero  =          0

    def toStrFile(self):
        return (self.Nombre + " -> " + self.Valor + "\n")

    def toStrConsole(self):
        return (self.Nombre + " -> " + self.Valor + "\t" + "Numero de Aparicion: " + str(self.Numero) + "\t" + "Numero Total de aparciones: "  \
        + str(self.Aparciones) + "\n")

    def asignarValores(self, PNombre, PValor, PApariciones, PNumero):

        self.Nombre = PNombre
        self.Valor  = PValor
        self.Aparciones = PApariciones
        self.Numero =PNumero

        return

    def igualdadNombre(self, PNombre2):

        return self.Nombre == PNombre2

