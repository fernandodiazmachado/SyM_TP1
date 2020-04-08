import tuplaKeys 

listaKeys = tuplaKeys.crearListaDeTuplasKey()

def crearTablero(listaKeys):
    diccionario={}
    for i in range(1,26):
        diccionario[listaKeys[i-1]]=""
    return diccionario

dic = crearTablero(listaKeys)

print (dic)


