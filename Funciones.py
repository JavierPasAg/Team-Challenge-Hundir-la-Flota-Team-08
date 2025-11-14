#Funciones

#Crear nuestro tablero:

def crear_tablero(filas=10, columnas=10):
    return np.full((filas, columnas),"")

#Crear tablero de la máquina:

def crear_tablero_maquina(filas=10, columnas=10):
    tablero_maquina = crear_tablero(filas, columnas)
    tablero_mascara = crear_tablero(filas, columnas)
    return tablero_maquina, tablero_mascara

