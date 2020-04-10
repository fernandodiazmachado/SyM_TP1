def SumarAdyacentes(matriz, fila, columna):
    totalVecinos = 0

    for fil in range(fila-1, fila+2, 1):
        for col in range(columna-1, columna+2, 1):
            if( fil == fila and col == columna):
                continue
            if fil == len(matriz) or col == len(matriz[fil]):
                break
            if fil >= 0 and col >= 0 and matriz[fil][col] == "X":
                totalVecinos = totalVecinos + 1

    return totalVecinos

def NuevaMatriz(matrizOriginal, iteraciones):
    if iteraciones == 0:
        print("Final")
        return
    
    matriz = [None] * len(matrizOriginal)
    for i in range(len(matrizOriginal)):
        matriz[i] = [None] * len(matrizOriginal[i])

    for fil in range(len(matrizOriginal)):
        for col in range(len(matrizOriginal[fil])):
            cantidad = SumarAdyacentes(matrizOriginal, fil, col)
            if cantidad <= 2:
                matriz[fil][col] = ""
            else:
                matriz[fil][col] = "X"

    print (matriz)
    NuevaMatriz(matriz, iteraciones-1)
        
matrizPrueba = [["X", "", ""], ["X","X", ""], ["X","", ""],["X","", ""]]
print(len(matrizPrueba))
print(matrizPrueba)
NuevaMatriz(matrizPrueba,2)
