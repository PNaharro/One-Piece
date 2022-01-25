#### imports #####
import Def
import Creacion
import Juego

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
        print("3")
    if opc == 4:
        print("4")
    if opc == 5:
        print("Exit...")
        break