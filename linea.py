import math
class Linea:

    def __init__(self):
        self.etiqueta   =   "NULL"
        self.comando    =   "NULL"
        self.argumento  =   "NULL"

    def toStr(self):
        return ("LECTURA " + self.etiqueta + " " + self.comando + " " + self.argumento)

    def asignarValores(self, etiquetaEntrada, comandoEntrada, argumentoEntrada):

        if(etiquetaEntrada == "" or etiquetaEntrada == "NULL" or  etiquetaEntrada ==" "):
            self.etiqueta = "NULL"

        else:
            self.etiqueta = etiquetaEntrada

        if (comandoEntrada == "" or comandoEntrada == "NULL" or comandoEntrada == " "):
            self.comando = "NULL"

        else:
            self.comando = comandoEntrada

        if (argumentoEntrada == "" or argumentoEntrada ==  "NULL" or argumentoEntrada == " "):
            self.argumento = "NULL"

        else:
            self.argumento = argumentoEntrada

    def rellenarFormatoPar(self, valor):

        while (len(valor) % 2 != 0):
            valor = "0" + valor

        return valor

    def rellenarFormatoByte(self, valor):

        while (len(valor) % 8 != 0):
            valor = "0" + valor

        return valor

    def retornarBase(self, valor):

        BanderaOctal    =   False
        BanderaHexa     =   False
        BanderaBin      =   False
        BAnderaASCII     =   False

        if (valor == "NULL"):
            return  "NULL"

        for i in valor:

            if i == "@":
                BanderaOctal = True

            if i == "$":
                BanderaHexa  = True

            if i == "%":
                BanderaBin  = True

            if i == "´":
                BAnderaASCII  = True

        if (BanderaOctal) and not (BanderaHexa or BanderaBin or BAnderaASCII):
            return "OCTAL"

        if (BanderaHexa) and not (BanderaOctal or BanderaBin or BAnderaASCII):
            return "HEXADECIMAL"

        if (BanderaBin) and not (BanderaOctal or BanderaHexa or BAnderaASCII):
            return "BINARIO"

        if (BAnderaASCII) and not (BanderaOctal or BanderaHexa or BanderaBin):
            return "ASCII"

        if not (BanderaOctal and BanderaHexa and BanderaBin and BAnderaASCII):
            return "DECIMAL"

        return "NULL"

    def retornarValorDec(self,valor):

        retornar = valor

        if "#" in retornar:
            retornar = retornar.replace("#", "")

        if "@" in retornar:
            retornar = retornar.replace("@", "")

        if "$" in retornar:
            retornar = retornar.replace("$", "")

        if "%" in retornar:
            retornar = retornar.replace("%", "")

        if (self.retornarBase(valor) == "NULL"):
            return "NULL"

        if (self.retornarBase(valor) == "DECIMAL"):
            retornar = str(int(retornar))

        if (self.retornarBase(valor) == "OCTAL"):
            retornar = str(int(retornar, 8))

        if (self.retornarBase(valor) == "HEXADECIMAL"):
            retornar = str(int(retornar, 16))

        if (self.retornarBase(valor) == "BINARIO"):
            retornar = str(int(retornar, 2))

        retornar = self.rellenarFormatoPar(retornar)
        return retornar

    def retornarValorOctal(self,valor):

        retornar = valor

        if "#" in valor:
            retornar = retornar.replace("#", "")

        if "@" in valor:
            retornar = retornar.replace("@", "")

        if "$" in valor:
            retornar = retornar.replace("$", "")

        if "%" in valor:
            retornar = retornar.replace("%", "")

        if (self.retornarBase(valor) == "NULL"):
            return "NULL"

        if (self.retornarBase(valor) == "DECIMAL"):
            retornar = oct(int(retornar))[2:]

        if (self.retornarBase(valor) == "OCTAL"):
            retornar = oct(int(retornar, 8))[2:]

        if (self.retornarBase(valor) == "HEXADECIMAL"):
            retornar = oct(int(retornar, 16))[2:]

        if (self.retornarBase(valor) == "BINARIO"):
            retornar = oct(int(retornar, 2))[2:]

        retornar = self.rellenarFormatoPar(retornar)
        return retornar

    def retornarValorHex(self,valor):

        retornar = valor

        if "#" in valor:
            retornar = retornar.replace("#", "")

        if "@" in valor:
            retornar = retornar.replace("@", "")

        if "$" in valor:
            retornar = retornar.replace("$", "")

        if "%" in valor:
            retornar = retornar.replace("%", "")

        if "´" in valor:
            retornar = retornar.replace("´", "")

        if(self.retornarBase(valor) == "NULL"):
            return  "NULL"

        if (self.retornarBase(valor) == "DECIMAL"):
            retornar = hex(int(retornar))[2:]

        if (self.retornarBase(valor) == "OCTAL"):
            retornar = hex(int(retornar,8))[2:]

        if (self.retornarBase(valor) == "HEXADECIMAL"):
            retornar = hex(int(retornar, 16))[2:]

        if (self.retornarBase(valor) == "BINARIO"):
            retornar = hex(int(retornar, 2))[2:]

        if (self.retornarBase(valor) == "ASCII"):
            retornar = str(hex(int(ord(retornar))))[2:]


        retornar = self.rellenarFormatoPar(retornar)
        return retornar

    def retornarValorBin(self,valor):

        retornar = valor

        if "#" in valor:
            retornar = retornar.replace("#", "")

        if "@" in valor:
            retornar = retornar.replace("@", "")

        if "$" in valor:
            retornar = retornar.replace("$", "")

        if "%" in valor:
            retornar = retornar.replace("%", "")

        if(self.retornarBase(valor) == "NULL"):
            return  "NULL"

        if (self.retornarBase(valor) == "DECIMAL"):
            retornar = bin(int(retornar))[2:]

        if (self.retornarBase(valor) == "OCTAL"):
            retornar = bin(int(retornar,8))[2:]

        if (self.retornarBase(valor) == "HEXADECIMAL"):
            retornar = bin(int(retornar,16))[2:]

        if (self.retornarBase(valor) == "BINARIO"):
            retornar = bin(int(retornar,2))[2:]

        retornar = self.rellenarFormatoPar(retornar)
        return retornar

    def sonMultiplesQ(self):
        separador = self.argumento.split(",");
        separador = ' '.join(separador).split()
        return len(separador) > 1

    def listaDeArgumentosPuros(self):

        retornar = self.argumento

        if "#" in retornar:
            retornar = retornar.replace("#", "")

        if "@" in retornar:
            retornar = retornar.replace("@", "")

        if "$" in retornar:
            retornar = retornar.replace("$", "")

        if "%" in retornar:
            retornar = retornar.replace("%", "")

        separador = retornar.split(",");
        separador = ' '.join(separador).split()
        return separador

    def listaDeArgumentosBrutos(self):

        retornar = self.argumento
        separador = retornar.split(",");
        separador = ' '.join(separador).split()
        return separador

    def listaDeArgumentosAHEX(self,valores):

        embutido = valores
        retornar = []


        if "#" in embutido:
            embutido = embutido.replace("#", "")

        separador = embutido.split(",");
        separador = ' '.join(separador).split()

        for i in separador:
            aux = self.retornarValorHex(i)
            retornar.append(aux)

        return retornar

    def obtenerLongitudDeByte(self,valor):

        embutido = valor
        alfa = 0

        if "#" in embutido:
            embutido = embutido.replace("#", "")

        embutido = self.retornarValorBin(embutido)
        embutido = self.rellenarFormatoByte(embutido)

        alfa = (len(embutido)/8)

        return alfa


    def LongitudDeArgumentos(self,valores):

        embutido = valores
        retornar = []


        if "#" in embutido:
            embutido = embutido.replace("#", "")

        separador = embutido.split(",");
        separador = ' '.join(separador).split()

        for i in separador:
            aux = self.obtenerLongitudDeByte(i)
            retornar.append(aux)

        return retornar

    def formato2HEX(self,valor):

        retorno = ""

        for i in range(0,len(valor)):

            if(i >= 2 and i%2 == 0):
                retorno += "_"

            retorno += valor[i]

        return retorno;

