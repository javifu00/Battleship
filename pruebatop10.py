def top_10():
    """
    Lee el documento Basedatos.txt y almacena en una lista los 10 usuarios con el puntaje mas alto
    y los muestra en orden
    """
    print("\n")
    usuarios_top = []
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        usuarios_top.append(y)
    usuarios_top = sorted(usuarios_top, key=lambda x: x[4], reverse=True) #ordena la lista de los usuarios por el puntaje
    print(Fore.LIGHTRED_EX, " "*70, "TOP 10", Fore.RESET)
    usuarios = []
    for x in usuarios_top: #se almacenaran solo los 10 primeros usuarios en otra lista y se mostraran
        usuarios.append(x)
        if len(usuarios) <= 10:
            print(Fore.LIGHTMAGENTA_EX + " "*58, x[0], "-"*5 + ">", x[4] +"pts", "--" + x[5], "disparos" + Fore.RESET)
        else: break
    print("\n")

top_10()