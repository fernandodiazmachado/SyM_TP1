def crearTablero():
    primeraClave=1
    ultimaClave=25
    diccionario={}
    for i in range(primeraClave,ultimaClave+1):
        #el primer valor de clave es incluyente, pero el ultimo excluyente, por eso sumo 1
        diccionario[i]="X"
        #Seteo todos los valores iguales
    return diccionario

def imprimirTableroValores():
    dic = crearTablero()
    corte=5 
    #Variable corte, pensada como un salto de linea cada 5 columnas
    for i in dic:
        if i==corte or i==corte*2 or i==corte*3 or i==corte*4:
            print(dic[i])
        else:
            print(dic[i]+"",end="")
    print()

def imprimirTableroClaves():
    dic = crearTablero()
    corte=5
    for i in dic:
        if i==corte or i==corte*2 or i==corte*3 or i==corte*4:
            print(i)
        else:
            print(i,end=" ")
    print()

def imprimirTableroCompleto():
    dic = crearTablero()
    for i in dic.items():
        if i==(5,"X") or i==(10,"X") or i==(15,"X") or i==(20,"X") or i==(5,"") or i==(10,"") or i==(15,"") or i==(20,""):
            print(i)
        else:
            print(i,end="")
    print()

imprimirTableroValores()
imprimirTableroClaves()
imprimirTableroCompleto()

