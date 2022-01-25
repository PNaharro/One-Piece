#####imports#####
import random
import Dicionarios
#### def ####
def Inicio(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena +="".ljust(45) + (str(i+1)+")"+tupla[i]+"\n")
        print(cadena)
        opc = input("".ljust(45)+"Opcion: ")
        if not opc.isdigit():
            print("Opcion invalida")
        elif int(opc) < 1 or int(opc) > len(tupla):
            print("Opcion invalida")
        else:
            return int(opc)

def Menu(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena +=(str(i+1)+")"+tupla[i]+"\n")
        print(cadena)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("Opcion invalida")
        elif int(opc) < 1 or int(opc) > len(tupla):
            print("Opcion invalida")
        else:
            return int(opc)
def Fuerza():
    while True:
        strength = input("fuerza del arma 1-9: ")
        if not strength.isdigit():
            print("opcion incorecta")

        elif int(strength) < 1 or int(strength) > 9:
            print("opcion incorecta")

        else:
            break
    return strength

def Speed():
    while True:
        speed = input("velodidad del arma 1-9: ")
        if not speed.isdigit():
            print("opcion incorecta")

        elif int(speed) < 1 or int(speed) > 9:
            print("opcion incorecta")

        else:
            break
    return speed

def enpuñadura():
    menu_Tipo_arma = "tipo de arma\n1)Una Mano\n2)Dos Manos"
    while True:
        print(menu_Tipo_arma)
        tipo_mano = input("-->")
        if not tipo_mano.isdigit():
            print("opcion incorecta")

        elif int(tipo_mano) < 1 or int(tipo_mano) > 2:
            print("opcion incorecta")

        else:
            tipo_mano = int(tipo_mano)

        if tipo_mano == 1:
            two_hand = False
            break
        if tipo_mano == 2:
            two_hand = True
            break
    return two_hand

def getOpt(textopts="",inputOptText="",rangeList=[],exceptions=[]):
    while True:
        print(textopts)
        opc = input(inputOptText)
        for i in exceptions:
            for j in rangeList:
                if opc != i:
                    print("error")
                elif opc != j:
                    print("error")
                else:
                    return opc


# opc = getOpt(textopts="1)Login\n2)Create user\n3)Show Adventures\n4)Exit",inputOptText="\nElige tu opción:",rangeList=[1,2,3,4],exceptions=["w","e",-1])
# print(opc)
def Cabecera(text):
    x = (100-len(text))/2
    y = 100
    if len(text)%2!=0:
        y -= 1
    cadena = "*"*y +"\n" + "="*int(x) + text + "="*int(x) + "\n" + "*"*y
    return cadena

def getHeader(text):
    x = (25-len(text))/2
    y = 25
    if len(text)%2!=0:
        y -= 1
    cadena = "*"*y +"\n" + "="*int(x) + text + "="*int(x) + "\n" + "*"*y
    return cadena

def getHeader_getHeadeForTableFromTuples(text):
    x = (104-len(text))/2
    y = 104
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena

def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title):
    cadena = getHeader_getHeadeForTableFromTuples(title) + "\n"
    for i in t_name_columns:
            cadena += i.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 104
    return cadena

def ordenar_lista(lista1, orden="asc"):
    lista = []
    for x in lista1:
        lista.append(x)
    print(lista)
    if orden == "desc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
        print(lista)
    if orden == "asc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
        print(lista)

