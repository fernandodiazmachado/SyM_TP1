import tuplaKeys 

listaKeys = tuplaKeys.crearListaDeTuplasKey()

def crearTablero(listaKeys):
    diccionario={}
    for i in range(1,26):
        diccionario[i]="x"
    return diccionario

dic = crearTablero(listaKeys)
print(dic)
corte=5
for i in dic:
    if i==corte or i==corte*2 or i==corte*3 or i==corte*4:
        print(dic[i])
    else:
        print(dic[i]+"",end="")


