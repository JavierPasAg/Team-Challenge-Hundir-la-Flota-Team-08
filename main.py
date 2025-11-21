from funciones import (
    generar_barco,posicionar_barco,elegir_modalidad,crear_tablero,
    crear_tablero_maquina, pedir_coordenadas_usuario, recibir_disparo,
    disparo_maquina
)
from variables import bienvenida, fin_partida, victoria, derrota, barcos, id_columnas
import numpy as np

print(bienvenida)

tablero_usuario = crear_tablero()
tablero_maquina, tablero_mascara = crear_tablero_maquina()

print("Tablero usuario\n",id_columnas,"\n",tablero_usuario,"\n",id_columnas,"\n")
print("Tablero enemigo:\n",id_columnas,"\n", tablero_mascara,"\n",id_columnas,"\n")
# Usuario elige y colca barcos
eleccion = elegir_modalidad()
for tamaño in barcos:

    colocado = False
    while not colocado:
        barco = (generar_barco(eleccion,tamaño))
        tablero,colocado = posicionar_barco(barco,tablero_usuario)


# Máquina coloca barcos
eleccion_maquina = "A"
for tamaño in barcos:
    colocado = False
    while not colocado:
        barco = (generar_barco(eleccion_maquina,tamaño))
        tablero_maquina,colocado = posicionar_barco(barco,tablero_maquina)

print("Tablero usuario:\n",id_columnas,"\n",tablero,"\n",id_columnas,"\n")
print("Tablero enemigo:\n",id_columnas,"\n",tablero_mascara,"\n",id_columnas,"\n")

def separador(titulo=None):
    print("\n" + "=" * 60)
    if titulo:
        print(f" {titulo}")
        print("-" * 60)
    print()
    
# BUCLE CON ESTO
# Pedimos coordenadas
while not fin_partida:
    fin_partida
    acierto_usuario = True
    acierto_maquina = True
    # Bucle que se repite mientras acierte el usuario
    while acierto_usuario:
        separador("TU TURNO")
        fila_elegida, columna_elegida = pedir_coordenadas_usuario()
        print(fila_elegida,columna_elegida)
        tablero_maquina,tablero_mascara, acierto_usuario, fin_partida = recibir_disparo(fila_elegida,columna_elegida,tablero_maquina,tablero_mascara, fin_partida)
        print("""
              """)
        print("Tablero usuario:\n",id_columnas,"\n",tablero,"\n",id_columnas,"\n")
        print("Tablero enemigo:\n",id_columnas,"\n",tablero_mascara,"\n",id_columnas,"\n")
        if fin_partida:
            print(victoria)
            break
    
    # Evaluamos si ha terminado la partida
    if fin_partida:
        break
    # Bucle que se repite mientras acierte la máquina
    while acierto_maquina:
        separador("TURNO DE LA MÁQUINA")
        tablero_usuario,acierto_maquina, fin_partida = disparo_maquina(tablero_usuario, fin_partida)
        print("""
              """)
        print("Tablero usuario:\n",id_columnas,"\n",tablero,"\n",id_columnas,"\n")
        print("Tablero enemigo:\n",id_columnas,"\n",tablero_mascara,"\n",id_columnas,"\n")
        if fin_partida:
            print(derrota)
            break
    # Evaluamos si ha terminado la partida 
    if fin_partida:
        break



