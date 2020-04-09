class Matriz:
    filas=5
    columnas=5

    def crearMatriz(self):
        Matrix=[["" for x in range(self.columnas)] for y in range(self.filas)] 
        #podria haber puesto: Matriz =[["","","","",""]  [][][][]  ]
        #solo complete la fila 1, cada columna en vacio
        return Matrix

    def mostrarMatrizCompleta(self):
        print (self)

    def mostrarCeldaMatriz(self,fila,columna):
        print (self[fila][columna])

    def modificarCelda(self,fila,columna):
        self[fila][columna]="X"
        return matriz

ma = crearMatriz()

mostrarMatrizCompleta(ma)

modificarCelda(ma,0,4)

mostrarMatrizCompleta(ma)
