<<<<<<< Updated upstream
from variables import valores_aleatorio,valores_manual,valores_norte,valores_sur,valores_este,valores_oeste
import numpy as np
import random
=======
from variables import valores_aleatorio,valores_manual,valores_norte,valores_sur,valores_este,valores_oeste, mov_tocado,mov_barco,mov_agua, total_casillas
import numpy as np
import random
#Funciones
#Funciones Naza
#Crear nuestro tablero:

def crear_tablero(filas=10, columnas=10):
    return np.full((filas, columnas)," ")

#Crear tablero de la máquina:

def crear_tablero_maquina(filas=10, columnas=10):
    tablero_maquina = crear_tablero(filas, columnas)
    tablero_mascara = crear_tablero(filas, columnas)
    return tablero_maquina, tablero_mascara

# Funciones Román
def disparo_maquina(tablero_usuario, fin_partida):
    """
    La máquina dispara aleatoriamente sobre el tablero del usuario.
    Si cae en una casilla ya disparada, muestra mensaje y vuelve a intentar.
    """
    
    nfil, ncol = tablero_usuario.shape
    acierto = False
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
            acierto = True
        # 3. Si hay agua
        elif celda == " ":
            tablero_usuario[fila, columna] = "-"
            resultado = "agua"
        
        # 4. Ya tenemos un disparo válido, salir del bucle
        break
    
    print(f"La máquina ha disparado en ({fila}, {columna}) y ha sido: {resultado.upper()}")
    conteo = np.count_nonzero(tablero_usuario == 'X')
    if conteo == total_casillas:
        fin_partida = True

    return tablero_usuario, acierto, fin_partida

# Funciones Sara
filas = 10
columnas = 10

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
    
    return fila,col

def recibir_disparo(fila, col,tablero_maquina,tablero_mascara, fin_partida):

    #Devuelve:
    # -1 -> ya se había disparado en esa casilla
    # "1" -> si impacta en un barco
    # "0" -> si disparo se efectua en el agua
    acierto = False
    #Comprobamos si se ha realizado un disparo en una coordenada
    if tablero_mascara[fila,col] in (mov_tocado,mov_agua):
        print("Ya se habia disparado aqui")
        
    
    #Si hay un barco
    if tablero_maquina[fila,col] == mov_barco:
        tablero_maquina[fila,col] = mov_tocado #Marco el barco tocado en el tablero de los barcos
        tablero_mascara[fila,col] = mov_tocado #Marco el barco tocado en el tablero de los impactos
        acierto = True
        print ("Tocado!")
        # return 1

    #Si hay agua
    else:
        tablero_mascara[fila,col] = mov_agua
        print("Has tocado agua")
    conteo = np.count_nonzero(tablero_mascara == 'X')
    if conteo == total_casillas:
        fin_partida = True

    return tablero_maquina,tablero_mascara,acierto,fin_partida
    
# Funciones Javier
>>>>>>> Stashed changes

# Funcion para elegir la modalidad al colocar barcos
# Manual: El usuario elige la colocación inicial y orientación de cada barco
# Aleatorio: Se asigna de forma aleatoria la posición de cada barco

def elegir_modalidad():
    eleccion = input("¿Cómo quieres crear los barcos?\n" \
    "(Manual (M) o Aleatorio (A))\n")
    
    while eleccion not in valores_manual and eleccion not in valores_aleatorio: 
        eleccion = input("Introduce un valor válido\n" \
    "(Manual (M) o Aleatorio (A))\n")
    
    return eleccion

# Función para crear cada barco en función de su tamaño, estableciendo el punto de inicio del barco
def generar_barco(eleccion,tamaño):
    barco = []
    
    if eleccion  in valores_manual:
        print("Has elegido manual.")
        pos_x = int(input (f"Indícame la fila dónde quieres poner el barco de tamaño {tamaño}:\n"))
        pos_y = int(input (f"Indícame la columna dónde quieres poner el barco de tamaño {tamaño}:\n"))
        orientacion = input("Indícame la orientación que quieres que tenga el barco:\n")
        barco_inicio = np.array([(pos_x,pos_y)])
        barco = ampliar_barco(orientacion,pos_x,pos_y,barco_inicio,tamaño)

    if eleccion in valores_aleatorio:
        print("Has elegido aleatorio.")
        pos_x = np.random.randint(0,10)
        pos_y = np.random.randint(0,10)
        barco_inicio = np.array([(pos_x,pos_y)])
        cardinales = ["N","S","E","O"]
        orientacion = random.choice(cardinales) # Genero la orientación al azar
        barco = ampliar_barco(orientacion,pos_x,pos_y,barco_inicio,tamaño)

    return barco

# Función para ir añadiendo casillas al barco hasta completar su tamaño y siguiendo la orientación
def ampliar_barco(orientacion,x,y,barco,tamaño):
    if orientacion in valores_norte:
        for i in range(tamaño-1):
            x = x -1
            barco = np.concatenate([(barco),np.array([(x,y)])])
    elif orientacion in valores_sur:
        for i in range(tamaño-1):
            x = x +1
            barco = np.concatenate([(barco),np.array([(x,y)])])
    elif orientacion in valores_este:
        for i in range(tamaño-1):
            y = y -1
            barco = np.concatenate([(barco),np.array([(x,y)])])
    elif orientacion in valores_oeste:
        for i in range(tamaño-1):
            y = y +1
            barco = np.concatenate([(barco),np.array([(x,y)])])
    return barco

# Función para colocar los barcos generados, comprueba además que no se salga del tablero,
#  ni coincida o esté próximo a otro barco
def posicionar_barco(barco, tablero):
    nuevo_barco = []
    colocado = False
    for x,y in barco:

        if not (0 <= x < tablero.shape[0] and 0 <= y < tablero.shape[1]):
            # raise ValueError
            print(f"El barco {barco} no puede colocarse fuera del tablero {x,y}")
            nuevo_barco  = []
            break
            
        else: 
            if tablero[x,y] == mov_barco:
                # raise ValueError
                print(f"No es posible colocar el barco {barco} en una posición ocupada {x,y}")
                nuevo_barco = []
                break
                
            elif comprobar_contiguos(tablero,x,y):
                print(f"No es posible colocar el barco {barco} en una posición contigua a otro {x,y}")
                nuevo_barco =[]
                break
            else:
                nuevo_barco.append([x,y])
                
    print("El barco a pintar es:",nuevo_barco)
    if nuevo_barco: 
        colocado = True
        for x, y in nuevo_barco:
            tablero[x,y] = mov_barco
    return tablero,colocado

# Función para comprobar las casillas contiguas a una posición x e y dada y ver si tienen valor 'O' de barco

def comprobar_contiguos(tablero, x, y):
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(max(0, x-1), min(filas, x+2)):
        for j in range(max(0, y-1), min(columnas, y+2)):
            if tablero[i][j] == mov_barco:
                return True
    return False
