from Usuario import Usuario
from random import randint
from Naves import Portaviones, Fragata, Submarinos
from time import sleep
from colorama import Fore
#valores para crear los barcos
tablero = []
numero_filas = 10
numero_columnas = 10
orientaciones = ("Vertical", "Horizontal")
lista_ubicacion_barco = []  
lista_temporal = []
coordenadas_portaviones = []
coordenadas_fragata = []
coordenadas_submarinos = []
#valores para llevar el conteo de los disparos
disparos_elegidos = []
disparos_efectuados = 0
disparos_acertados = 0
disparos_fallidos = 0
disparos_repetidos = 0
#listas de estadisticas
lista_usuarios = []
lista_ranking = []
usuario_partida = []
lista_top_10 = []

def datos_usuario():
    usuario_partida.clear()
    puntaje = 0
    disparos_efectuados = 100
    username = input("Ingrese su username: ")
    usuarios = []
    nombre_lista = []
    username_repetido = True
    while username_repetido:
        with open("BaseDatos.txt", "r") as bd:
            datos = bd.readlines()
        for x in datos:
            usuario = x[:-1].split(',') # [:-1] para quitar el salto de linea
            usuarios.append(usuario[0])
            if username in usuarios:
                print("Veo que ya has jugado antes, gracias por volver :)\n")
                sleep(2)
                username = usuario[0]
                nombre = usuario[1].split(" ")
                nombre = nombre[1].title()
                edad = usuario[2].split(" ")
                edad = edad[1]
                genero = usuario[3].split(" ")
                genero = genero[1]
                puntaje = usuario[4].split(" ")
                puntaje = puntaje[1]
                disparos_efectuados = usuario[5].split(" ")
                disparos_efectuados = disparos_efectuados[1]
                usuario_partida.append(username)
                with open("Basedatos.txt", "r") as db:
                    lineas = db.readlines()
                with open("Basedatos.txt", "w") as db:
                    for linea in lineas:
                        if username not in linea:
                            db.write(linea) 
                with open("Basedatos.txt", "a") as bd: 
                    bd.write("{}, {}, {}, {}, {}, {}\n".format(username, nombre, edad, genero, puntaje, disparos_efectuados))
                return Usuario(username, nombre, edad, genero, puntaje, disparos_efectuados)
                username_repetido = False
        else:
            validacion_username = username.islower()
            while validacion_username == False or len(username) > 30 or " " in username:
                print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
                username = input("Ingerese su username nuevamente: ")
                validacion_username = username.islower()
            usuario_partida.append(username)
            nombre = input("Ingrese su nombre completo: ")
            verificacion_nombre = nombre.replace(" ", "").isalpha()
            while verificacion_nombre == False:
                    print("{}Su nombre solo puede tener letras{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                    nombre = input("Ingrese su nombre completo: ")
                    verificacion_nombre = nombre.replace(" ", "").isalpha()
            nombre = nombre.title()
            while True: #Validacion para edad
                try:
                    edad = int(input("Ingresa su edad: "))
                    if edad < 5 or edad > 100:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}Tu edad no es adecuada para jugar{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            while True: #Validacion para genero
                try:
                    genero = int(input("Ingrese su genero: \n1) Femenino \n2) Masculino \n3) Ninguno\n"))
                    if genero < 1 or genero > 3:
                        raise  ValueError
                    if genero == 1:
                        genero = "Femenino"
                    elif genero == 2: 
                        genero = "Masculino"
                    elif genero == 3:
                        genero = "Ninguno"
                    break
                except ValueError:
                    print("{}El valor ingresado no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            with open("Basedatos.txt", "a+") as bd: 
                bd.write("{}, {}, {}, {}, {}, {}\n".format(username, nombre, edad, genero, puntaje, disparos_efectuados))
            return Usuario(username, nombre, edad, genero, puntaje, disparos_efectuados)
            username_repetido = False

def crear_tablero(tablero): 
    for x in range(numero_filas):
        completar_tablero = ["O"] * numero_columnas
        tablero.append(completar_tablero) 
    return tablero

def mostrar_tablero(tablero):
    numeros_de_fila = []
    for x in range(1, numero_columnas+1):
        y = str(x)
        numeros_de_fila.append(y)
    print("   " + " ".join(numeros_de_fila))
    for w in range(numero_columnas):
        if w < 9:
            print(str(w + 1) + "  " + " ".join(str(x) for x in tablero[w]))
        else: print(str(w + 1) + " " + " ".join(str(x) for x in tablero[w]))
    print("\n")

#definiciones para comenzar el juego
def ubicar_portaviones():
    tamano = Portaviones.tamano
    cantidad = Portaviones.cantidad
    orientacion = orientaciones[(randint(0, 1))]
    while cantidad > 0:
        if orientacion == "Vertical":
            coor_fila = randint(1, numero_filas)
            coor_columna = randint(1, numero_columnas)
            while (coor_fila + tamano) > 10:
                coor_fila = randint(1,numero_filas)
            ubicacion = (coor_fila, coor_columna)
            lista_temporal.append(ubicacion)
            while len(lista_temporal) < tamano:
                coor_fila += 1
                ubicacion = (coor_fila, coor_columna)
                lista_temporal.append(ubicacion)
            cantidad -= 1
        elif orientacion == "Horizontal":
            coor_fila = randint(1, numero_filas)
            coor_columna = randint(1, numero_columnas)
            while (coor_columna + tamano) > 10:
                coor_columna = randint(1, numero_columnas)
            ubicacion = (coor_fila, coor_columna)
            lista_temporal.append(ubicacion)
            while len(lista_temporal) < tamano:
                coor_columna += 1
                ubicacion = (coor_fila, coor_columna)
                lista_temporal.append(ubicacion)
        for x in lista_temporal:
            lista_ubicacion_barco.append(x)
            coordenadas_portaviones.append(x)
        lista_temporal.clear()
        cantidad -= 1

def ubicar_fragata():
    tamano = Fragata.tamano
    cantidad = Fragata.cantidad
    orientacion = orientaciones[(randint(0, 1))]
    seguir_coordenadas = True
    while seguir_coordenadas:
        mal_ubicado = "no"
        if orientacion == "Vertical":
            coor_fila = randint(1, numero_filas)
            coor_columna = randint (1, numero_columnas)
            while (coor_fila + tamano) > 10:
                coor_fila = randint(1,numero_filas)
            ubicacion = (coor_fila, coor_columna)
            lista_temporal.append(ubicacion)
            while len(lista_temporal) < tamano:
                coor_fila += 1
                ubicacion = (coor_fila, coor_columna)
                lista_temporal.append(ubicacion)
            for x in lista_ubicacion_barco:
                for y in lista_temporal:
                    if x == y:
                        mal_ubicado = "si"
                    elif (y[0] == x[0] or (y[0]+1) == x[0] or (y[0]-1) == x[0]) and ((y[1]) == x[1] or (y[1]+1) == x[1] or (y[1]- 1) == x[1]):
                        mal_ubicado = "si"
        if orientacion == "Horizontal":
            coor_fila = randint(1, numero_filas)
            coor_columna = randint(1, numero_columnas)
            while (coor_columna + tamano) > 10:
                coor_columna = randint(1, numero_columnas)
            ubicacion = (coor_fila, coor_columna)
            lista_temporal.append(ubicacion)
            while len(lista_temporal) < tamano:
                coor_columna += 1
                ubicacion = (coor_fila, coor_columna)
                lista_temporal.append(ubicacion)
            for x in lista_ubicacion_barco:
                for y in lista_temporal:
                    if x == y:
                        mal_ubicado = "si"
                    elif (y[0] == x[0] or (y[0]+1) == x[0] or (y[0]-1) == x[0]) and ((y[1]) == x[1] or (y[1]+1) == x[1] or (y[1]- 1) == x[1]):
                        mal_ubicado = "si"
        if mal_ubicado == "si":
            seguir_coordenadas = True
            lista_temporal.clear()
        elif mal_ubicado == "no": 
            for x in lista_temporal:
                # lista_ubicacion_barco.append(x)
                coordenadas_fragata.append(x)
            lista_temporal.clear()
            seguir_coordenadas = False

def ubicar_submarino():
    tamano = Submarinos.tamano
    cantidad = Submarinos.cantidad
    while cantidad > 0:
        mal_ubicado = "no"
        coor_fila = randint(1,numero_filas)
        coor_columna = randint(1,numero_columnas)
        ubicacion = (coor_fila, coor_columna)
        for x in lista_ubicacion_barco:
            if x == ubicacion:
                mal_ubicado = "si"
            elif (ubicacion[0] == x[0] or (ubicacion[0]+1) == x[0] or (ubicacion[0]-1) == x[0]) and ((ubicacion[1]) == x[1] or (ubicacion[1]+1) == x[1] or (ubicacion[1]- 1) == x[1]):
                mal_ubicado = "si"
        if mal_ubicado == "no":
            cantidad -= 1
            # lista_ubicacion_barco.append(ubicacion)
        elif mal_ubicado == "si":
            cantidad = cantidad

def ubicar_naves():
    tablero.clear()
    crear_tablero(tablero)
    ubicar_portaviones()
    ubicar_fragata()
    ubicar_submarino()

def juego():
    ubicar_naves()
    global disparos_acertados, disparos_efectuados, disparos_elegidos, disparos_fallidos, disparos_repetidos
    disparos_efectuados = 0
    disparos_acertados = 0
    disparos_fallidos = 0
    disparos_repetidos = 0
    puntaje = 0
    for x in usuario_partida:
        usuario = x
    print("¿Estas listo para jugar {}? eso espero porque no hay vuelta atras\nCargando........ :/\n".format(usuario))
    sleep(3)
    mostrar_tablero(tablero)
    while len(lista_ubicacion_barco) > 0:
        while True:
            try:
                elegir_fila = int(input("Ingresa una fila: "))
                if elegir_fila < 1 or (elegir_fila >10 and elegir_fila != 24):
                    raise  ValueError
                break
            except ValueError:
                print("{}No existe dicha fila{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        # validar_fila = elegir_fila.isdigit()
        while True:
            try:
                elegir_columna = int(input("Ingresa una columna: "))
                if elegir_columna < 1 or (elegir_columna >10):
                    raise  ValueError
                break
            except ValueError:
                print("{}No existe dicha fila{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        tiro_elegido = (elegir_fila, elegir_columna)
        if tiro_elegido[0] == 24:
            print("Has accedido a un cheat code, los barcos estan en: ",lista_ubicacion_barco)
        elif tiro_elegido in disparos_elegidos:
            print("Este disparo ya lo has hecho antes :|")
            disparos_repetidos += 1
        elif tiro_elegido in lista_ubicacion_barco:
            disparos_elegidos.append(tiro_elegido)
            print("Has acertado\n")
            tablero[elegir_fila - 1][elegir_columna - 1] = "{}F{}".format(Fore.RED, Fore.RESET)
            lista_ubicacion_barco.remove(tiro_elegido)
            disparos_efectuados += 1
            disparos_acertados += 1
            puntaje += 10
            if tiro_elegido in coordenadas_portaviones:
                coordenadas_portaviones.remove(tiro_elegido)
                if len(coordenadas_portaviones) == 0:
                    print("Felicitaciones has hundido el portaviones, su ataque aereo quedo neutralizado\n")
            elif tiro_elegido in coordenadas_fragata:
                coordenadas_fragata.remove(tiro_elegido)
                if len(coordenadas_fragata) == 0:
                    print("Felicitaciones has hundido la Fragata, su comunicacion con tierra ha sido detenida\n")
            elif tiro_elegido in coordenadas_submarinos:
                coordenadas_submarinos.remove(tiro_elegido)
                if len(coordenadas_submarinos) == 0:
                    print("Felicitaciones has hundido los submarinos\n")
        else:
            disparos_elegidos.append(tiro_elegido)
            print("Has fallado\n")
            tablero[elegir_fila - 1][elegir_columna - 1] = "{}X{}".format(Fore.BLUE, Fore.RESET)
            disparos_efectuados += 1
            disparos_fallidos += 1
            puntaje -= 2
        mostrar_tablero(tablero)
    disparos_elegidos.clear()
    print("{}Ese disparo me ha dolido.{} Has logrado hundir toda mi flota :(".format(Fore.RED, Fore.RESET))
    sleep(1)
    if disparos_efectuados == 9:
        print("¿Eres un robot? lo que acabas de hacer es poco probable... ¿viste los cheat codes verdad?")
    elif disparos_efectuados < 45:
        print("Excelente estrategia")
    elif disparos_efectuados >= 45 and disparos_efectuados <= 70:
        print("Buena estrategia, pero hay que mejorar(o buscar los cheat codes)")
    elif disparos_efectuados > 70:
        print("{}Considérese Perdedor, tiene que mejorar{}".format(Fore.RED, Fore.RESET))
    sleep(0.7)
    print("\nCargando tus estadisticas :| .......... pssss deberias probar el numero de kobe en fila\n")
    sleep(2.5)
    for x in usuario_partida:
        print("{}{} tus estadisticas fueron las siguientes:{}".format(Fore.YELLOW,x, Fore.RESET))
    print("Disparos realizados = {}".format(disparos_efectuados))
    print("Puntaje total = {}".format(puntaje))
    print("Disparos repetidos = {}".format(disparos_repetidos))
    print("Tu tablero quedo asi:")
    mostrar_tablero(tablero)
    for x in usuario_partida:
        y = x
    with open("Basedatos.txt", "r") as bd:
        punto = []
        datos = bd.readlines()
    nuevo_valor = ""
    for x in datos:
        if y in x:
            index = datos.index(x)
            puntos = x[:-1].split(",")
            if int(puntos[4]) < puntaje:
                puntos[4] = " {}".format(puntaje)
            if int(puntos[5]) > disparos_efectuados:
                puntos[5] = " {}".format(disparos_efectuados)
    for x in range(len(puntos)):
        if x != len(puntos) - 1:
            nuevo_valor += puntos[x] + ","
        else:
            nuevo_valor += puntos[x] + "\n"
    datos[index] = nuevo_valor
    with open("Basedatos.txt", "w") as bd:
        bd.writelines(datos)

def top_10():
    print("\n")
    usuarios_top = []
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        usuarios_top.append(y)
    usuarios_top = sorted(usuarios_top, key=lambda x: x[4], reverse=True)
    print(Fore.LIGHTRED_EX, " "*70, "TOP 10", Fore.RESET)
    usuarios = []
    for x in usuarios_top:
        usuarios.append(x)
        if len(usuarios) <= 10:
            print(Fore.LIGHTMAGENTA_EX + " "*60, x[0], "-"*5 + ">", x[4] +"pts", "--" + x[5], "disparos" + Fore.RESET)
        else: break
    print("\n")

def puntos_genero():
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    genero = []
    masculinos = []
    femeninos = []
    ninguno = []
    puntos_masculinos = 0
    puntos_femeninos = 0
    puntos_ninguno = 0
    for x in datos:
        genero = x[:-1].split(",")
        genero[4] = int(genero[4]) 
        if genero[3] == " Masculino":
            puntos_masculinos += genero[4]
        elif genero[3] == " Femenino":
            puntos_femeninos += genero[4]
        elif genero[3] == " Ninguno":
            puntos_ninguno += genero[4]
    print("Los puntos totales por usuarios masculinos son: {}".format(puntos_masculinos))
    print("Los puntos totales por usuarios femeninos son: {}".format(puntos_femeninos))
    print("Los puntos totales por usuarios que decidieron no especificar su genero son: {}".format(puntos_ninguno))

def usuarios_edades():
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    lista_max_edades = []
    lista_ninos = []
    lista_adultos = []
    lista_pures = []
    lista_viejos = []
    for x in datos:
        edades = x[:-1].split(",")
        edad = int(edades[4])
        if edad >= 5 and edad <= 18:
            lista_ninos.append(edades)
        elif edad >= 19 and edad <= 45:
            lista_adultos.append(edades)
        elif edad >= 46 and edad <= 60:
            lista_pures.append(edades)
        elif edad >= 61 and edad <= 100:
            lista_viejos.append(edades)
    cantidad_ninos = len(lista_ninos)
    lista_max_edades.append(str(cantidad_ninos))
    cantidad_adultos = len(lista_adultos)
    lista_max_edades.append(str(cantidad_adultos))
    cantidad_pures = len(lista_pures)
    lista_max_edades.append(str(cantidad_pures))
    cantidad_viejos = len(lista_viejos)
    lista_max_edades.append(str(cantidad_viejos))
    maximo = max(lista_max_edades)
    rango = ""
    if int(maximo) == cantidad_ninos:
        rango = "5 - 18"
    elif int(maximo) == cantidad_adultos:
        rango = "19 - 45"
    elif int(maximo) == cantidad_pures:
        rango = "46 - 60"
    elif int(maximo) == cantidad_viejos:
        rango = " 61 - 100"
    print("Los usuarios que mas juegan estan entre las edades de {} años".format(rango))

def promedio_disparos():
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    disparos_totales = 0
    lista_disparos = []
    for x in datos:
        lista = x[:-1].split(",")
        lista_disparos.append(lista)
        disparos_totales += int(lista[5])
    disparos_totales /= len(lista_disparos)
    print("Los disparos totales en promedio para ganar fueron: {}".format(disparos_totales))

def ver(edit = False):
    print("\nEstos son los usuarios registrados actualmente:\n")
    usuarios = []
    with open("BaseDatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        usuario = x[:-1].split(',') # [:-1] para quitar el salto de linea
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]))
    #usuarios = sorted(usuarios, key= lambda user: user.username)
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for n, y in enumerate(usuarios):
        print('='*5, n+1, '='*5)
        print(y)
        print("\n")

def actualizar_datos(elegir):
    print("""
¿Qué dato desea modificar?
1 - Username
2 - Nombre
3 - Edad
4 - Género
Ni el puntaje ni los disparos los puedes cambiar, no seas chiguire
    """)
    eleccion = int(input("Ingrese una opción: "))
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
        user = datos[elegir - 1][:-1].split(",")
    if eleccion == 1:
        user[eleccion - 1] = input("Ahora ingrese su nuevo username: ") 
        validacion_username = user[eleccion - 1].islower()
        while validacion_username == False or len(user[eleccion - 1]) > 30 or " " in user[eleccion - 1]:
            print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
            user[eleccion - 1] = input("Ingerese su username nuevamente: ")
            validacion_username = user[eleccion - 1].islower()
        usuario_partida.clear()
        usuario_partida.append(user[eleccion - 1])
    elif eleccion == 2:
        user[eleccion - 1] = input("Ahora ingrese su nuevo nombre: ")
        verificacion_nombre = user[eleccion - 1].replace(" ", "").isalpha()
        while verificacion_nombre == False:
                print("{}Su nombre solo puede tener letras{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                user[eleccion - 1] = input("Ingrese su nombre completo: ")
                verificacion_nombre = user[eleccion - 1].replace(" ", "").isalpha()
        user[eleccion - 1] = user[eleccion - 1].title()
        user[eleccion - 1] = " " + user[eleccion - 1]  
    elif eleccion == 3:
        while True: #Validacion para edad
            try:
                user[eleccion - 1] = int(input("Ingresa su edad: "))
                if user[eleccion - 1] < 5 or user[eleccion - 1] > 100:
                    raise  ValueError
                break
            except ValueError:
                print("{}Tu edad no es adecuada para jugar{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        user[eleccion - 1] = " " + str(user[eleccion - 1]) 
    elif eleccion == 4:
        while True: #Validacion para genero
                try:
                    user[eleccion - 1] = int(input("Ingrese su genero: \n1) Femenino \n2) Masculino \n3) Ninguno\n"))
                    if user[eleccion - 1] < 1 or user[eleccion - 1] > 3:
                        raise  ValueError
                    if user[eleccion - 1] == 1:
                        user[eleccion - 1] = " Femenino"
                    elif user[eleccion - 1] == 2: 
                        user[eleccion - 1] = " Masculino"
                    elif user[eleccion - 1] == 3:
                        user[eleccion - 1] = " Ninguno"
                    break
                except ValueError:
                    print("{}El valor ingresado no es valido{}".format(Fore.LIGHTRED_EX, Fore.RESET))
    nuevo_valor = ""
    for x in range(len(user)):
        if x != len(user) - 1:
            nuevo_valor += user[x] + ','
        else:
            nuevo_valor += user[x] + '\n'
    datos[elegir - 1] = nuevo_valor
    with open("Basedatos.txt", "w") as bd:
        bd.writelines(datos)

def main():
    top_10()
    print("{}Bienvenido a BATTLESHIP ¿crees tener lo necesario para hundir mi flota?{}".format(Fore.BLUE, Fore.RESET))
    sleep(2)
    print("{}No lo creo JAJAJA{}".format(Fore.RED, Fore.RESET))
    continuar_jugando = True
    while continuar_jugando:
        sleep(1.5)
        print("""
Selecciona lo que quieras hacer
1) Jugar una partida
2) Editar un usuario
3) Ver el leaderboard
4) Ver estadisticas
5) Salir del Juego
""")
        while True:
            try:
                elegir = int(input("{}Ingrese su opcion: {}".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                if elegir < 1 or elegir > 5:
                    raise  ValueError
                break
            except ValueError:
                print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        if elegir == 1:
            print("\n")
            lista_usuarios.append(datos_usuario())
            juego()
            while True: 
                try:
                    seguir = int(input("Ingresa una de las opciones: \n{}1) Volver al menu {}\n{}2) Salir {}\n".format(Fore.LIGHTBLUE_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 2:
            print("\n")
            ver(edit = True)
            seleccion = int(input("Seleccione el usuario que desee actualizar: "))
            actualizar_datos(seleccion)
            while True: 
                try:
                    seguir = int(input("Ingresa una de las opciones: \n{}1) Volver al menu {}\n{}2) Salir {}\n".format(Fore.LIGHTBLUE_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 3:
            top_10()
            while True: 
                try:
                    seguir = int(input("Ingresa una de las opciones:\n{}1) Volver al menu {}\n{}2) Salir {}\n".format(Fore.LIGHTBLUE_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 4:
            print("\n")
            promedio_disparos()
            sleep(1.5)
            puntos_genero()
            sleep(1.5)
            usuarios_edades()
            while True: 
                try:
                    seguir = int(input("Ingresa una de las opciones: \n{}1) Volver al menu {}\n{}2) Salir {}\n".format(Fore.LIGHTBLUE_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 5:
            continuar_jugando = False
    print("Te deseamos un feliz dia, gracias por jugar Battleship\n")
    sleep(1,25)
    top_10()

main()