from random import randint
from Naves import Portaviones
from Naves import Fragata
from Naves import Submarinos
numero_columnas = 10
numero_filas = 10
tablero = []
orientaciones = ("Vertical", "Horizontal")
lista_ubicacion_barco = []  
lista_temporal = []
coordenadas_portaviones = []
coordenadas_fragata = []
coordenadas_submarinos = []
disparos_elegidos = []
disparos_efectuados = 0
disparos_acertados = 0
disparos_fallidos = 0
disparos_repetidos = 0
puntaje = 0

def crear_tablero(tablero): 
    for x in range(numero_filas):
        completar_tablero = ["■"] * numero_columnas
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
                lista_ubicacion_barco.append(x)
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
            lista_ubicacion_barco.append(ubicacion)
        elif mal_ubicado == "si":
            cantidad = cantidad
def ubicar_naves():
    crear_tablero(tablero)
    ubicar_portaviones()
    ubicar_fragata()
    ubicar_submarino()

def juego():
    global disparos_acertados, disparos_efectuados, disparos_elegidos, disparos_fallidos, disparos_repetidos
    disparos_efectuados = 0
    disparos_acertados = 0
    disparos_fallidos = 0
    disparos_repetidos = 0
    puntaje = 0
    while len(lista_ubicacion_barco) > 0:
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
            print("Has acertado")
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
            print("Has fallado")
            tablero[elegir_fila - 1][elegir_columna - 1] = "X"
            disparos_efectuados += 1
            disparos_fallidos += 1
            puntaje -= 2
        mostrar_tablero(tablero)
    disparos_elegidos.clear()
    print("Tu puntaje fue: ",puntaje)
    print("Disparos efectuados: ",disparos_efectuados)
    print("Disparos acertados: ",disparos_acertados)
    print("Disparos fallidos: ",disparos_fallidos)
    print("Disparos repetidos: ",disparos_repetidos)
    if disparos_efectuados == 9:
        print("¿Eres un robot? lo que acabas de hacer es poco probable... ¿viste los cheat codes verdad?")
    elif disparos_efectuados < 45:
        print("Excelente estrategia")
    elif disparos_efectuados >= 45 and disparos_efectuados <= 70:
        print("Buena estrategia, pero hay que mejorar(o buscar los cheat codes)")
    elif disparos_efectuados > 70:
        print("Considérese Perdedor, tiene que mejorar(cuando te pidan las filas mete en fila el #de Kobe y en columna el #de Jordan)")
    tablero.clear()
