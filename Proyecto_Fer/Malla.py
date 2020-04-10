class Malla():

    def __init__(self):
        self.__filas=5
        self.__columnas=5
        self.__celulaMuerta=""
        self.__celulaViva="X"
        self.__matriz=[[self.__celulaViva for x in range(self.__columnas)] for y in range(self.__filas)]
        #creo el atributo matriz con todos sus campos cargados como self.__celulaViva/Muerta
    
    def mostrarMallaCompleta(self):
        print(self.__matriz)

    def mostrarCelula(self,fila,columna):
        print(self.__matriz[fila][columna])

    def celulaViva(self,fila,columna):
        self.__matriz[fila][columna]=self.__celulaViva

    def celulaMuerta(self,fila,columna):
        self.__matriz[fila][columna]=self.__celulaMuerta

"""
m = Malla()
m.mostrarMallaCompleta()
m.mostrarCelula(1,2)
m.celulaMuerta(1,2)
m.mostrarMallaCompleta()
"""