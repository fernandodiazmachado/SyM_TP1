class Malla():

    def __init__(self):
        self.__filas=5
        self.__columnas=5
        self.__celulaMuerta=""
        self.__celulaViva="X"

    def cargarMalla(self):
        self=[[self.__celulaViva for x in range(self.__columnas)] for y in range(self.__filas)] 
        #podria haber puesto: Matriz =[["","","","",""]  [][][][]  ]
        #solo complete la fila 1, cada columna en vacio
        #return Matrix

    def mostrarMallaCompleta(self):
        print(self)

    def mostrarCelula(self,fila,columna):
        print(self[fila][columna])

    def celulaViva(self,fila,columna):
        self[fila][columna]=self.__celulaViva
"""
ma = crearMatriz()

mostrarMatrizCompleta(ma)

modificarCelda(ma,0,4)

mostrarMatrizCompleta(ma) """
m = Malla()
m.cargarMalla()
m.mostrarMallaCompleta()

<__main__.Malla object at 0x7efd085889b0>