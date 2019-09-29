from linea import Linea
from ListaDeEtiquetas import EtiquetaList

Lectura = Linea()
LEtiqutas = EtiquetaList()

def escribirArchivo(cadena,archivo):
    file = open(archivo, 'w')
    file.write(cadena)
    file.close()
def rellenarFormatoPar(valor):

    while (len(valor) % 2 != 0):
        valor = "0" + valor

    return valor


def sumaHex(A,B):
    Numero1 = int(A,16)
    Numero2 = int(B,16)
    NumeroR = Numero1 + Numero2
    retorno = hex(NumeroR)
    retorno = retorno[2:]
    retorno = rellenarFormatoPar(retorno)
    return  retorno

def validadorInicial(cadena):

    separator = cadena.split(";")

    if (len(separator) <= 1 or len(separator) > 2):
        print("Archivo dañado")
        return ["ERROR", "ERROR", "ERROR", "ERROR"]

    blankSeparator = separator[0].split();
    blankSeparator = ' '.join(blankSeparator).split()

    if(len(blankSeparator) == 3):
        return  [blankSeparator[0],blankSeparator[1],blankSeparator[2],separator[1]]

    if (len(blankSeparator) == 2):

        if (not LEtiqutas.is_palabraReservada(blankSeparator[0])):
            return [blankSeparator[0], blankSeparator[1], "", separator[1]]
        else:
            return ["", blankSeparator[0], blankSeparator[1], separator[1]]


    if (len(blankSeparator) == 1):
        return ["", blankSeparator[0], "", separator[1]]

def TrackingNumero(NumeroHex,TuplaF):

    if (TuplaF[0] == "S" or TuplaF[0] == "M"):
        return sumaHex(NumeroHex,TuplaF[1])

    if (TuplaF[0] == "R"):
        return TuplaF[1]

    else:
        return NumeroHex


def Asignamiento(cadena):
    parametrosLectura = validadorInicial(cadena)
    Lectura.asignarValores(parametrosLectura[0],parametrosLectura[1],parametrosLectura[2])
    if(parametrosLectura[0] == "ERROR"):
        print("ERROR")
        return False
    else:
        print("ETIQUETA:\t\t", parametrosLectura[0])
        print("OPERACION:\t\t", parametrosLectura[1])
        print("ARGUMENTO:\t\t", parametrosLectura[2])
        print("COMENTARIO:\t\t ", parametrosLectura[3])
        return True

def Asignamiento2(cadena):
    parametrosLectura = validadorInicial(cadena)
    Lectura.asignarValores(parametrosLectura[0],parametrosLectura[1],parametrosLectura[2])
    if(parametrosLectura[0] == "ERROR"):
        print("ERROR")
        return False
    else:
        return True

def buscarEnDirectivas():

    #Asegurarse de retornar ["MODO","VALOR HEX", "IMPRESION",...."OTROS"]

    if(Lectura.comando == "START"):
        return ["R", "00", "NULL"]

    if(Lectura.comando == "ORG"):
        return ["R", str(Lectura.retornarValorHex(Lectura.argumento)), "NULL"]

    if (Lectura.comando == "EQU"):
        return ["A", "0", "NULL"]

    if (Lectura.comando == "END"):
        return ["E", "NULL", "NULL"]

    elif ("BSZ" == Lectura.comando):
        cadena = ""
        retorno = []
        retorno.append("S")
        retorno.append(str(Lectura.retornarValorHex(Lectura.argumento)))
        cadena = "00"
        for i in range(0,int(retorno[1], 16)-1):
            cadena += " 00"

        retorno.append(cadena)
        return(retorno)

    elif ("ZMB" == Lectura.comando):
        cadena = ""
        retorno = []
        retorno.append("S")
        retorno.append(str(Lectura.retornarValorHex(Lectura.argumento)))
        cadena = "00"
        for i in range(0,int(retorno[1], 16)-1):
            cadena += " 00"
        return(retorno)

    elif ("FCB" == Lectura.comando):

        retorno = []
        retorno.append("S")
        aux = Lectura.argumento
        cantidad = aux.split(",")

        for i in range(0,len(cantidad)):
            alfa = Lectura.retornarValorHex(cantidad[i])
            cantidad[i] = alfa

        retorno.append(Lectura.retornarValorHex(str(len(cantidad))))

        IMPRESION = ""
        for x in cantidad:
            IMPRESION += x + " "

        retorno.append(IMPRESION)
        retorno = retorno + cantidad

        return(retorno)

    elif ("FCC" == Lectura.comando):

        retorno = []
        retorno.append("S")
        palabra = Lectura.argumento.replace("/", "")
        retorno.append(Lectura.retornarValorHex(str(len(palabra))))
        reservado = ""

        for i in range(0, len(palabra)):
            alfa = Lectura.retornarValorHex(str(int(ord(palabra[i]))))
            reservado += alfa + " "
        retorno.append(reservado)

        return(retorno)

    elif ("DC.B" == Lectura.comando):

        retorno = []
        retorno.append("S")

        if (Lectura.argumento == "NULL"):
            retorno.append("1")
            retorno.append("00")
            return (retorno)

        lista = Lectura.listaDeArgumentosAHEX(Lectura.argumento)
        cadena = ""

        for i in lista:
            cadena += str(i) + " "

        retorno.append(Lectura.retornarValorHex(str(len(lista))))
        retorno.append(cadena)

        return(retorno)

    elif ("DC.W" == Lectura.comando):
        retorno = []
        retorno.append("S")

        if (Lectura.argumento == "NULL"):
            retorno.append("2")
            retorno.append("00 00")
            return (retorno)

        lista = Lectura.listaDeArgumentosAHEX(Lectura.argumento)
        cadena = ""

        for i in lista:
            cadena += "00" + " "
            cadena += str(i) + " "

        retorno.append(Lectura.retornarValorHex(str(2**len(lista))))
        retorno.append(cadena)
        return(retorno)

    elif ("FILL" == Lectura.comando):
        retorno = []
        retorno.append("S")
        sosten = ""
        argummento = Lectura.argumento
        argumentado = argummento.split(",")
        retorno.append(Lectura.retornarValorHex(str(int(argumentado[1]))))
        for i in range(0, int(argumentado[1])):
            alfa = str(Lectura.retornarValorHex((argumentado[0])))
            sosten += Lectura.formato2HEX(alfa) + " "
        retorno.append(sosten)
        return(retorno)



    return ["NULL","NULL","NULL"]

def buscarEnArchivo():

    buscado = ""

    if ("#" in Lectura.argumento):
        buscado = "IMM"

    elif("NULL" == Lectura.argumento):
        buscado = "INH"

    elif (not Lectura.sonMultiplesQ()):
        if(Lectura.obtenerLongitudDeByte(Lectura.argumento) < 2):
            buscado = "DIR"
        elif(int(Lectura.obtenerLongitudDeByte(Lectura.argumento)) >= 2):
            buscado = "EXT"

    file = open('TABCOP.txt')

    while True:

        line = file.readline()

        if not line:
            return ["NULL","NULL","NULL","NULL"]
            break

        blankSeparator = line.split();
        blankSeparator = ' '.join(blankSeparator).split()

        #print("BS: ", blankSeparator[2], "Buscado: ", buscado,"Comando", Lectura.comando, "Comando Archivo: ", blankSeparator[0], "BST: ", blankSeparator)

        if (blankSeparator[2] == buscado and (Lectura.comando == blankSeparator[0])):
            break;

        if(blankSeparator[2] == "REL" and (Lectura.comando == blankSeparator[0])):
            break


    file.close()

    estructuraS = blankSeparator[3].split("_")
    AUX = Lectura.listaDeArgumentosAHEX(Lectura.argumento)
    estructuraSSTR = ""

    for i in AUX:
        #print(i)
        estructuraSSTR += "_" + Lectura.formato2HEX(i)

    estructuraSSTR = estructuraS[0] + estructuraSSTR

    if(buscado == "INH"):
        estructuraSSTR = blankSeparator[3]

    # return ["M", Lectura.comando, buscado, Lectura.retornarValorHex(str(len(blankSeparator[3].split("_")))), blankSeparator[3], estructuraSSTR]
    return ["M", Lectura.retornarValorHex(str(len(blankSeparator[3].split("_")))), estructuraSSTR, blankSeparator[3]]

def asignarEtiqueta(NumeroHex):

    retorno = ""

    if(Lectura.etiqueta == "NULL"):
        return ""

    if(Lectura.comando == "EQU"):
        retorno += Lectura.etiqueta + " -> " + Lectura.retornarValorHex(Lectura.argumento) + "\n"

    else:
        retorno += Lectura.etiqueta + " ->" + NumeroHex + "\n"

    return  retorno

def asignarEtiquetaLectura1Segura(NumeroHex):

    retorno = []

    if(Lectura.etiqueta == "NULL"):
        return ["NULL","NULL"]

    if(Lectura.comando == "EQU"):
        return [Lectura.etiqueta, Lectura.retornarValorHex(Lectura.argumento)]

    else:
        return [Lectura.etiqueta, NumeroHex]

    return  retorno


def asignarCadena(NumeroHex,Lista):
    retorno = ""

    retorno += NumeroHex + "\t\t\t"

    if(Lectura.etiqueta != "NULL"):
        retorno += Lectura.etiqueta + "\t\t\t"

    else:
        retorno += "" + "\t\t\t"

    retorno += Lectura.comando + "\t\t\t"

    retorno += Lectura.argumento + "\t\t\t"

    #retorno += Lista[0] + "\t\t\t"

    retorno += Lista[1] + "\t\t\t"

    retorno += Lista[2] + "\t\t\n"

    return retorno

def Lectura1():

    numero = "00"
    etiquetasFinal = ""
    archivoFinal = ""
    Archivo = "Ingreso.txt"

    file = open(Archivo)

    while True:

        line = file.readline()

        if not line:
            print("Se ha terminado la lectura de archivo")
            break


        if(not Asignamiento(line)):
            break

        Decantador = buscarEnDirectivas()
        etiquetasFinal += asignarEtiqueta(numero)
        Seguro1 = asignarEtiquetaLectura1Segura(numero)
        #print(Seguro1)
        if(Seguro1[0] != "NULL"):
            print("Entramos Etiquetas L1")
            if(not LEtiqutas.is_palabraReservada(Seguro1[0])):
                LEtiqutas.agregar(Seguro1[0], Seguro1[1])
            else:
                print("Etiqueta no valida")
                break;

        if(Decantador[0] != "NULL"):
            archivoFinal += asignarCadena(numero,Decantador)
            if (Lectura.comando == "END"):
                print("Directiva TERMINAL")
                break

        else:
            Decantador = buscarEnArchivo()
            if(Decantador[0] == "NULL"):
                file.close()
                print("Mnemonico Inexistente")
                return
            else:
                archivoFinal += asignarCadena(numero,Decantador)

        numero = TrackingNumero(numero,Decantador)


    file.close()
    #print(etiquetasFinal)
    #print(archivoFinal)
    ArchivoEtiquetas = "tabsim.txt"
    ArchivoF = "lst.txt"

    #escribirArchivo(etiquetasFinal, "tabsim.txt")
    #escribirArchivo(archivoFinal, "lst.txt")

    print(LEtiqutas.toStrConsole())

    return True

def Lectura2():

    numero = "00"
    etiquetasFinal = ""
    archivoFinal = ""
    Archivo = "Ingreso.txt"

    file = open(Archivo)

    while True:

        line = file.readline()

        if not line:
            print("Se ha terminado la lectura de archivo")
            break


        if(not Asignamiento2(line)):
            break

        Decantador = buscarEnDirectivas()
        etiquetasFinal += asignarEtiqueta(numero)
        Seguro1 = asignarEtiquetaLectura1Segura(numero)
        #print(Seguro1)
        if(Seguro1[0] != "NULL"):
            if(LEtiqutas.is_palabraReservada(Seguro1[0])):
                print("Etiqueta no valida")
                break;

        if(Decantador[0] != "NULL"):
            archivoFinal += asignarCadena(numero,Decantador)
            if (Lectura.comando == "END"):
                print("Directiva TERMINAL")
                break

        else:
            Decantador = buscarEnArchivo()
            if(Decantador[0] == "NULL"):
                file.close()
                print("Mnemonico Inexistente")
                return
            else:
                archivoFinal += asignarCadena(numero,Decantador)

        numero = TrackingNumero(numero,Decantador)


    file.close()
    print(etiquetasFinal)
    print(archivoFinal)
    ArchivoEtiquetas = "tabsim.txt"
    ArchivoF = "lst.txt"

    escribirArchivo(etiquetasFinal, "tabsim.txt")
    escribirArchivo(archivoFinal, "lst.txt")

    #print(LEtiqutas.toStrConsole())

    return True


Lectura1()
Lectura2()