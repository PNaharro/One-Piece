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
def menu(tupla):
    while True:
        cadena = ""
        for i in range(len(tupla)):
            cadena += (str(i+1)+")"+tupla[i]+"\n")
        print(cadena)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("Opcion invalida")
        elif int(opc) < 1 or int(opc) > len(tupla):
            print("Opcion invalida")
        else:
            return int(opc)
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

def getHeader_getHeadeForTableFromTuples2(text):
    x = (120-len(text))/2
    y = 120
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return

def ordenar_lista(lista, orden="asc"):
    print("a")