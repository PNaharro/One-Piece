import Def
import Dicionarios
import random
#################################################
menu = "Edit Character","Edit weapon","Go back"
menu_add_arma = "add Weapon \n Weapon Id) to add weapon Id \n 0) finish Weapon\n Weapon Id) delete weapon"
#################################################
arma = []
weapon = []
weapon_num = []
Fuerza = []
veloz = []
hands = []
################################################
def editar():
    while True:
        print(Def.Cabecera("Editar"))
        opc = Def.Inicio(menu)
        if opc == 1:
            print(Def.getHeader("Editar Personajes"))
            for i in Dicionarios.dict_characters:
                armas = []
                for j in Dicionarios.dict_characters[i]["weapons"]:
                    armas.append(Dicionarios.dict_weapons[j]["name"])
                cadena = "ID: {},Nombre: {}, Categoria: {}, Armas: {}, Fuerza: {}, Velocidad: {}, Experiencia: {}" \
                    .format(i,Dicionarios.dict_characters[i]["name"], Dicionarios.dict_characters[i]["category"], armas,
                            Dicionarios.dict_characters[i]["strength"], Dicionarios.dict_characters[i]["speed"],
                            Dicionarios.dict_characters[i]["experience"])
                print(cadena)
            ID = Def.IdPersonaje()
            ED = Def.opcionED(ID)
            if ED == 1:
                while True:
                    nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                    nwnombre = nwnombre.capitalize()
                    if not nwnombre.isalpha():
                        print("Valor no valido")
                    elif not len(nwnombre) < 20:
                        print("El nombre es demasiado largo")
                    elif not len(nwnombre) > 0:
                        print("El nombre es demasiado corto")
                    else:
                        break
                opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                    Dicionarios.dict_characters[ID]["name"], nwnombre))
                if opcion == "S" or opcion == "s":
                    Dicionarios.dict_characters[ID]["name"] = nwnombre
                    print("Nombre Actualizado")
            elif ED == 2:
                Flag = True
                while Flag:
                    print("=" * 8 + "Avalible Weapon" + "=" * 8)
                    if len(arma) == 0:
                        for i in range(len(Dicionarios.dict_weapons)):
                            cadena = str(i + 1) + ") " + Dicionarios.dict_weapons[i + 1]["name"] + ", strength: " + str(
                                Dicionarios.dict_weapons[i + 1]["strength"]) \
                                     + ", speed: " + str(Dicionarios.dict_weapons[i + 1]["speed"])
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
                            for i in range(len(Dicionarios.dict_weapons)):
                                a = Dicionarios.dict_weapons[i + 1]["two_hand"]
                                if a == False:
                                    cadena = str(i + 1) + ") " + Dicionarios.dict_weapons[i + 1][
                                        "name"] + ", strength: " + str(
                                        Dicionarios.dict_weapons[i + 1]["strength"]) \
                                             + ", speed: " + str(Dicionarios.dict_weapons[i + 1]["speed"])
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

                    if not opc_arma.isdigit() and (len(opc_arma) <= 1):
                        print("opcion incorecta 1")

                    elif int(opc_arma) > len(Dicionarios.dict_weapons):
                        print("opcion incorecta 5")

                    elif len(arma) >= 2 and opc_arma != "0":
                        print("no se pueden añadir mas armas")

                    elif len(arma) == 1 and hands[0] == True and opc_arma != "0":
                        print("no se pueden llebar mas armas")

                    elif len(opc_arma) > 1:
                        if not opc_arma[0] == "-":
                            print("opcion incorecta")
                        elif not opc_arma[1].isdigit():
                            print("opcion incorecta")

                        elif int(opc_arma[1]) > len(Dicionarios.dict_weapons):
                            print("opcion incorecta")

                        if opc_arma[0] == "-" or opc_arma[1].isdigit():
                            print("")
                    else:
                        opc_arma = int(opc_arma)

                    if opc_arma == 0:
                        F = random.randrange(1, 9)
                        S = random.randrange(1, 9)
                        cadena = "Name: " + Dicionarios.dict_characters[ID]["name"] + "\nWeapons: " + str(
                            weapon)[3:-3] + "\nStrength: " + str(F) + "\nSpeed: " + str(S) \
                                 + "\nTipo de empuñadura: " + str(hands)[1:-1] + "\nExperiens: " + "0"
                        print(cadena)
                        while True:
                            opc_acep = input("guarda arma s/n ")
                            if opc_acep == "s" or opc_acep == "S":
                                cadena ="name:",Dicionarios.dict_characters[ID]["name"],"category:", Dicionarios.dict_characters[ID]["category"],\
                                                                "weapons", weapon_num,\
                                                                "strength", F,\
                                                                "speed", S,\
                                                                "experience", "0"
                                print(cadena)
                                Dicionarios.dict_characters[ID] = {"name": Dicionarios.dict_characters[ID]["name"],
                                                                "category": Dicionarios.dict_characters[ID]["category"],
                                                                "weapons": weapon_num,
                                                                "strength": F,
                                                                "speed": S,
                                                                "experience": "0"}
                                arma.clear()
                                weapon.clear()
                                Fuerza.clear()
                                veloz.clear()
                                hands.clear()
                                print(cadena)
                                Flag = False
                                break
                            if opc_acep == "n" or opc_acep == "N":
                                print("no se ha guardado")
                                flag = False
                                break
                            else:
                                print("opcion incorecta")

                    elif opc_arma in Dicionarios.dict_weapons:
                        cadena = str(opc_arma) + ") " + Dicionarios.dict_weapons[opc_arma]["name"] + ", strength: " + str(
                            Dicionarios.dict_weapons[opc_arma]["strength"]) \
                                 + ", speed: " + str(Dicionarios.dict_weapons[opc_arma]["speed"])
                        arma.append(cadena + "\n")
                        weapon.append([Dicionarios.dict_weapons[opc_arma]["name"]])
                        weapon_num.append(int(opc_arma))
                        Fuerza.append(Dicionarios.dict_weapons[opc_arma]["strength"])
                        veloz.append(Dicionarios.dict_weapons[opc_arma]["speed"])
                        hands.append(Dicionarios.dict_weapons[opc_arma]["two_hand"])

                    elif opc_arma[0] == "-":
                        if int(opc_arma[1]) in Dicionarios.dict_weapons:
                            if len(arma) != 0:
                                cadena = str(opc_arma[1:]) + ") " + Dicionarios.dict_weapons[int(opc_arma[1:])][
                                    "name"] + ", strength: " + str(Dicionarios.dict_weapons[int(opc_arma[1:])]["strength"]) \
                                         + ", speed: " + str(Dicionarios.dict_weapons[int(opc_arma[1:])]["speed"])
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
            elif ED == 3:
                break
        if opc == 2:
            print(Def.getHeader("Editr arma"))
            for i in Dicionarios.dict_weapons:
                cadena = "{}) {}, Fuerza: {}, Velocidad: {}".format(i, Dicionarios.dict_weapons[i]["name"],
                            Dicionarios.dict_weapons[i]["strength"],Dicionarios.dict_weapons[i]["speed"])
                print(cadena)

            ID = Def.IdArma()
            ED = Def.opcED(ID)
            if ED == 1:
                while True:
                    # Introducir nuevo nombre
                    nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                    nwnombre = nwnombre.capitalize()
                    if not nwnombre.isalpha():
                        print("Valor no valido")
                    elif not len(nwnombre) < 20:
                        print("El nombre es demasiado largo")
                    elif not len(nwnombre) > 0:
                        print("El nombre es demasiado corto")
                    else:
                        break
                opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                    Dicionarios.dict_weapons[ID]["name"], nwnombre))
                if opcion == "S" or opcion == "s":
                    Dicionarios.dict_weapons[ID]["name"] = nwnombre
                    print("Nombre Actualizado")
            elif ED == 2:
                while True:
                    # Introducir nueva Fuerza
                    nwfuerza = input("Introduce la nueva fuerza (9 Max):\n")
                    if not nwfuerza.isdigit():
                        print("Valor no valido")
                    elif not int(nwfuerza) < 10:
                        print("Demasiada fuerza")
                    elif not int(nwfuerza) > 0:
                        print("Poca fuerza")
                    else:
                        break
                opcion = input("Estas seguro de que quieres cambiar la fuerza de {} a {}?(S/N)".format(
                    Dicionarios.dict_weapons[ID]["strength"], nwfuerza))
                if opcion == "S" or opcion == "s":
                    Dicionarios.dict_weapons[ID]["strength"] = nwfuerza
                    print("Fuerza Actualizada")
            elif ED == 3:
                while True:
                    # Introducir nueva Velocidad
                    nwvelocidad = input("Introduce la nueva velocidad (9 Max):\n")
                    if not nwvelocidad.isdigit():
                        print("Valor no valido")
                    elif not int(nwvelocidad) < 10:
                        print("Demasiada velocidad")
                    elif not int(nwvelocidad) > 0:
                        print("Poca velocidad")
                    else:
                        break
                opcion = input("Estas seguro de que quieres cambiar la velocidad de {} a {}?(S/N)".format(
                    Dicionarios.dict_weapons[ID]["speed"], nwvelocidad))
                if opcion == "S" or opcion == "s":
                    Dicionarios.dict_weapons[ID]["speed"] = nwvelocidad
                    print("Velocidad Actualizada")
            elif ED == 4:
                break
        if opc == 3:
            break

