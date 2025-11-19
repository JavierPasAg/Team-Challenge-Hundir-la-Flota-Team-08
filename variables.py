#Variables

bienvenida = r"""
¡BIENVENIDO A HUNDIR LA FLOTA!

                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Tu tablero y el de la máquina son de 10x10 casillas.
2. Hay distintos barcos que debes hundir:
   - 4 barcos de 1 casilla 
   - 3 barcos de 2 casillas 
   - 2 barcos de 3 casillas 
   - 1 barco de 4 casillas 
3. Cada turno, dispara a una coordenada (fila,columna). Ejemplo: 3,5
   - Si aciertas, tu turno continúa.
   - Si fallas, le toca a la máquina.
4. El juego termina cuando un jugador pierde todos sus barcos.
¡Buena suerte!

"""
fin_partida = False
victoria = """¡Enhorabuena!\n
Has ganado la partida\n
Tú eres el verdadero máquina"""
derrota = """¡Vaya!, Has perdido la partida.\n
Vuelve a intentarlo"""
usuario1 = "Máquina"
usuario2 = "Yo"

tablero = n_filas = 10; n_columnas = 10

barcos = [4,3,3,2,2,2,1,1,1,1]
total_casillas = sum(barcos)

mov_barco = "O"
mov_tocado = "X"
mov_agua = "-"

valores_manual = ["M","m","Manual","manual","MANUAL"]
valores_aleatorio = ["A","a","Aleatorio","aleatorio","ALEATORIO"]
valores_norte = ["N","n","Norte","norte","NORTE"]
valores_sur = ["S","s","Sur","sur","SUR"]
valores_este = ["E","e","Este","este","ESTE"]
valores_oeste = ["O","o","Oeste","oeste","OESTE"]