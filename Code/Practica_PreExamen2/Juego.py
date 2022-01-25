import Def
import Dicionarios
##################
def juego():
    tupla = ("Crew vs Crew","Crew vs Rank")
    print(Def.getHeader("Elige"))
    opc = Def.Menu(tupla)
    if opc == 1:
        print(Def.getHeadeForTableFromTuples(("Id","Crew","Membres"), (0, 20, 40), ""))
    if opc == 2:
        print(Def.getHeadeForTableFromTuples(("Id", "Crew", "Membres"), (0, 20, 40), ""))
