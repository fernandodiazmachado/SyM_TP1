class Malla():

    def __init__(self):
        self.__filas=5
        self.__columnas=5
        self.__celulaMuerta=""
        self.__celulaViva="X"
        self.__matriz=self.cargarMatriz()

    def cargarMatriz(self):
        self.__matriz=[[self.__celulaViva for x in range(self.__columnas)] for y in range(self.__filas)] 
        #podria haber puesto: Matriz =[["","","","",""]  [][][][]  ]
        #solo complete la fila 1, cada columna en vacio
        #return Matrix

    def mostrarMallaCompleta(self):
        print(self.__matriz)

    def mostrarCelula(self,fila,columna):
        print(self.__matriz[fila][columna])

    def celulaViva(self,fila,columna):
        self.__matriz[fila][columna]=self.__celulaViva
"""
ma = crearMatriz()

mostrarMatrizCompleta(ma)

modificarCelda(ma,0,4)

mostrarMatrizCompleta(ma) """
m = Malla()

m.mostrarMallaCompleta()