tuplaKey_1=(1,1)
tuplaKey_2=(1,2)
tuplaKey_3=(1,3)
tuplaKey_4=(1,4)
tuplaKey_5=(1,5)

tuplaKey_6=(2,1)
tuplaKey_7=(2,2)
tuplaKey_8=(2,3)
tuplaKey_9=(2,4)
tuplaKey_10=(2,5)

def crearTablero(): return {
                            tuplaKey_1:"a",tuplaKey_2:"X",tuplaKey_3:"X",tuplaKey_4:"c",tuplaKey_5:"b",
                            tuplaKey_6:"X",tuplaKey_7:"X",tuplaKey_8:"X",tuplaKey_9:"X",tuplaKey_10:"X"
                            }

tabla = crearTablero()


for i in range(1,3):
    for j in range(1,6):
        numero=i,j
        print(tabla[numero]+" ",end="")
    print()


