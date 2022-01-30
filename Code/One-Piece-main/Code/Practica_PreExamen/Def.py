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
############## jugar ##################################################################################################################################
def getHeader_getHeadeForTableFromTuples2(text):
    x = (120-len(text))/2
    y = 120
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena
def getHeaderForTableFromTuples2(t_name_columns,t_size_columns,title):
    cadena = getHeader_getHeadeForTableFromTuples2(title) + "\n"
    for i in t_name_columns:
            cadena += i.rjust(t_size_columns[0])
            t_size_columns = t_size_columns[1:]
    cadena += "\n" + "*" * 119
    return cadena
##### listar ##########################################################################################################################################
def ordenar_lista(lista, orden="asc"):
    if orden == "asc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
        return lista
    if orden == "desc":
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] < lista[j + 1]:
                    numero = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = numero
        return lista
def ordenar_dict_dict_key(diccionario, orden="des", key=""):
    lista = []
    Z = []
    for i in diccionario:
        lista.append(diccionario[i][key])
    if orden == "des":
        for i in diccionario:
            Z = ordenar_lista(lista, orden="desc")
        return Z
    if orden == "asc":
        for i in diccionario:
            Z = ordenar_lista(lista, orden="asc")
        return Z
def getHeader_getHeadeForTableFromTuplesCharacter(text):
    x = (104-len(text))/2
    y = 104
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena
def headerDictCharactersTable(t_fields,t_sizeFields,title=""):
    cadena = getHeader_getHeadeForTableFromTuplesCharacter(title) + "\n"
    for i in t_fields:
        cadena += i.rjust(t_sizeFields[0])
        t_sizeFields = t_sizeFields[1:]
    cadena += "\n" + "*" * 104
    return cadena
#print(headerDictCharactersTable(("Id","Name","Strength","Speed","Experience"),(0,21,28,28,25),"Texto de ejemplo"))
#######################################################################################################################################################
def dictCharactersTable(list_keys,dic_characters,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    for j in list_keys:
        for i in dic_characters:
            if dic_characters[i][key] == j:
                cadena = str(i).ljust(19) + str(dic_characters[i]["name"]).ljust(24) + str(dic_characters[i]["strength"]).ljust(31) +\
                         str(dic_characters[i]["speed"]).ljust(29) + str(dic_characters[i]["experience"]).ljust(25)
                print(cadena)
def dictCharactersTableFuerza(list_keys,dic_characters,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    listaname = []
    listakey = []
    for i in Dicionarios.dict_characters:
        listaname.append(Dicionarios.dict_characters[i]["strength"])
        listakey.append(i)
    for i in range(len(listaname) - 1):
        for j in range(len(listaname) - i - 1):
            if listaname[j] < listaname[j + 1]:
                numero = listaname[j]
                listaname[j] = listaname[j + 1]
                listaname[j + 1] = numero
                numero = listakey[j]
                listakey[j] = listakey[j + 1]
                listakey[j + 1] = numero
    for i in listakey:
        cadena = str("{}".format(i)).ljust(19) + Dicionarios.dict_characters[i]["name"].ljust(24) + str(
            Dicionarios.dict_characters[i]["strength"]).ljust(31) + \
                 str(Dicionarios.dict_characters[i]["speed"]).ljust(20) + \
                 str(Dicionarios.dict_characters[i]["experience"]).ljust(25)
        print(cadena)
# lista = ordenar_dict_dict_key(Dicionarios.dict_characters,orden="des",key="name")
# print(lista)
# dictCharactersTable(lista,Dicionarios.dict_characters,("Id","Name","Strength","Speed","Experience"),(0,21,28,28,25),"Texto de ejemplo",key="name")
def dictCharactersTablevelocidad(list_keys,dic_characters,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    listaname = []
    listakey = []
    for i in Dicionarios.dict_characters:
        listaname.append(Dicionarios.dict_characters[i]["speed"])
        listakey.append(i)
    for i in range(len(listaname) - 1):
        for j in range(len(listaname) - i - 1):
            if listaname[j] < listaname[j + 1]:
                numero = listaname[j]
                listaname[j] = listaname[j + 1]
                listaname[j + 1] = numero
                numero = listakey[j]
                listakey[j] = listakey[j + 1]
                listakey[j + 1] = numero
    for i in listakey:
        cadena = str("{}".format(i)).ljust(19) + Dicionarios.dict_characters[i]["name"].ljust(24) + str(
            Dicionarios.dict_characters[i]["strength"]).ljust(31) + \
                 str(Dicionarios.dict_characters[i]["speed"]).ljust(20) + \
                 str(Dicionarios.dict_characters[i]["experience"]).ljust(25)
        print(cadena)
# lista = ordenar_dict_dict_key(Dicionarios.dict_characters,orden="des",key="name")
# print(lista)
# dictCharactersTable(lista,Dicionarios.dict_characters,("Id","Name","Strength","Speed","Experience"),(0,21,28,28,25),"Texto de ejemplo",key="name")
#################################################################################################################################################################
def getHeader_getHeadeForTableFromTuplesweapon(text):
    x = (64-len(text))/2
    y = 64
    if len(text)%2!=0:
        y -= 1
    cadena = "="*int(x) + text + "="*int(x)
    return cadena
def headerDictWeaponsTable(t_fields,t_sizeFields,title=""):
    cadena = getHeader_getHeadeForTableFromTuplesweapon(title) + "\n"
    for i in t_fields:
        cadena += i.rjust(t_sizeFields[0])
        t_sizeFields = t_sizeFields[1:]
    cadena += "\n" + "*" * 64
    return cadena
#print(headerDictWeaponsTable(("Id","Name","Strength","Speed","Experience"),(0,10,27,10,15),"Texto de ejemplo"))
def dictWeaponsTable(list_keys,dict_weapons,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    for j in list_keys:
        for i in dict_weapons:
            if dict_weapons[i][key] == j:
                cadena = str(i).ljust(19) + str(dict_weapons[i]["name"]).ljust(24) + str(
                    dict_weapons[i]["strength"]).ljust(23) + \
                         str(dict_weapons[i]["speed"]).ljust(30) + str(dict_weapons[i]["two_hand"]).ljust(25)
                print(cadena)
def dictWeaponsTableFuerza(list_keys,dict_weapons,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    listaname = []
    listakey = []
    for i in dict_weapons:
        listaname.append(dict_weapons[i]["strength"])
        listakey.append(i)
    for i in range(len(listaname) - 1):
        for j in range(len(listaname) - i - 1):
            if listaname[j] < listaname[j + 1]:
                numero = listaname[j]
                listaname[j] = listaname[j + 1]
                listaname[j + 1] = numero
                numero = listakey[j]
                listakey[j] = listakey[j + 1]
                listakey[j + 1] = numero
    for i in listakey:
        cadena = str("{}".format(i)).ljust(19) + str(dict_weapons[i]["name"]).ljust(24) + \
                 str(dict_weapons[i]["strength"]).ljust(23) + \
                 str(dict_weapons[i]["speed"]).ljust(30) + str(dict_weapons[i]["two_hand"]).ljust(25)
        print(cadena)
def dictWeaponsTableVelocidad(list_keys,dict_weapons,t_fields,t_sizeFields,title="",key=""):
    print(headerDictCharactersTable(t_fields, t_sizeFields, title))
    listaname = []
    listakey = []
    for i in dict_weapons:
        listaname.append(dict_weapons[i]["speed"])
        listakey.append(i)
    for i in range(len(listaname) - 1):
        for j in range(len(listaname) - i - 1):
            if listaname[j] < listaname[j + 1]:
                numero = listaname[j]
                listaname[j] = listaname[j + 1]
                listaname[j + 1] = numero
                numero = listakey[j]
                listakey[j] = listakey[j + 1]
                listakey[j + 1] = numero
    for i in listakey:
        cadena = str("{}".format(i)).ljust(19) + str(dict_weapons[i]["name"]).ljust(24) + \
                 str(dict_weapons[i]["strength"]).ljust(23) + \
                 str(dict_weapons[i]["speed"]).ljust(30) + str(dict_weapons[i]["two_hand"]).ljust(25)
        print(cadena)
###################################################################################################################################################################
def IdPersonaje():
    while True:
        ID = input("ID del Personaje: ")
        if not ID.isdigit():
            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
        elif int(ID) <= (len(Dicionarios.dict_characters) - len(Dicionarios.dict_characters)) \
                or int(ID) > len(Dicionarios.dict_characters):
            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
        else:
            return int(ID)
def opcionED(ID):
    while True:
        print("Selecciona la caracteristica a editar del personaje ID: {}, Nombre: {}\n\n1)Nombre\n2)Arma\n3)Atras"
            .format(ID, Dicionarios.dict_characters[ID]["name"]))
        while True:
            opcioned = input("->Opcion: ")
            if not opcioned.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcioned) < 1 or int(opcioned) > 3:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                opcioned = int(opcioned)
                return opcioned

def IdArma():
    while True:
        ID = input("ID del Arma: ")
        if not ID.isdigit():
            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
        elif int(ID) <= (len(Dicionarios.dict_weapons) - len(Dicionarios.dict_weapons)) or \
                int(ID) > len(Dicionarios.dict_weapons):
            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
        else:
            return int(ID)

def opcED(ID):
    while True:
        print("=" * 10, "Menu 032X (Caracteristica del Arma a Editar)", "=" * 10,
              "\n\n1)Nombre\n2)Plus Fuerza\n3)Plus Velocidad\n4)Atras\nElige la caracteristica a cambiar del arma ID: {}, Nombre: {}"
              .format(ID, Dicionarios.dict_weapons[ID]["name"]))
        while True:
            opcioned = input("->Opcion: ")
            if not opcioned.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcioned) < 1 or int(opcioned) > 4:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                return int(opcioned)