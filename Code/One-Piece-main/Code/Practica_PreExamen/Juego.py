import Def
import Dicionarios
#####################
menu = "Crew vs Crew","Crew vs Rank"
#######################
def juego():
    lista = []
    while True:
        print(Def.getHeader("Jugar"))
        opc = Def.menu(menu)
        if opc == 1:
            print(Def.getHeaderForTableFromTuples2(("Id","Crew","Members"),(0,20,50),""))
            lista = []
            n =[]
            for h in range(len(Dicionarios.dict_crews)):
                lista.append(Dicionarios.dict_crews[h+1]["members"])
            for h in range(len(lista)):
                for j in lista[h]:
                    for i in range(len(Dicionarios.dict_characters)):
                        if j == i:
                            n.append(Dicionarios.dict_characters[i]["name"])
            for i in Dicionarios.dict_crews:
                Cadena = str(i).ljust(18) + str(Dicionarios.dict_crews[i]["name"]).ljust(47) + str(lista[i-1])
                print(Cadena)
        if opc == 2:
            print()

juego()


