import Def
import random
import Dicionarios
def Creacion():
    ##########
    Menu_Creacion = ("Create character", "create Weapon", "go back")
    menu_band = ("marina", "piratas")
    menu_rango_man = ("Admiral", "ViceAdmiral", "Lieutenant")
    menu_rango_pir = ("Straw hat", "Pirates Buggy", "Pirates Rocks")
    menu_add_arma = "add Weapon \n Weapon Id) to add weapon Id \n 0) finish Weapon\n Weapon Id) delete weapon"
    ##########
    arma = []
    weapon = []
    weapon_num = []
    strength = []
    speed = []
    hands = []
    ##########
    flag = True
    ##########
    while True:
        print(Def.getHeader("Creacion"))
        opc = Def.menu(Menu_Creacion)
        if opc == 1:
            print("Create character")
            nombre_ch = input("introduce el nombre del personaje: ")
            while True:
                print(Def.getHeader("Elige Band"))
                opc = Def.menu(menu_band)
                if opc == 1:
                    bando = "Marines"
                    print(Def.getHeader("Marines"))
                    while True:
                        rango= Def.menu(menu_rango_man)
                        if (rango + 3) in Dicionarios.dict_categorys:
                            rank = Dicionarios.dict_categorys[rango + 3]
                            rank_num = rango + 3
                            print(rank)
                            break
                    break
                if opc == 2:
                    bando = "piratas"
                    print(Def.getHeader("Piratas"))
                    while True:
                        rango = Def.menu(menu_rango_pir)
                        if rango in Dicionarios.dict_categorys:
                            rank = Dicionarios.dict_categorys[rango]
                            rank_num = rango
                            print(rank)
                            break
                    break
            while flag:
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
                    print(hands)
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
                    cadena = "Name: " + nombre_ch + "\nCategori: " + str(rank) + "\nWeapons: " + str(
                        weapon)[3:-3].strip("'],['") + "\nStrength: " + str(F) + "\nSpeed: " + str(S) \
                             + "\nTipo de empuñadura: " + str(hands)[1:-1] + "\nExperiens: " + "0"
                    print(cadena)
                    while True:
                        opc_acep = input("guarda arma s/n ")
                        if opc_acep == "s" or opc_acep == "S":
                            Dicionarios.dict_characters[len(Dicionarios.dict_characters) + 1] = {"name": nombre_ch, "category": rank_num,
                                                                         "weapons": weapon_num, "strength": F,
                                                                         "speed": S, "experience": "0"}
                            arma.clear()
                            weapon.clear()
                            strength.clear()
                            speed.clear()
                            hands.clear()
                            Flag = False
                            return
                        if opc_acep == "n" or opc_acep == "N":
                            print("no se ha guardado")
                            flag= False
                            return
                        else:
                            print("opcion incorecta")

                elif opc_arma in Dicionarios.dict_weapons:
                    cadena = str(opc_arma) + ") " + Dicionarios.dict_weapons[opc_arma]["name"] + ", strength: " + str(
                        Dicionarios.dict_weapons[opc_arma]["strength"]) \
                             + ", speed: " + str(Dicionarios.dict_weapons[opc_arma]["speed"])
                    arma.append(cadena + "\n")
                    weapon.append([Dicionarios.dict_weapons[opc_arma]["name"]])
                    weapon_num.append(opc_arma)
                    strength.append(Dicionarios.dict_weapons[opc_arma]["strength"])
                    speed.append(Dicionarios.dict_weapons[opc_arma]["speed"])
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
        if opc == 2:
            print("Create weapon")
            flag_speed = True
            flag_tipoArma = True
            nombre = input("introduce el nombre del arma: ")
            strength = Def.Fuerza()
            speed = Def.Speed()
            two_hand = Def.enpuñadura()
            cadana2 = "Name: " + nombre + "\nStrength: " + str(strength) + "\nSpeed: " + str(
                speed) + "\nDos Manos: " + str(two_hand)
            print(cadana2)
            while True:
                opc_acep = input("guarda arma s/n ")
                if opc_acep == "s" or opc_acep == "S":
                    Dicionarios.dict_weapons[len(Dicionarios.dict_weapons) + 1] = {"name": nombre, "strength": int(strength),
                                                           "speed": int(speed), "two_hand": two_hand}
                    print(Dicionarios.dict_weapons)
                    break
                if opc_acep == "n" or opc_acep == "N":
                    print("no se ha guardado")

                    break
                else:
                    print("opcion incorecta")
        if opc == 3:
            print("Back ...")
            break
