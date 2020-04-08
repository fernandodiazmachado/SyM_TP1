def crearMatriz():
    columnas, filas = 5, 5;
    Matrix=[["" for x in range(columnas)] for y in range(filas)] 
    #podria haber puesto: Matriz =[["","","","",""]  [][][][]  ]
    #solo complete la fila 1, cada columna en vacio
    return Matrix

def mostrarMatrizCompleta(matriz):
    print (matriz)

def mostrarCeldaMatriz(matriz,fila,columna):
    print (matriz[fila][columna])

def modificarCelda(matriz,fila,columna):
    matriz[fila][columna]="X"
    return matriz

ma = crearMatriz()

mostrarMatrizCompleta(ma)

modificarCelda(ma,0,4)

mostrarMatrizCompleta(ma)