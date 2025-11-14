from variables import valores_aleatorio,valores_manual,valores_norte,valores_sur,valores_este,valores_oeste
import numpy as np
import random

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
            
        else: 
            if tablero[x,y] == 'O':
                # raise ValueError
                print(f"No es posible colocar el barco {barco} en una posición ocupada {x,y}")
                nuevo_barco = []
                
            elif comprobar_contiguos(tablero,x,y):
                print(f"No es posible colocar el barco {barco} en una posición contigua a otro {x,y}")
                nuevo_barco =[]
            else:
                nuevo_barco.append([x,y])
                
    print("El barco a pintar es:",nuevo_barco)
    if nuevo_barco: 
        colocado = True
        for x, y in nuevo_barco:
            tablero[x,y] = 'O'
    return tablero,colocado

# Función para comprobar las casillas contiguas a una posición x e y dada y ver si tienen valor 'O' de barco

def comprobar_contiguos(tablero, x, y):
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(max(0, x-1), min(filas, x+2)):
        for j in range(max(0, y-1), min(columnas, y+2)):
            if tablero[i][j] == 'O':
                return True
    return False
