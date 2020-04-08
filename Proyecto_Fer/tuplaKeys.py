"""tuplaKey_1=(1,1)
tuplaKey_2=(1,2)
tuplaKey_3=(1,3)
tuplaKey_4=(1,4)
tuplaKey_5=(1,5)
tuplaKey_6=(2,1)
tuplaKey_7=(2,2)
tuplaKey_8=(2,3)
tuplaKey_9=(2,4)
tuplaKey_10=(2,5)
tuplaKey_11=(3,1)
tuplaKey_12=(3,2)
tuplaKey_13=(3,3)
tuplaKey_14=(3,4)
tuplaKey_15=(3,5)
tuplaKey_16=(4,1)
tuplaKey_17=(4,2)
tuplaKey_18=(4,3)
tuplaKey_19=(4,4)
tuplaKey_20=(4,5)
tuplaKey_21=(5,1)
tuplaKey_22=(5,2)
tuplaKey_23=(5,3)
tuplaKey_24=(5,4)
tuplaKey_25=(5,5)"""

def crearListaDeTuplasKey():
    lista=[]
    for fila in range(1,6):
        for columna in range(1,6):
            tupla=(fila,columna)
            lista.append(tupla)
    return lista
