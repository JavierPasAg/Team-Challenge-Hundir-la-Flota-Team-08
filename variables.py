#Variables

bienvenida = """¡BIENVENIDO A HUNDIR LA FLOTA!\n
1.Tu tablero y el de la máquina son de 10x10 casillas.\n
2. Hay distintos barcos que debes hundir:\n
   - 4 barcos de 1 casilla\n
   - 3 barcos de 2 casillas\n
   - 2 barcos de 3 casillas\n
   - 1 barco de 4 casillas\n
3. Cada turno, dispara a una coordenada (fila,columna). Ejemplo: 3,5\n
   - Si aciertas, tu turno continúa.\n
   - Si fallas, le toca a la máquina.\n
4. El juego termina cuando un jugador pierde todos sus barcos.\n
¡Buena suerte!"""


usuario1 = "Máquina"
usuario2 = "Yo"

tablero = n_filas = 10; n_columnas = 10

#Barcos
#b1(tamaño 1)= 4 barcos
#b2 (tamaño 2)= 3 barcos
#b3 (tamaño 3)= 2 barcos
#b4 (tamaño 4) = 1 barco

barcos = [1,1,1,1,2,2,2,3,3,4]

mov_barco = "O"
mov_tocado = "X"
mov_agua = "-"

valores_manual = ["M","m","Manual","manual","MANUAL"]
valores_aleatorio = ["A","a","Aleatorio","aleatorio","ALEATORIO"]
valores_norte = ["N","n","Norte","norte","NORTE"]
valores_sur = ["S","s","Sur","sur","SUR"]
valores_este = ["E","e","Este","este","ESTE"]
valores_oeste = ["O","o","Oeste","oeste","OESTE"]
