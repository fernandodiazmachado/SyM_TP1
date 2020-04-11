import Malla

def SumarAdyacentes(matriz, fila, columna):
    totalVecinos = 0

    for fil in range(fila-1, fila+2, 1):#Recorro desde la fila anterior, hasta la siguiente.
        for col in range(columna-1, columna+2, 1):#Recorro desde la columna anterior hasta la siguiente
            if( fil == fila and col == columna):
                continue #-->Continuo con la siguiente iteración
            if fil == len(matriz) or col == len(matriz[fil]):
                break
            if fil >= 0 and col >= 0 and matriz[fil][col] == "X":
                totalVecinos = totalVecinos + 1

    return totalVecinos

def NuevaMatriz(matrizOriginal):
 
    matriz = Malla.Malla(5,5)
    #Creo matriz vacia
    for fil in range(len(matrizOriginal)):
        for col in range(len(matrizOriginal[fil])):
            cantidad = SumarAdyacentes(matrizOriginal, fil, col)
            if cantidad < 2 or cantidad >3:
                matriz.celulaMuerta(fil+1,col+1) #= ""
            elif cantidad ==2 or cantidad==3:
                matriz.celulaViva(fil+1,col+1) #= "X"

    return matriz.mallaCompleta()

