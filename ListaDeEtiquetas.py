from etiqueta import Etiqueta
import copy
class EtiquetaList:

    def __init__(self):
        self.lista = []
        self.Agregado = Etiqueta()

    def toStrFile(self):

        retorno = ""
        for Etiqueta in self.lista:
            retorno += Etiqueta.toStrFile()

        return retorno

    def toStrConsole(self):

        retorno = ""
        for Etiqueta in self.lista:
            retorno += Etiqueta.toStrConsole()

        return retorno

    def is_palabraReservada_Mnemonico(self, cadena):

        file = open('TABCOP.txt')

        while True:

            line = file.readline()

            if not line:
                return False
                break

            blankSeparator = line.split();
            blankSeparator = ' '.join(blankSeparator).split()


            if (cadena == blankSeparator[0]):
                return True
                break

        file.close()

        return False

    def is_palabraReservada_Directiva(self, cadena):


        Directivas = ["ORG", "END", "START", "EQU", "DC.B", "BSZ", "FILL", "DC.W", "FCC", "FCB"]

        if cadena in Directivas:
            return True

        return False


    def is_palabraReservada(self, cadena):

        A = self.is_palabraReservada_Directiva(cadena)
        B = self.is_palabraReservada_Mnemonico(cadena)

        if(A or B):
            return True

        return False

    def agregar(self, PNombre, PValor):

        if(self.is_palabraReservada(PNombre)):
            return False

        Apariciones = 1
        Numero      = 1

        for Etiqueta in self.lista:
            if (Etiqueta.Nombre == PNombre):
                Apariciones = Apariciones + 1
                Numero = Numero + 1

        Ajuste = Numero
        self.Agregado.asignarValores(PNombre, PValor, Apariciones, Numero)
        copia = copy.copy(self.Agregado)
        self.lista.append(copia)

        for Etiqueta in self.lista:
            if (Etiqueta.Nombre == PNombre):
                Etiqueta.Aparciones = Ajuste

        return True