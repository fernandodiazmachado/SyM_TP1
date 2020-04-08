import tuplaKeys 

listaKeys = tuplaKeys.crearListaDeTuplasKey()

def crearTablero(listaKeys):
    diccionario={}
    for i in range(1,26):
        diccionario[i]=""
    return diccionario

dic = crearTablero(listaKeys)

for i in dic:
    print(dic[i]+"",end="")
    if i!=5:
        print(dic[i]+"",end="")
    else:
        print(dic[i])

#print (dic)


