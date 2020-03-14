from Usuario import Usuario
from random import randint
import Naves
from Naveshijas import Portaviones, Fragata, Submarinos
from time import sleep
from colorama import Fore
tablero = []
#Valores para crear los barcos
numero_filas = 10
numero_columnas = 10
orientaciones = ("Vertical", "Horizontal") #Tupla que se usara para definir aleatoriamente la orientacion de los barcos mayores a 1 posicion
lista_ubicacion_barco = []  #Lista donde se ubicaran las posiciones de cada uno de los barcos
lista_temporal = []
coordenadas_portaviones = []
coordenadas_fragata = []
coordenadas_submarinos = []
#Valores para llevar el conteo de los disparos
disparos_elegidos = []
disparos_efectuados = 0
disparos_acertados = 0
disparos_fallidos = 0
disparos_repetidos = 0
#Listas de estadisticas
lista_usuarios = []
lista_ranking = []
usuario_partida = []
lista_top_10 = []

def datos_usuario():
    """
    Aqui el usuario va a ingresar sus datos (username, nombre, edad y genero)
    """
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
            usuario = x[:-1].split(',') #si el username esta en la base de datos no necesita ingresar sus datos
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
            while validacion_username == False or len(username) > 30 or " " in username: #Validacion para username
                print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
                username = input("Ingerese su username nuevamente: ")
                validacion_username = username.islower()
            usuario_partida.append(username)
            nombre = input("Ingrese su nombre completo: ")
            verificacion_nombre = nombre.replace(" ", "").isalpha()
            while verificacion_nombre == False: #Validacion para nombre
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

#Funciones para el tablero
def crear_tablero(tablero): 
    """
    Se creara la matriz 10x10 para el tablero
    """
    for x in range(numero_filas):
        completar_tablero = ["O"] * numero_columnas
        tablero.append(completar_tablero) 
    return tablero

def mostrar_tablero(tablero):
    """
    Se encarga de imprimir el tablero listo para jugar y que se vea mejor
    """
    numeros_de_fila = []
    for x in range(1, numero_columnas+1):
        y = str(x)
        numeros_de_fila.append(y)
    print("   " + " ".join(numeros_de_fila)) #fila de numeros que designa las columnas
    for w in range(numero_columnas):
        if w < 9:
            print(str(w + 1) + "  " + " ".join(str(x) for x in tablero[w])) #sale primero el numero de la fila y luego imprime la fila del tablero
        else: print(str(w + 1) + " " + " ".join(str(x) for x in tablero[w]))
    print("\n")

#Funciones para ubicar los barcos
def ubicar_portaviones():
    """
    Funcion que ubica el barco mas grande (3 posiciones)
    """
    tamano = Portaviones.tamano #se importa el tamano del barco de su clase
    cantidad = Portaviones.cantidad #se importa la cantidad de barcos de este tamano desde su clase
    orientacion = orientaciones[(randint(0, 1))] #elige aleatoriamente el index de una tupla que tiene 2 valores horizontal y vertical
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
    """
    Se encarga de ubicar el segundo barco mas grande (2 posiciones)
    """
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
                    elif (y[0] == x[0] or (y[0]+1) == x[0] or (y[0]-1) == x[0]) and ((y[1]) == x[1] or (y[1]+1) == x[1] or (y[1]- 1) == x[1]): #validacion para que no se ubique el barco al lado o diagonalmente cercano a otro
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
                    elif (y[0] == x[0] or (y[0]+1) == x[0] or (y[0]-1) == x[0]) and ((y[1]) == x[1] or (y[1]+1) == x[1] or (y[1]- 1) == x[1]):  #validacion para que no se ubique el barco al lado o diagonalmente cercano a otro
                        mal_ubicado = "si"
        if mal_ubicado == "si":
            seguir_coordenadas = True
            lista_temporal.clear()
        elif mal_ubicado == "no": 
            for x in lista_temporal:
                lista_ubicacion_barco.append(x)
                coordenadas_fragata.append(x)
            lista_temporal.clear()
            seguir_coordenadas = False

def ubicar_submarino():
    """
    Se encarga de ubicar las naves mas pequenas (1 posicion)
    """
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
            #validacion para que cada uno de los barcos no queden contiguos entre si
            elif (ubicacion[0] == x[0] or (ubicacion[0]+1) == x[0] or (ubicacion[0]-1) == x[0]) and ((ubicacion[1]) == x[1] or (ubicacion[1]+1) == x[1] or (ubicacion[1]- 1) == x[1]): 
                mal_ubicado = "si"
        if mal_ubicado == "no":
            cantidad -= 1 #se resta uno a la cantidad de los barcos porque ya este se posiciono correctamente
            lista_ubicacion_barco.append(ubicacion) #si el barco no es contiguo con ningun otro barco se agrega a la lista de los barcos ya posicionados
        elif mal_ubicado == "si":
            cantidad = cantidad #la cantidad de barcos se mantiene igual porque el barco quedo contiguo a otro, se repite el proceso d eubicacion para este barco

def ubicar_naves():
    """
    Se encarga de llamar a cada una de las funciones para ubicar los barcos por orden,
    se borra el tablero existente para crear uno nuevo y que la partida empiece con un tablero sin modificaciones
    y con los barcos ya ubicados
    """
    tablero.clear()
    crear_tablero(tablero)
    ubicar_portaviones()
    ubicar_fragata()
    ubicar_submarino()

def juego():
    """
    Funcion que contiene todo lo que sucede desde que se empieza a jugar hasta que se termina,
    tiene los contadores para las categorias de disparo y puntaje
    """
    ubicar_naves()
    global disparos_acertados, disparos_efectuados, disparos_elegidos, disparos_fallidos, disparos_repetidos
    #contadores
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
        while True: #validacion para la fila ingresada por el usuario
            try:
                elegir_fila = int(input("Ingresa una fila: "))
                if elegir_fila < 1 or (elegir_fila >10 and elegir_fila != 24):
                    raise  ValueError
                break
            except ValueError:
                print("{}No existe dicha fila{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        # validar_fila = elegir_fila.isdigit()
        while True: #validacion para la columna ingresada por el usuario
            try:
                elegir_columna = int(input("Ingresa una columna: "))
                if elegir_columna < 1 or (elegir_columna >10):
                    raise  ValueError
                break
            except ValueError:
                print("{}No existe dicha columna{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        tiro_elegido = (elegir_fila, elegir_columna) #cada tiro se almacena en una lista
        if tiro_elegido[0] == 24:
            print("Has accedido a un cheat code, los barcos estan en: ",lista_ubicacion_barco)
        elif tiro_elegido in disparos_elegidos: #si la coordenada ingresada por el usuario ya la ingreso anteriormente, quedo guardada en la lista y no le va a contar como disparo efectuadao
            print("Este disparo ya lo has hecho antes :|")
            disparos_repetidos += 1
        elif tiro_elegido in lista_ubicacion_barco:
            disparos_elegidos.append(tiro_elegido)
            print("Has acertado\n")
            tablero[elegir_fila - 1][elegir_columna - 1] = "{}F{}".format(Fore.RED, Fore.RESET) #se remplaza la coordenada acertada por una F roja
            lista_ubicacion_barco.remove(tiro_elegido)
            disparos_efectuados += 1
            disparos_acertados += 1
            puntaje += 10
            #se verifica si la coordenada ingresada pertenece a alguna coordenada almacenada en las listas de cada barco
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
            tablero[elegir_fila - 1][elegir_columna - 1] = "{}X{}".format(Fore.BLUE, Fore.RESET) #se remplaza la coordenada errada por una X azul
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
    print("\nCargando tus estadisticas :| .......... pssss deberias probar el numero de kobe en fila\n")
    sleep(2.5)
    for x in usuario_partida: #usuario_partida almacena el usuario de cada partida, se borra la lista cuando se ingresa otro jugador
        print("{}{} tus estadisticas fueron las siguientes:{}".format(Fore.YELLOW,x, Fore.RESET))
    print("Disparos realizados = {}".format(disparos_efectuados))
    print("Puntaje total = {}".format(puntaje))
    print("Disparos repetidos = {}".format(disparos_repetidos))
    print("Tu tablero quedo asi:")
    mostrar_tablero(tablero)
    #se agregaran los puntajes y disparos del usuario a la base de datos en el txt
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
            if int(puntos[4]) < puntaje: #si el usuario ya tiene un puntaje se va a almacenar en el txt el que sea mayor (puede ser el viejo o el que acaba de obtener)
                puntos[4] = " {}".format(puntaje)
            if int(puntos[5]) > disparos_efectuados: #si el usuario ya ha jugado se va a almacenar en el txt la menor cantidad de disparos que haya obtenido 
                puntos[5] = " {}".format(disparos_efectuados)
    for x in range(len(puntos)):
        if x != len(puntos) - 1:
            nuevo_valor += puntos[x] + ","
        else:
            nuevo_valor += puntos[x] + "\n"
    datos[index] = nuevo_valor
    with open("Basedatos.txt", "w") as bd: #se reescribira el txt con los datos del usuario que jugo la partida actualizados
        bd.writelines(datos)

#Funciones para las estadisticas
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

def puntos_genero():
    """
    Calcula el puntaje total para cada genero
    """
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
    print("Puntos totales por usuarios masculinos: {}".format(puntos_masculinos))
    print("Puntos totales por usuarios femeninos: {}".format(puntos_femeninos))
    print("Puntos totales por usuarios que no especificaron su genero: {}".format(puntos_ninguno))

def usuarios_edades():
    """
    Muestra el rango de edad de los usuarios que mas han jugado
    """
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    lista_max_edades = []
    lista_ninos = []
    lista_adultos = []
    lista_pures = []
    lista_viejos = []
    for x in datos: #se va a leer las edades de cada uno de los usuarios en la base de datos y se almacenan en listas segmentadas por edades
        edades = x[:-1].split(",")
        edad = int(edades[2])
        if edad >= 5 and edad <= 18:
            lista_ninos.append(edades)
        elif edad >= 19 and edad <= 45:
            lista_adultos.append(edades)
        elif edad >= 46 and edad <= 60:
            lista_pures.append(edades)
        elif edad >= 61 and edad <= 100:
            lista_viejos.append(edades)
    #se calcula la cantidad de usuarios en cada lista por edades y se ingresan las cantidades en otra lista 
    cantidad_ninos = len(lista_ninos) 
    lista_max_edades.append(str(cantidad_ninos))
    cantidad_adultos = len(lista_adultos)
    lista_max_edades.append(str(cantidad_adultos))
    cantidad_pures = len(lista_pures)
    lista_max_edades.append(str(cantidad_pures))
    cantidad_viejos = len(lista_viejos)
    lista_max_edades.append(str(cantidad_viejos))
    #se calcula el maximo valor de la lista y se compara con cada uno de los valores obtenidos en las listas por cada rango de edad
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
    """
    Calcula el promedio de la cantidad de disparos para ganar entre todos los usuarios 
    """
    with open("Basedatos.txt", "r") as bd:
        datos = bd.readlines()
    disparos_totales = 0
    lista_disparos = []
    for x in datos:
        lista = x[:-1].split(",")
        lista_disparos.append(lista)
        disparos_totales += int(lista[5])
    disparos_totales /= len(lista_disparos)
    disparos_totales = (round(disparos_totales, 2))
    print("Los disparos totales en promedio para ganar fueron: {}".format(disparos_totales))

#Funciones para editar datos
def ver(edit = False):
    """
    Le muestra al usuario los usuarios que ya estan registrados en la base de datos para luego editarlos
    """
    print("\nEstos son los usuarios registrados actualmente:\n")
    usuarios = []
    with open("BaseDatos.txt", "r") as bd:
        datos = bd.readlines()
    for x in datos:
        usuario = x[:-1].split(',')
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]))
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for n, y in enumerate(usuarios): #imprime cada uno de los usuarios
        print(Fore.LIGHTCYAN_EX + "="*10 + Fore.YELLOW, n+1, Fore.LIGHTRED_EX + "="*10, Fore.RESET)
        print(y)
        print("\n")

def actualizar_datos(elegir):
    """
    Muestra los datos que se pueden cambiar, el usuario selecciona el que quiera modificar e ingresa el nuevo valor
    """
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
        while validacion_username == False or len(user[eleccion - 1]) > 30 or " " in user[eleccion - 1]: #validacion para el nuevo username
            print("{}Su usuario solo puede contener minusculas y numeros sin ningun espacio{}\n".format(Fore.LIGHTRED_EX, Fore.RESET))
            user[eleccion - 1] = input("Ingerese su username nuevamente: ")
            validacion_username = user[eleccion - 1].islower()
        usuario_partida.clear()
        usuario_partida.append(user[eleccion - 1])
    elif eleccion == 2:
        user[eleccion - 1] = input("Ahora ingrese su nuevo nombre: ")
        verificacion_nombre = user[eleccion - 1].replace(" ", "").isalpha()
        while verificacion_nombre == False: #validacion para el nuevo nombre
                print("{}Su nombre solo puede tener letras{}".format(Fore.LIGHTRED_EX, Fore.RESET))
                user[eleccion - 1] = input("Ingrese su nombre completo: ")
                verificacion_nombre = user[eleccion - 1].replace(" ", "").isalpha()
        user[eleccion - 1] = user[eleccion - 1].title()
        user[eleccion - 1] = " " + user[eleccion - 1]  
    elif eleccion == 3:
        while True: #Validacion para la nueva edad
            try:
                user[eleccion - 1] = int(input("Ingresa su edad: "))
                if user[eleccion - 1] < 5 or user[eleccion - 1] > 100:
                    raise  ValueError
                break
            except ValueError:
                print("{}Tu edad no es adecuada para jugar{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        user[eleccion - 1] = " " + str(user[eleccion - 1]) 
    elif eleccion == 4:
        while True: #Validacion para el nuevo genero
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
    with open("Basedatos.txt", "w") as bd: #se reescribe el archivo txt con el valor del usuario modificado 
        bd.writelines(datos)

def titulo():
    """
    Muestra el titulo inicial del programa
    """
    print("\n" + Fore.WHITE + " "*70 + "SAMAN")
    sleep(1)
    print(" "*75 + "GAMES\n" + Fore.RESET)
    sleep(1)
    print(" "*71 + Fore.LIGHTBLACK_EX + "Presenta\n" + Fore.RESET)
    sleep(1.25)
    print(" "*66 + Fore.LIGHTBLUE_EX + "███ " + "BATTLESHIP" + " ███" + Fore.RESET)
    sleep(1)

def main():
    """
    Se va a mostrar el menu principal y se llaman a todas las funciones para correr el programa
    """
    titulo()
    top_10() #muestra el top10 cada vez que se inicie el juego
    print("{}Bienvenido ¿crees tener lo necesario para hundir mi flota?{}".format(Fore.BLUE, Fore.RESET))
    sleep(2)
    print("{}No lo creo JAJAJA{}".format(Fore.RED, Fore.RESET))
    continuar_jugando = True
    while continuar_jugando:
        print("""
        Menu        
1) Jugar una partida
2) Ver todos los usuarios
3) Editar un usuario
4) Ver el leaderboard
5) Ver estadisticas
6) Salir del Juego
""")
        while True: #validacion para la opcion de menu elegida por el usuario
            try:
                elegir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                if elegir < 1 or elegir > 6:
                    raise  ValueError
                break
            except ValueError:
                print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
        if elegir == 1:
            print("\n")
            lista_usuarios.append(datos_usuario())
            juego()
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 2:
            ver(edit=False)
            sleep(1.5)
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 3:
            print("\n")
            ver(edit = True)
            with open("Basedatos.txt", "r") as bd:
                total = bd.readlines()
            largo = len(total)
            while True:
                try:
                    seleccion = int(input("Seleccione el usuario que desee actualizar: "))
                    if seleccion > int(largo) or seleccion < 1:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            actualizar_datos(seleccion)
            sleep(1)
            print("Su usuario ha sido actualizado correctamente")
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 4:
            top_10()
            sleep(1.5)
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 5:
            print("\n")
            promedio_disparos()
            puntos_genero()
            usuarios_edades()
            sleep(1.5)
            print("\n{}1) Volver al menu \n{}2) Salir {}".format(Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.RESET))
            while True: 
                try:
                    seguir = int(input("{}Ingrese su opcion:{} ".format(Fore.LIGHTYELLOW_EX, Fore.RESET)))
                    if seguir < 1 or seguir > 2:
                        raise  ValueError
                    break
                except ValueError:
                    print("{}La opcion ingresada no es valida{}".format(Fore.LIGHTRED_EX, Fore.RESET))
            if seguir == 1:
                continuar_jugando = True
            else: continuar_jugando = False
        elif elegir == 6:
            continuar_jugando = False
    print("Te deseamos un feliz dia, gracias por jugar " + Fore.LIGHTBLUE_EX + "███ " + "BATTLESHIP" + " ███" + Fore.RESET)
    sleep(1.25)
    top_10()

main()