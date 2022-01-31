import Def
import Dicionarios
########
menu_lista ="list characters","list Weapons","list side","lista range","go back"
menu_opc = "List by id ","List by name","List by strength","List by speed","go back"
def List():
    while True:
        print(Def.Cabecera("List"))
        opc = Def.Inicio(menu_lista)
        if opc == 1:
            while True:
                print(Def.getHeader("list characters"))
                opc = Def.menu(menu_opc)
                if opc == 1:
                    print(Def.headerDictCharactersTable(("Id","Name","Strength","Speed","Experience"),(0,21,28,28,25),"List by id"))
                    for i in Dicionarios.dict_characters:
                        cadena = str(i).ljust(19) + str(Dicionarios.dict_characters[i]["name"]).ljust(24) + str(
                            Dicionarios.dict_characters[i]["strength"]).ljust(31) + \
                                 str(Dicionarios.dict_characters[i]["speed"]).ljust(20) + \
                                 str(Dicionarios.dict_characters[i]["experience"]).ljust(25)
                        print(cadena)
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 2:
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_characters, orden="des", key="name")
                    Def.dictCharactersTable(lista, Dicionarios.dict_characters,
                                        ("Id", "Name", "Strength", "Speed", "Experience"), (0, 21, 28, 28, 25),
                                        "List by name", key="name")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 3:
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_characters, orden="des", key="strength")
                    Def.dictCharactersTableFuerza(lista, Dicionarios.dict_characters,
                                            ("Id", "Name", "Strength", "Speed", "Experience"), (0, 21, 28, 28, 25),
                                            "List by strength", key="strength")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 4:
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_characters, orden="des", key="speed")
                    Def.dictCharactersTablevelocidad(lista, Dicionarios.dict_characters,
                                                  ("Id", "Name", "Strength", "Speed", "Experience"),
                                                  (0, 21, 28, 28, 25),
                                                  "List by speed", key="speed")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 5:
                    print("go back ....")
                    opc = 0
                    break
        if opc == 2:
            while True:
                print(Def.getHeader("list Weapons"))
                opc = Def.menu(menu_opc)
                if opc == 1:
                    print(Def.headerDictCharactersTable(("Id", "Name", "Strength", "Speed", "Two Hand"),
                                                        (0, 21, 28, 30, 25), "List by id"))
                    for i in Dicionarios.dict_weapons:
                        cadena = str(i).ljust(19) + str(Dicionarios.dict_weapons[i]["name"]).ljust(24) + str(
                            Dicionarios.dict_weapons[i]["strength"]).ljust(31) + \
                                 str(Dicionarios.dict_weapons[i]["speed"]).ljust(20) + \
                                 str(Dicionarios.dict_weapons[i]["two_hand"]).ljust(25)
                        print(cadena)
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 2:
                    print(Def.getHeader("List by name"))
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_weapons, orden="des", key="name")
                    Def.dictWeaponsTable(lista, Dicionarios.dict_weapons,
                                            ("Id", "Name", "Strength", "Speed", "two hand"), (0, 21, 28, 20, 33),
                                            "List by name", key="name")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 3:
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_weapons, orden="des", key="strength")
                    Def.dictWeaponsTableFuerza(lista, Dicionarios.dict_weapons,
                                         ("Id", "Name", "Strength", "Speed", "two hand"), (0, 21, 28, 20, 33),
                                         "List by strength", key="strength")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 4:
                    lista = Def.ordenar_dict_dict_key(Dicionarios.dict_weapons, orden="des", key="speed")
                    Def.dictWeaponsTableVelocidad(lista, Dicionarios.dict_weapons,
                                               ("Id", "Name", "Strength", "Speed", "two hand"), (0, 21, 28, 20, 33),
                                               "List by speed", key="speed")
                    print("pulsa cualquir tecla para volver al menu")
                    input()
                if opc == 5:
                    print("go back ....")
                    opc = 0
                    break
        if opc == 3:
            while True:
                print(Def.getHeader("list side"))
                opc = Def.menu(menu_opc)
                if opc == 1:
                    print(Def.getHeader("List by id"))
                    opc = Def.menu(menu_opc)
                if opc == 2:
                    print(Def.getHeader("List by name"))
                    opc = Def.menu(menu_opc)
                if opc == 3:
                    print(Def.getHeader("List by strength"))
                    opc = Def.menu(menu_opc)
                if opc == 4:
                    print(Def.getHeader("List by speed"))
                    opc = Def.menu(menu_opc)
                if opc == 5:
                    print("go back ....")
                    opc = 0
                    break
        if opc == 4:
            while True:
                print(Def.getHeader("lista range"))
                opc = Def.menu(menu_opc)
                if opc == 1:
                    print(Def.getHeader("List by id"))
                    opc = Def.menu(menu_opc)
                if opc == 2:
                    print(Def.getHeader("List by name"))
                    opc = Def.menu(menu_opc)
                if opc == 3:
                    print(Def.getHeader("List by strength"))
                    opc = Def.menu(menu_opc)
                if opc == 4:
                    print(Def.getHeader("List by speed"))
                    opc = Def.menu(menu_opc)
                if opc == 5:
                    print("go back ....")
                    opc = 0
                    break
        if opc == 5:
            print("go back ....")
            break
