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
puntaje = 0
#listas de estadisticas
lista_usuarios = []
lista_ranking = []
usuario_partida = []
lista_ninos = []
lista_jovenes = []
lista_adultos = []
lista_ancianos = []
lista_top_10 = []

def datos_usuario():
    global lista_ninos, lista_jovenes, lista_adultos, lista_ancianos
    usuario_partida.clear()
    username = input("Ingrese su username: ")
    usuarios = []
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
                nombre = nombre[1]
                edad = usuario[2].split(" ")
                edad = edad[1]
                genero = usuario[3].split(" ")
                genero = genero[1]
                usuario_partida.append(username)
                with open("Basedatos.txt", "r") as db:
                    lineas = db.readlines()
                with open("Basedatos.txt", "w") as db:
                    for linea in lineas:
                        if username not in linea:
                            db.write(linea) 
                with open("Basedatos.txt", "a") as bd: 
                    bd.write("{}, {}, {}, {}\n".format(username, nombre, edad, genero))
                return Usuario(username, nombre, edad, genero)
                username_repetido = False
        else:
            validacion_username = username.islower()
            while validacion_username == False:
                print("Su usuario solo puede contener minusculas y numeros\n")
                username = input("Ingerese su username nuevamente: ")
                validacion_username = username.islower()
            while len(username) > 30 or " " in username:
                if len(username) > 30:
                    print("Su usuario no puede ser mayor a 30 caracteres\n")
                    username=input("Ingerese su username nuevamente: ")
                if " " in username:
                    print("Su usuario no puede contener espacios\n")
                    username = input("Ingerese su username nuevamente: ")
            usuario_partida.append(username)
            nombre = input("Ingrese su nombre completo: ")
            nombre.title()
            edad = input("Ingrese su edad: ")
            verificacion_edad = edad.isdigit()
            while verificacion_edad == False:
                print("Su edad solo puede contener numeros\n")
                edad = input("Ingerese su edad nuevamente: ")
                verificacion_edad = edad.isdigit()
            edad = int(edad)
            while edad >= 0 and edad < 5 or edad > 100:
                print("Tu edad no es adecuada para jugar, ingrese otro numero o juegue con alguien mas\n" )
                edad = input("Ingrese su edad nuevamente: ")
                validacion_edad = edad.isdigit()
                edad = int(edad)
                if edad >= 5 and edad < 101:
                    continue
            if edad >= 5 and edad <= 18:
                lista_ninos.append(edad)
            elif edad >= 19 and edad <= 45:
                lista_jovenes.append(edad)
            elif edad >= 46 and edad <= 60:
                lista_adultos.append(edad)
            elif edad >= 61 and edad <= 100:
                lista_ancianos.append(edad)
            genero = input("Ingrese su genero: \n1) Femenino \n2) Masculino \n3) Ninguno\n")
            verificacion_genero = genero.isdigit()
            while verificacion_genero == False:
                print("No seas bobo ingresa el numero bien")
                genero = input("Ingrese su genero: \n1) Femenino \n2) Masculino \n3) Ninguno\n")
                verificacion_genero = genero.isdigit()
            genero = int(genero)
            while genero < 1 or genero > 3:
                print("No seas bobo ingresa el numero bien")
                genero = input("Ingrese su genero: \n1) Femenino \n2) Masculino \n3) Ninguno\n")
                verificacion_genero = genero.isdigit()
                genero = int(genero)
            if genero == 1:
                genero = "Femenino"
            elif genero == 2: 
                genero = "Masculino"
            elif genero == 3:
                genero = "Ninguno"
            with open("Basedatos.txt", "a+") as bd: 
                bd.write("{}, {}, {}, {}\n".format(username, nombre, edad, genero))
            return Usuario(username, nombre, edad, genero)
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
    while len(lista_ubicacion_barco) > 0:
        mostrar_tablero(tablero)
        elegir_fila = int(input("Ingresa una fila: "))
        elegir_columna = int(input("Ingresa una columna: "))
        tiro_elegido = (elegir_fila, elegir_columna)
        if tiro_elegido == (24,23):
            print("Has accedido a un cheat code, los barcos estan en: ",lista_ubicacion_barco)
        elif tiro_elegido in disparos_elegidos:
            print("Este disparo ya lo has hecho antes :|")
            disparos_repetidos += 1
        elif tiro_elegido in lista_ubicacion_barco:
            disparos_elegidos.append(tiro_elegido)
            print("Has acertado\n")
            tablero[elegir_fila - 1][elegir_columna - 1] = "F"
            lista_ubicacion_barco.remove(tiro_elegido)
            disparos_efectuados += 1
            disparos_acertados += 1
            puntaje += 10
            if tiro_elegido in coordenadas_portaviones:
                coordenadas_portaviones.remove(tiro_elegido)
                if len(coordenadas_portaviones) == 0:
                    print("Felicitaciones has hundido el portaviones, su ataque aereo quedo neutralizado.")
            elif tiro_elegido in coordenadas_fragata:
                coordenadas_fragata.remove(tiro_elegido)
                if len(coordenadas_fragata) == 0:
                    print("Felicitaciones has hundido la Fragata, su comunicacion con tierra ha sido detenida")
            elif tiro_elegido in coordenadas_submarinos:
                coordenadas_submarinos.remove(tiro_elegido)
                if len(coordenadas_submarinos) == 0:
                    print("Felicitaciones has hundido los submarinos")
        else:
            disparos_elegidos.append(tiro_elegido)
            print("Has fallado\n")
            tablero[elegir_fila - 1][elegir_columna - 1] = "X"
            disparos_efectuados += 1
            disparos_fallidos += 1
            puntaje -= 2
    disparos_elegidos.clear()
    print("{}Ese disparo me ha dolido{}".format(Fore.RED, Fore.RESET))
    sleep(1)
    if disparos_efectuados == 9:
        print("¿Eres un robot? lo que acabas de hacer es poco probable... ¿viste los cheat codes verdad?")
    elif disparos_efectuados < 45:
        print("Excelente estrategia")
    elif disparos_efectuados >= 45 and disparos_efectuados <= 70:
        print("Buena estrategia, pero hay que mejorar(o buscar los cheat codes)")
    elif disparos_efectuados > 70:
        print("{}Considérese Perdedor, tiene que mejorar(cuando te pidan las filas mete en fila el #de Kobe y en columna el #de Jordan){}".format(Fore.RED, Fore.RESET))
    print("{}Felicidades has hundido todas las naves{}".format(Fore.YELLOW, Fore.RESET))
    sleep(0.7)
    print("\nEstamos cargando tus estadisticas, para la proxima deberias probar poner el numero de kobe y jordan en fila y columana, solo digo\n")
    sleep(2)
    for x in usuario_partida:
        print("{}{} tus estadisticas fueron las siguientes:{}".format(Fore.YELLOW,x, Fore.RESET))
    print("Disparos realizados = {}".format(disparos_efectuados))
    print("Puntaje total = {}".format(puntaje))
    print("Disparos repetidos = {}".format(disparos_repetidos))
    print("Tu tablero quedo asi:")
    mostrar_tablero(tablero)
    for x in usuario_partida:
        y = x
    with open("Top10.txt", "a") as t10:
        t10.write("{}, {}\n".format(y, puntaje))

def top_10():
    usuarios_top = []
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        y = x[:-1].split(",")
        usuarios_top.append(y)
    usuarios_top = sorted(usuarios_top, key=lambda x: x[4], reverse=True)
    print("\nEl top 10 de usuarios es:")
    usuarios = []
    for x in usuarios_top:
        usuarios.append(x)
        if len(usuarios) <= 10:
            print("="*20, x[0], "-"*5, ">", x[4],"pts")
        else: break

def ver(edit = False):
    print("Estos son los usuarios registrados actualmente:")
    usuarios = []
    with open("BaseDatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        usuario = x[:-1].split(',') # [:-1] para quitar el salto de linea
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
        print(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
    #usuarios = sorted(usuarios, key= lambda user: user.username)
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for n, y in enumerate(usuarios):
        print('='*5, n+1, '='*5)
        print(y)

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
            genero.append(masculinos)
            puntos_masculinos += genero[4]
        elif genero[3] == " Femenino":
            genero.append(femeninos)
            puntos_femeninos += genero[4]
        elif genero[3] == " Ninguno":
            genero.append(ninguno)
            puntos_ninguno += genero[4]

def actualizar_datos(elegir):
    print("""
¿Qué dato desea modificar?
1 - Username
2 - Nombre
3 - Edad
4 - Género
    """)
    eleccion = int(input("Ingrese una opción: "))
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
        user = datos[elegir - 1][:-1].split(",")
    user[eleccion - 1] = input("Ahora ingrese su nuevo dato: ")
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
    print("{}Bienvenidos a Battleship ¿crees tener lo necesario para hundir mi flota?{}".format(Fore.BLUE, Fore.RESET))
    sleep(2)
    print("{}No lo creo jajaja{}".format(Fore.RED, Fore.RESET))
    continuar_jugando = True
    while continuar_jugando:
        sleep(1.5)
        print("""
Selecciona lo que quieras hacer
1) Jugar una partida
2) Ver tabla de usuarios
3) Editar un usuario
4) Ver el leaderboard
5) Salir del Juego
""")
        elegir = input("Ingrese su opcion: ")
        if elegir == "1":
            lista_usuarios.append(datos_usuario())
            juego()
        elif elegir == "2":
            puntos_genero()
        elif elegir == "3":
            ver(edit = True)
            seleccion = int(input("Seleccione el usuario que desee actualizar: "))
            actualizar_datos(seleccion)
        elif elegir == "4":
            top_10()
        elif elegir == "5":
            print("Te deseamos un feliz dia, gracias por jugar Battleship")
            continuar_jugando = False
    print("Ranking de jugadores")

main()
