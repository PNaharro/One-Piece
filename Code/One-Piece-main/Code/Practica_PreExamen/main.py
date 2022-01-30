#### imports #####
import Dicionarios
import Def
import Creacion
import List
import Juego
import Editar
import random

#### Menus ####
Menu_principal = ("Play","Create","edit","list","exit")
while True:
    print(Def.Cabecera("One Piece"))
    opc = Def.Inicio(Menu_principal)
    if opc == 1:
        Juego.juego()
    if opc == 2:
        Creacion.Creacion()
    if opc == 3:
        Editar.editar()
    if opc == 4:
        List.List()
    if opc == 5:
        print("Exit...")
        break