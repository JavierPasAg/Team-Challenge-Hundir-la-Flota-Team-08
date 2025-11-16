from funciones import generar_barco,posicionar_barco,elegir_modalidad,crear_tablero,crear_tablero_maquina, pedir_coordenadas_usuario, recibir_disparo,disparo_maquina
from variables import bienvenida, fin_partida, victoria, derrota, barcos
import numpy as np

# tablero_test = np.full((10,10)," ")
# EJECUTAR CON: python main.py
print(bienvenida)

tablero_usuario = crear_tablero()
tablero_maquina, tablero_mascara = crear_tablero_maquina()
print("tablero_usuario\n",tablero_usuario)
print("Tablero máquina:\n", tablero_mascara)
# Usuario elige y colca barcos
eleccion = elegir_modalidad()
for tamaño in [4,3,3,2,2,2,1,1,1,1]:
    colocado = False
    while not colocado:
        barco = (generar_barco(eleccion,tamaño))
        print(barco)
        tablero,colocado = posicionar_barco(barco,tablero_test)


# Máquina coloca barcos
eleccion_maquina = "A"
for tamaño in barcos:
    colocado = False
    while not colocado:
        barco = (generar_barco(eleccion_maquina,tamaño))
        print(barco)
        tablero_maquina,colocado = posicionar_barco(barco,tablero_maquina)

print("Tablero usuario:\n",tablero)
print("Tablero_maquina:\n",tablero_maquina)
print("Tablero_maquina Máscara:\n",tablero_mascara)

# BUCLE CON ESTO
# Pedimos coordenadas
while not fin_partida:
    fin_partida
    acierto_usuario = True
    acierto_maquina = True
    # Bucle que se repite mientras acierte el usuario
    while acierto_usuario:
        fila_elegida, columna_elegida = pedir_coordenadas_usuario()
        print(fila_elegida,columna_elegida)
        tablero_maquina,tablero_mascara, acierto_usuario, fin_partida = recibir_disparo(fila_elegida,columna_elegida,tablero_maquina,tablero_mascara, fin_partida)
        print("Tablero_maquina:\n",tablero_maquina)
        print("Tablero_maquina Máscara:\n",tablero_mascara)
        if fin_partida:
            print(victoria)
            break
    
    # Evaluamos si ha terminado la partida
    if fin_partida:
        break
    # Bucle que se repite mientras acierte la máquina
    while acierto_maquina:
        tablero_usuario,acierto_maquina, fin_partida = disparo_maquina(tablero_usuario, fin_partida)
        print("Tablero usuario:\n",tablero)
        if fin_partida:
            print(derrota)
            break
    # Evaluamos si ha terminado la partida 
    if fin_partida:
        break



