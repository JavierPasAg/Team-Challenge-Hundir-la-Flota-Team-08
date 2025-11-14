#Funciones
import numpy as np
import random

#Crear nuestro tablero:

def crear_tablero(filas=10, columnas=10):
    return np.full((filas, columnas),"")

#Crear tablero de la máquina:

def crear_tablero_maquina(filas=10, columnas=10):
    tablero_maquina = crear_tablero(filas, columnas)
    tablero_mascara = crear_tablero(filas, columnas)
    return tablero_maquina, tablero_mascara


def disparo_maquina(tablero_usuario):
    """
    La máquina dispara aleatoriamente sobre el tablero del usuario.
    Si cae en una casilla ya disparada, muestra mensaje y vuelve a intentar.
    """
    
    nfil, ncol = tablero_usuario.shape
    
    while True:
        fila = random.randrange(nfil)
        columna = random.randrange(ncol)
        
        celda = tablero_usuario[fila, columna]
        
        # 1. Si ya se disparó ahí → mensaje y continuar
        if celda in ("X", "-"):
            print(f"La máquina intentó disparar en ({fila}, {columna}) pero YA había disparado ahí.")
            continue
        
        # 2. Si hay barco → tocado
        if celda == "O":
            tablero_usuario[fila, columna] = "X"
            resultado = "tocado"
        
        # 3. Si hay agua
        elif celda == " ":
            tablero_usuario[fila, columna] = "-"
            resultado = "agua"
        
        # 4. Ya tenemos un disparo válido, salir del bucle
        break
    
    print(f"La máquina ha disparado en ({fila}, {columna}) y ha sido: {resultado.upper()}")
    return fila, columna, resultado

# Función disparo Sara
filas = 10
columnas = 10

mov_barco = "O"
mov_tocado = "X"
mov_agua = "-"

#Turno completo del usuario
#Pide las coordenadas al usuario
#Llama al tablero de la maquina para recibir el disparo
#Si dispara a un barco (la funcion devuelve 1), el usuario repite turno
#Si dispara al agua (la funcion devuelve 0), finaliza su turno y es el turno de la maquina
#Si ya ha disparado en esa celda (la funcion devuelve -1) y se le vuelven a pedir coordenadas al usuario


def pedir_coordenadas_usuario():
 
    #Pide por teclado una fila y una columna válidas al usuario.
    #Devuelve (fila, col) como enteros.
    
    while True:
        try:
            fila = int(input(f"Introduce la FILA (0 - {filas - 1}): "))
            col = int(input(f"Introduce la COLUMNA (0 - {columnas- 1}): "))

            if 0 <= fila < filas and 0 <= col < columnas:
                return fila, col
            else:
                print("Coordenadas fuera del tablero. Inténtalo de nuevo.\n")
        except ValueError:
            print("Debes introducir NÚMEROS enteros. Inténtalo de nuevo.\n")


def recibir_disparo(fila, col):

    #Devuelve:
    # -1 -> ya se había disparado en esa casilla
    # "1" -> si impacta en un barco
    # "0" -> si disparo se efectua en el agua

    #Comprobamos si se ha realizado un disparo en una coordenada
    if tablero_impactos[fila,col] in (mov_tocado,mov_agua):
        print("Ya se habia disparado aqui")
        return -1
    
    #Si hay un barco
    if tablero_barcos[fila,col] == mov_barco:
        tableros_barcos[fila,col] = mov_tocado #Marco el barco tocado en el tablero de los barcos
        tablero_impactos[fila,col] = mov_tocado #Marco el barco tocado en el tablero de los impactos
        print ("Tocado!")
        return 1
    
    #Si hay agua
    else:
        tablero_impactos[fila,col] = mov_agua
        print("Has tocado agua")
        return 0
