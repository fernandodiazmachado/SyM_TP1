#Si no reconoce curses como libreria, correr el siguiente comando por consola:
#sudo apt-get install libncurses5-dev libncursesw5-dev
import curses
FILAS = 5 
COLUMNAS = 5
CELULA_MUERTA = "-"
CELULA_VIVA = "X"
matrizInicial = []

def AsignarValorCelula(fila, columna, valor):
    matrizInicial[fila][columna] = valor

def InicializarMatriz():
    #Inicializo todas las celdas como muertas
    #matrizInicial = [[CELULA_MUERTA for x in range(COLUMNAS)] for yin range(FILAS):
    for i in range(FILAS):
        matrizInicial.append([CELULA_MUERTA] * COLUMNAS)

    #Asigno celula viva, #la primera fila es 0
    AsignarValorCelula(0, 0, CELULA_VIVA)
    AsignarValorCelula(1, 1, CELULA_VIVA)
    AsignarValorCelula(1, 3, CELULA_VIVA)
    AsignarValorCelula(2, 0, CELULA_VIVA)
    AsignarValorCelula(2, 2, CELULA_VIVA)
    AsignarValorCelula(3, 1, CELULA_VIVA)
    AsignarValorCelula(3, 3, CELULA_VIVA)
    AsignarValorCelula(4, 0, CELULA_VIVA)

def NuevaMatriz(matrizOriginal):

    matriz = [None] * len(matrizOriginal)
    for i in range(len(matrizOriginal)):
        matriz[i] = [None] * len(matrizOriginal[i])

    for fil in range(len(matrizOriginal)):
        for col in range(len(matrizOriginal[fil])):
            cantidad = SumarAdyacentes(matrizOriginal, fil, col)
            if matrizOriginal[fil][col]==CELULA_VIVA and cantidad ==2 or cantidad==3:
                matriz[fil][col] = CELULA_VIVA
            elif matrizOriginal[fil][col]==CELULA_MUERTA and cantidad==3:
                matriz[fil][col] = CELULA_VIVA
            else:
                matriz[fil][col] = CELULA_MUERTA

    return matriz

def SumarAdyacentes(matriz, fila, columna):
    totalVecinos = 0

    for fil in range(fila-1, fila+2, 1): #Recorro desde la fila anterior, hasta la siguiente.
        for col in range(columna-1, columna+2, 1): #Recorro desde lacolumna anterior hasta la siguiente
            if( fil == fila and col == columna):
                continue #Estoy en la celda de la que estoy contandolos vecinos, empiezo siguiente iteracion
            if fil == len(matriz) or col == len(matriz[fil]):
                break
            if fil >= 0 and col >= 0 and matriz[fil][col] == CELULA_VIVA:
                totalVecinos = totalVecinos + 1

    return totalVecinos

def main():
    screen = curses.initscr() #inicializo el objeto ventana
    fila = 0
    InicializarMatriz()

    screen.addstr(fila,0, "**********MATRIZ INICIAL**********")

    fila += 1
    for fil in range(len(matrizInicial)):
        texto = ""
        for col in range(len(matrizInicial[fil])):
            texto = texto + matrizInicial[fil][col]
            screen.addstr(fila+fil,0, texto)

    curses.napms(1000) #paro la ejecucion (milisegundos)
    fila = fila + FILAS + 1 
    screen.addstr(fila,0, "Presione b para inicializar el programa: ")
    caracter = screen.getch()

    matriz = NuevaMatriz(matrizInicial) #'matriz' es la siguiente matriz a mostrar con las nuevas celulas vivas o muertas

    if chr(caracter) == 'b':
        screen.clear()
        fila = 0
        while chr(caracter) != 'q':
            for fil in range(len(matriz)):
                texto = ""
                for col in range(len(matriz[fil])):
                    texto = texto + matriz[fil][col]
                    screen.addstr(fila+fil, 0, texto)

            curses.napms(1000)
            fila = fila + FILAS + 1

            if fila + FILAS + 1 >= curses.LINES: 
                screen.clear()
                fila = 0
            matriz = NuevaMatriz(matriz)
            caracter = screen.getch()
    curses.endwin()

main()