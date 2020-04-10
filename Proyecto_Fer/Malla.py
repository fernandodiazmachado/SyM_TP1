class Malla():

    def __init__(self,filas,columnas):
        self.__filas=filas
        self.__columnas=columnas
        self.__celulaMuerta=""
        self.__celulaViva="X"
        self.__matriz=[[self.__celulaViva for x in range(self.__columnas)] for y in range(self.__filas)]
        #creo el atributo matriz con todos sus campos cargados como self.__celulaViva/Muerta
    
    def mostrarMallaCompleta(self):
        print(self.__matriz)

    def valorCelula(self,fila,columna):
        return self.__matriz[fila - 1][columna - 1]

    def celulaViva(self,fila,columna):
        self.__matriz[fila - 1][columna - 1]=self.__celulaViva

    def celulaMuerta(self,fila,columna):
        self.__matriz[fila - 1][columna - 1]=self.__celulaMuerta

"""
m = Malla(3,3)
m.mostrarMallaCompleta()


m.celulaMuerta(3,2)
m.mostrarMallaCompleta()

m.mostrarMallaCompleta()

m.mostrarCelula(1,2)
m.celulaMuerta(1,2)
m.mostrarMallaCompleta()
"""
