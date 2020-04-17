from io import *

def listaCelulasVivas():
    celulasDePrueba=open("CelulasVivas.txt","r")
    texto = celulasDePrueba.readlines()
    celulasDePrueba.close()
    return texto