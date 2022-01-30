import random
dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" : 7,"experience": 0},
                    2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience": 0},
                    3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" : 6,"experience": 0 },
                    4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4, "experience" : 0},
                    5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience" : 0},
                    6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5, "experience" : 0},
                    7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3, "experience" : 0},
                    8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1, "experience" : 0},
                    9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4, "experience" : 0},
                    10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8, "experience" : 0},
                    11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4, "experience" : 0},
                    12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3, "experience" : 0},
                    13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5, "experience" : 0},
                    14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4, "experience" : 0},
                    15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4, "experience" : 0},
                  }

dict_weapons = { 1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
               2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
               3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
               4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
               5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
               }


dict_crews = { 1 : {"name" : "Straw hat","members": [8,6]},
                       2 : {"name" : "Pirates Buggy","members": [1,3,5]},
                       3: {"name": "Pirates Rocks","members": [2,4,7,]}
               }

dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
               2 : {"name" : "ViceAdmiral","members": [12,13]},
               3: {"name": "Lieutenant","members": [14,15]}
               }

dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

# Banderas
flag = True
flag_creacion = True
flag_arma = True
flag_band = True
flag_rango = True
flag_speed = True
flag_stre = True
flag_tipoArma = True
flag_listar = True
flag_listar_char = True
flag_listar_wea = True

# menus
menu0 = "="*8+"Menu0 (One Piece)"+"="*8+"\n"+"1)Play\n"+"2)crear\n"+"3)editar\n"+"4)list\n"+"5)salir\n"
menu02 = "="*8+"Menu02 (create)"+"="*8+"\n"+"1)Create character\n"+"2)create Weapon\n"+"3)go back\n"
menu_band = "Elige bando\n1)marina\n2)piratas"
menu_rango_man = "Elige rango\n1)Admiral\n2)ViceAdmiral\n3)Lieutenant"
menu_rango_pir = "Elige banda\n1)Straw hat\n2)Pirates Buggy\n3)Pirates Rocks"
menu_add_arma = "add Weapon \n Weapon Id) to add weapon Id \n 0) finish Weapon\n Weapon Id) delete weapon"
menu_Tipo_arma = "tipo de arma\n1) una manos\n2)dos manos"
menu_lista = "="*8+"Menu04 (list)"+"="*8+"\n"+"1)list characters\n"+"2)list Weapons\n"+"3)list side\n"+"4)lista range\n"+"5)go back\n"
menu_lista_char = "="*8+"Menu041 (list characters)"+"="*8+"\n"+"1)list by id\n"+"2)list by name\n"+"3)list by strength\n"+"4)lista by speed\n"+"5)go back\n"

# listas
arma = []
weapon = []
weapon_num = []
strength = []
speed = []
hands = []

#codigo
while flag:
    flag_creacion = True
    flag_arma = True
    flag_band = True
    flag_rango = True
    flag_speed = True
    flag_stre = True
    flag_tipoArma = True
    flag_listar = True
    flag_listar_char = True
    flag_listar_wea = True
    print(menu0)
    opc = input("opcion:")
    if not opc.isdigit():
        print("opcion incorecta")
    elif int(opc) < 1 or int(opc) > 5:
        print("opcion incorecta")
    else:
        opc = int(opc)
        if opc  ==1:
            print("Play")
        if opc == 2:
            print("Crear")
            while flag_creacion:
                flag_creacion = True
                flag_arma = True
                flag_band = True
                flag_rango = True
                print(menu02)
                opc = input("opcion:")
                if not opc.isdigit():
                    print("opcion incorecta")
                elif int(opc) < 1 or int(opc) > 5:
                    print("opcion incorecta")
                else:
                    opc = int(opc)
                    if opc ==1:
                        print("create charater")
                        nombre_ch = input("introduce el nombre del personaje: ")

                        while flag_band:
                            print(menu_band)
                            band = input("opcion:")

                            if not band.isdigit():
                                print("opcion incorecta")

                            elif int(band) < 1 or int(band) > 2:
                                print("opcion incorecta")

                            else:
                                band = int(band)

                                if band == 1:
                                    bando = "Marines"
                                    print("marines")

                                    while flag_rango:
                                        print(menu_rango_man)
                                        rango = input("opcion: ")

                                        if not rango.isdigit():
                                            print("opcion incorecta")

                                        elif int(rango) < 1 or int(rango) > 3:
                                            print("opcion incorecta")

                                        else:
                                            rango = int(rango)

                                            if (rango+3) in dict_categorys:
                                                rank = dict_categorys[rango+3]
                                                rank_num = rango+3
                                                print(rank)
                                                flag_band = False
                                                flag_rango = False
                                if band == 2:
                                    bando = "piratas"
                                    print("piratas")

                                    while flag_rango:
                                        print(menu_rango_pir)
                                        rango = input("opcion: ")

                                        if not rango.isdigit():
                                            print("opcion incorecta")

                                        elif int(rango) < 1 or int(rango) > 3:
                                            print("opcion incorecta")

                                        else:
                                            rango = int(rango)

                                            if rango in dict_categorys:
                                                rank = dict_categorys[rango]
                                                rank_num = rango
                                                print(rank)
                                                flag_band = False
                                                flag_rango = False

                        while flag_arma:
                            print("=" * 8 + "Avalible Weapon" + "=" * 8)
                            if len(arma) == 0:
                                for i in range(len(dict_weapons)):
                                    cadena = str(i + 1) + ") " + dict_weapons[i + 1]["name"] + ", strength: " + str(
                                        dict_weapons[i + 1]["strength"]) \
                                             + ", speed: " + str(dict_weapons[i + 1]["speed"])
                                    print(cadena)
                                print("\n" * 3 + "=" * 8 + "character Weapon" + "=" * 8)
                                print("-" * 14 + "none" + "-" * 14)
                            if len(arma) == 1:
                                if hands[0] == True:
                                    print("-" * 14 + "none" + "-" * 14)
                                    print("\n" * 3 + "=" * 8 + "character Weapon" + "=" * 8)
                                    strarma = "".join(arma)
                                    print(strarma)
                                if hands[0] == False:
                                    for i in range(len(dict_weapons)):
                                        a = dict_weapons[i + 1]["two_hand"]
                                        if a == False:
                                            cadena = str(i + 1) + ") " + dict_weapons[i + 1][
                                                "name"] + ", strength: " + str(
                                                dict_weapons[i + 1]["strength"]) \
                                                     + ", speed: " + str(dict_weapons[i + 1]["speed"])
                                            print(cadena)
                                    print("\n" * 3 + "=" * 8 + "character Weapon" + "=" * 8)
                                    strarma = "".join(arma)
                                    print(strarma)
                            if len(arma) >= 2:
                                print("-" * 14 + "none" + "-" * 14)
                                print("\n" * 3 + "=" * 8 + "character Weapon" + "=" * 8)
                                strarma = "".join(arma)
                                print(strarma)
                            print("\n" * 3 + menu_add_arma)
                            opc_arma = input("opcion: ")
                            print(hands)

                            if not opc_arma.isdigit() and (len(opc_arma) <= 1):
                                print("opcion incorecta 1")

                            elif int(opc_arma) > len(dict_weapons):
                                print("opcion incorecta 5")

                            elif len(arma) >=2 and opc_arma != 0:
                                print("no se pueden añadir mas armas")

                            elif len(arma) == 1 and hands[0] == True and opc_arma != 0:
                                    print("no se pueden llebar mas armas")

                            elif len(opc_arma) > 1:
                                if not opc_arma[0] == "-":
                                     print("opcion incorecta")
                                elif not opc_arma[1].isdigit():
                                    print("opcion incorecta")

                                elif int(opc_arma[1]) > len(dict_weapons):
                                     print("opcion incorecta")

                                if opc_arma[0] == "-" or opc_arma[1].isdigit():
                                    print("")
                            else:
                                opc_arma = int(opc_arma)

                            if opc_arma == 0:
                                F = random.randrange(1,9)
                                S = random.randrange(1,9)
                                cadena = "Name: " + nombre_ch + "\nCategori: " + str(rank) + "\nWeapons: " + str(
                                        weapon) + "\nStrength: " + str(F) + "\nSpeed: " + str(S)\
                                         + "\nTipo de empuñadura: " + str(hands)[1:-1]+ "\nExperiens: "+ "0"
                                print(cadena)
                                while True:
                                    opc_acep = input("guarda arma s/n ")
                                    if opc_acep == "s" or opc_acep == "S":
                                        dict_characters[len(dict_characters) + 1] = {"name": nombre_ch,"category":rank_num,"weapons": weapon_num, "strength": F,
                                                                               "speed": S, "experience": "0"}
                                        print(dict_characters)
                                        flag_arma = False
                                        arma.clear()
                                        weapon.clear()
                                        weapon_num.clear()
                                        strength.clear()
                                        speed.clear()
                                        hands.clear()
                                        break

                                    if opc_acep == "n" or opc_acep == "N":
                                        print("no se ha guardado")
                                        flag_arma = False
                                        break
                                    else:
                                        print("opcion incorecta")

                            elif opc_arma in dict_weapons:
                                cadena = str(opc_arma)+") " + dict_weapons[opc_arma]["name"] + ", strength: " + str(dict_weapons[opc_arma]["strength"]) \
                                      + ", speed: " + str(dict_weapons[opc_arma]["speed"])
                                arma.append(cadena+"\n")
                                weapon.append([dict_weapons[opc_arma]["name"]])
                                weapon_num.append(opc_arma)
                                strength.append(dict_weapons[opc_arma]["strength"])
                                speed.append(dict_weapons[opc_arma]["speed"])
                                hands.append(dict_weapons[opc_arma]["two_hand"])

                            elif opc_arma[0] == "-":

                                if int(opc_arma[1]) in dict_weapons:
                                    if len(arma) != 0:
                                        cadena = str(opc_arma[1:]) + ") " + dict_weapons[int(opc_arma[1:])]["name"] + ", strength: " + str(dict_weapons[int(opc_arma[1:])]["strength"]) \
                                         + ", speed: " + str(dict_weapons[int(opc_arma[1:])]["speed"])
                                        A = arma.index(cadena + "\n")
                                        arma.pop(A)

                                        if len(weapon) == 1 or len(weapon_num) == 1:

                                            weapon.clear()
                                            weapon_num.clear()
                                            hands.clear()
                                        if len(weapon) == 2 or len(weapon_num) == 2:
                                            weapon.pop()
                                            weapon_num.pop()
                                            hands.pop()

                    if opc ==2:
                        print("create Weapon")
                        flag_speed = True
                        flag_stre= True
                        flag_tipoArma = True
                        nombre = input("introduce el nombre del arma: ")
                        while flag_stre:
                            strength = input("fuerza del arma 1-9: ")
                            if not strength.isdigit():
                                print("opcion incorecta")

                            elif int(strength) < 1 or int(strength) > 9:
                                print("opcion incorecta")

                            else:
                                flag_stre = False
                        while flag_speed:
                            speed = input("velodidad del arma 1-9: ")
                            if not speed.isdigit():
                                print("opcion incorecta")

                            elif int(speed) < 1 or int(speed) > 9:
                                print("opcion incorecta")

                            else:
                                flag_speed = False
                        while flag_tipoArma:
                            print(menu_Tipo_arma)
                            tipo_mano = input("fuerza del arma 1-9: ")
                            if not tipo_mano.isdigit():
                                print("opcion incorecta")

                            elif int(tipo_mano) < 1 or int(tipo_mano) > 2:
                                print("opcion incorecta")

                            else:
                                tipo_mano = int(tipo_mano)

                            if tipo_mano == 1:
                                two_hand = False
                                flag_tipoArma = False
                            if tipo_mano == 2:
                                two_hand = True
                                flag_tipoArma = False
                        cadana2 = "name: "+ nombre + "\nstrength: "+ str(strength) + "\nspeed: " + str(speed) +"\ntipo de empuñadura: " + str(two_hand)
                        print(cadana2)
                        while True:
                            opc_acep = input("guarda arma s/n ")
                            if opc_acep == "s" or opc_acep == "S":
                                dict_weapons[len(dict_weapons) + 1] = {"name": nombre, "strength": int(strength),"speed": int(speed), "two_hand": two_hand}
                                print(dict_weapons)
                                break
                            if opc_acep == "n" or opc_acep == "N":
                                print("no se ha guardado")

                                break
                            else:
                                print("opcion incorecta")
                    if opc ==3:
                        print("go back")
                        flag_creacion=False
                        opc = 0
        if opc == 3:
            print("editar")
        if opc == 4:
            print("list")
            while flag_listar:
                flag_listar_char = True
                flag_listar_wea = True
                print(menu_lista)
                opc = input("opcion:")
                if not opc.isdigit():
                    print("opcion incorecta")
                elif int(opc) < 1 or int(opc) > 5:
                    print("opcion incorecta")
                else:
                    opc = int(opc)
                    if opc == 1:
                        print("list characters")
                        while flag_listar_char:
                            print(menu_lista_char)
                            opc = input("opcion:")
                            if not opc.isdigit():
                                print("opcion incorecta")
                            elif int(opc) < 1 or int(opc) > 5:
                                print("opcion incorecta")
                            else:
                                opc = int(opc)
                                if opc == 1:
                                    print("list by Id")
                                    cadena = "=" * 20 + "Characters ordered by ID" + "=" * 20 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(10) + "Experience".ljust(10) + "\n" + "=" * 64
                                    print(cadena)
                                    listaid = []
                                    for i in dict_characters:
                                        listaid.append(i)
                                        for j in dict_characters[i]["weapons"]:
                                            dict_characters[i]["strength"] += dict_weapons[j]["strength"]
                                            dict_characters[i]["speed"] += dict_weapons[j]["speed"]

                                    for i in dict_characters:
                                        cadena = str(i).ljust(10) + dict_characters[i]["name"].ljust(27) + str(dict_characters[i]["strength"]).ljust(11) + \
                                                 str(dict_characters[i]["speed"]).ljust(15) + str(dict_characters[i]["experience"]).ljust(10)
                                        print(cadena)
                                    print("\n")

                                if opc == 2:
                                    print("list by name")
                                    cadena = "=" * 20 + "Characters ordered by Name" + "=" * 20 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(10) + "Experience".ljust(10) + "\n" + "=" * 64
                                    print(cadena)
                                    listaid = []
                                    listaname = []
                                    for i in dict_characters:
                                        listaid.append(i)
                                        listaname.append(dict_characters[i]["name"])
                                        for j in dict_characters[i]["weapons"]:
                                            dict_characters[i]["strength"] += dict_weapons[j]["strength"]
                                            dict_characters[i]["speed"] += dict_weapons[j]["speed"]
                                    for i in range(len(listaname) - 1):
                                        for j in range(len(listaname) - i - 1):
                                            if listaname[j] < listaname[j + 1]:
                                                numero = listaname[j]
                                                listaname[j] = listaname[j + 1]
                                                listaname[j + 1] = numero

                                    for i in listaname:
                                        for j in dict_characters:
                                            if i == dict_characters[j]["name"]:
                                                cadena = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(27) + str(dict_characters[j]["strength"]).ljust(11) + \
                                                 str(dict_characters[j]["speed"]).ljust(15) + str(dict_characters[j]["experience"]).ljust(10)
                                        print(cadena)
                                    print("\n")
                                if opc == 3:
                                    print("list by strength")
                                    cadena = "=" * 20 + "Characters ordered by Name" + "=" * 20 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(10) + "Experience".ljust(10) + "\n" + "=" * 64
                                    print(cadena)
                                    listaname = []
                                    listakey = []
                                    for i in dict_characters:
                                        listaname.append(dict_characters[i]["strength"])
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
                                        cadena = str("{}".format(i)).ljust(25) + dict_characters[i]["name"].ljust(28) + str(dict_characters[i]["strength"]).ljust(28) + \
                                                    str(dict_characters[i]["speed"]).ljust(25) + str(dict_characters[i]["experience"]).ljust(25)
                                        print(cadena)
                                if opc == 4:
                                    print("list by speed")
                                    cadena = "=" * 20 + "Characters ordered by Name" + "=" * 20 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(10) + "Experience".ljust(10) + "\n" + "=" * 64
                                    print(cadena)
                                    listaname = []
                                    listakey = []
                                    for i in dict_characters:
                                        listaname.append(dict_characters[i]["speed"])
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
                                        cadena = str("{}".format(i)).ljust(10) + dict_characters[i]["name"].ljust(27) + str(dict_characters[i]["strength"]).ljust(11) + \
                                                    str(dict_characters[i]["speed"]).ljust(15) + str(dict_characters[i]["experience"]).ljust(10)
                                        print(cadena)
                                if opc == 5:
                                    print("go back")
                                    opc = 0
                                    flag_listar_char = False
                    if opc == 2:
                        print("list Weapons")
                        while flag_listar_wea:
                            print(menu_lista_char)
                            opc = input("opcion:")
                            if not opc.isdigit():
                                print("opcion incorecta")
                            elif int(opc) < 1 or int(opc) > 5:
                                print("opcion incorecta")
                            else:
                                opc = int(opc)
                                if opc == 1:
                                    print("list by Id")
                                    cadena = "=" * 21 + "Weapons ordered by ID" + "=" * 22 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(11) + "Two Hands".ljust(12) + "\n" + "=" * 64
                                    print(cadena)
                                    for i in dict_weapons:
                                        cadena = str(i).ljust(10) + dict_weapons[i]["name"].ljust(27) + str(
                                            dict_weapons[i]["strength"]).ljust(11) + \
                                                 str(dict_weapons[i]["speed"]).ljust(11) + str(dict_weapons[i]["two_hand"]).ljust(10)
                                        print(cadena)
                                    print("\n")
                                if opc == 2:
                                    print("list by name")
                                    cadena = "=" * 21 + "Weapons ordered by ID" + "=" * 22 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(11) + "Two Hands".ljust(12) + "\n" + "=" * 64
                                    print(cadena)
                                    listaname = []
                                    for i in dict_weapons:
                                        listaname.append(dict_weapons[i]["name"])
                                    for i in range(len(listaname) - 1):
                                        for j in range(len(listaname) - i - 1):
                                            if listaname[j] < listaname[j + 1]:
                                                numero = listaname[j]
                                                listaname[j] = listaname[j + 1]
                                                listaname[j + 1] = numero
                                    for i in listaname:
                                        for j in dict_weapons:
                                            if i == dict_weapons[j]["name"]:
                                                cadena = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(
                                                    27) + str(dict_weapons[j]["strength"]).ljust(11) + \
                                                         str(dict_weapons[j]["speed"]).ljust(11) + str(dict_weapons[j]["two_hand"]).ljust(10)
                                        print(cadena)
                                    print("\n")
                                if opc == 3:
                                    print("list by strength")
                                    cadena = "=" * 21 + "Weapons ordered by ID" + "=" * 22 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(11) + "Two Hands".ljust(12) + "\n" + "=" * 64
                                    print(cadena)
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
                                        cadena = str("{}".format(i)).ljust(10) + str(dict_weapons[i]["name"]).ljust(
                                                    27) + str(dict_weapons[i]["strength"]).ljust(11) + \
                                                         str(dict_weapons[i]["speed"]).ljust(11) + str(dict_weapons[i]["two_hand"]).ljust(10)
                                        print(cadena)
                                    print("\n")
                                if opc == 4:
                                    print("list by speed")
                                    cadena = "=" * 21 + "Weapons ordered by ID" + "=" * 22 + "\n" + "Id".ljust(
                                        10) + "Name".ljust(20) + "Strength".ljust(14) + \
                                             "Speed".ljust(11) + "Two Hands".ljust(12) + "\n" + "=" * 64
                                    print(cadena)
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
                                        cadena = str("{}".format(i)).ljust(10) + str(dict_weapons[i]["name"]).ljust(
                                            27) + str(dict_weapons[i]["strength"]).ljust(11) + \
                                                 str(dict_weapons[i]["speed"]).ljust(11) + str(dict_weapons[i]["two_hand"]).ljust(10)
                                        print(cadena)
                                if opc == 5:
                                    print("go back")
                                    opc = 0
                                    flag_listar_wea = False
                    if opc == 3:
                        print("list side")
                    if opc == 4:
                        print("list range")
                    if opc == 5:
                        print("go back")
                        opc = 0
                        flag_listar = False
        if opc == 5:
            print("salir")
            flag = False