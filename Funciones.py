#Funciones
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

