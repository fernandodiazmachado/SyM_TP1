from io import *

def LeerArchivo(nombreArchivo):
    matriz = []
    archivo = open(nombreArchivo, "r")

    for linea in archivo:
        matriz.append(linea.split(","))
    archivo.close()
    
    return matriz
