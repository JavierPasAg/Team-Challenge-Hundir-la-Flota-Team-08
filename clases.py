<<<<<<< HEAD
#Sergi

=======
>>>>>>> Sergi
import numpy as np
import random
from variables import dimensiones_tablero, barco, movimientos

class Tablero:
    def __init__(self, usuario_id, dimensiones = 10, dict_barcos)
        
        # usuario_id: identificador (ej. "jugador" o "maquina")
        # dict_barcos: diccionario "codigo_barco": eslora.

        self.usuario_id = usuario_id
        self.dimensiones = dimensiones
        self.tablero = np.full((10,10), mov_agua, dtype = int) # Tablero propio (barcos propios y marcas)
        self.seguimiento = np.full((10,10), mov_agua, dtype = int) # Tablero seguimiento (disparos en tablero adversario)
        self.barcos = [] #lista con objetos Barco. Facilita saber si está hundido y gestionar los impactos
        self.barco_posicionamiento_random() #Coloca barcos de forma aleatoria y crea objetos barco en self.barcos
    
    def barco_posicionamiento_random(self): #Colocar todos los barcos aleatoriamente para evitar solapamientos

    def disparo(self, x, y): #Resuelve disparo y actualiza barcos

    def barcos_hundidos(self): #Devuelve True si todos los barcos se hunden. Game over
        return all(barco.hundido() for barco in self.barcos)

    def imprimir_tablero(self): ?¿

class Barco:
    def __init__(self, nombre, eslora, coordenadas):
        self.nombre = nombre
        self.eslora = eslora
        self.coordenadas = set(coordenadas) #Permite buscar coordenadas rápidamente, 
        # eliminar coordenadas fácilmente y garantiza que no hay repeticiones
        self.vidas = eslora
    
    def recibir_impacto(self, x,y) #Marca un impacto en el barco, devuelve True si se hunde
        if (x,y) in self.coordenadas: #Comprovar si impacta en este barco
            self.coordenadas.remove((x,y)) #Eliminar coordenada del barco
            self.vidas -= 1 #Restar una vida
            if self.vidas <= 0 #Comprobación hundimiento
                return True
        return False

    def hundido (self) #Devuelve True si el barco se hunde.
        return f"Barcos {self.nombre} ({self.eslora}) vidas = {self.vidas}"
<<<<<<< HEAD
=======

>>>>>>> Sergi
