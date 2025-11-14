from funciones import generar_barco,posicionar_barco,elegir_modalidad
import numpy as np

tablero_test = np.full((10,10)," ")

eleccion = elegir_modalidad()
for tamaño in [4,3,3,2,2,2,1,1,1,1]:
    colocado = False
    while not colocado:
        barco = (generar_barco(eleccion,tamaño))
        print(barco)
        tablero,colocado = posicionar_barco(barco,tablero_test)

print(tablero)
