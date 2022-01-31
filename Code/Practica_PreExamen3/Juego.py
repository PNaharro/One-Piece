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
            A = []
            for h in range(len(Dicionarios.dict_crews)):
                lista.append(Dicionarios.dict_crews[h+1]["members"])

            for j in range(len(lista)):
                for h in lista[j]:
                    for i in range(len(Dicionarios.dict_characters)):
                        if h == i:
                            if len(n) == len(lista[j]):
                                A.append(n)
                                A.clear()
                            n.append(Dicionarios.dict_characters[i]["name"])
            print(A)
            for i in Dicionarios.dict_crews:
                Cadena = str(i).ljust(18) + str(Dicionarios.dict_crews[i]["name"]).ljust(47) + str(lista[i-1])
                print(Cadena)
        if opc == 2:
            print()

juego()


