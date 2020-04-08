def crearTablero():
    diccionario={}
    for i in range(1,26):
        diccionario[i]="X"
    return diccionario

def imprimirTablero():
    dic = crearTablero()
    print(dic)
    corte=5
    for i in dic:
        if i==corte or i==corte*2 or i==corte*3 or i==corte*4:
            print(dic[i])
        else:
            print(dic[i]+"",end="")
    print()

def imprimirTableroCompleto():
    dic = crearTablero()
    for i in dic.items():
        if i==(5,"X") or i==(10,"X") or i==(15,"X") or i==(20,"X") or i==(5,"") or i==(10,"") or i==(15,"") or i==(20,""):
            print(i)
        else:
            print(i,end="")
    print()



