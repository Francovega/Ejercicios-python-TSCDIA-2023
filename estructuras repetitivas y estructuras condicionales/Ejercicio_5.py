# Leer 15 números negativos y convertirlos a positivos e imprimir dichos
# números.

numeros=[]
for i in range (15):
    while(True):
        numero=int(input("Ingrese un numero negativo: "))
        if (numero<0):
            numeros.append(numero)
            break
        else:
            print("Ingrese solo numeros negativos")

positivos=[]
for x in numeros:
    positivo= abs(x)
    positivos.append(positivo)

print("Los numeros convertidos a positivos son : {}".format(positivos))