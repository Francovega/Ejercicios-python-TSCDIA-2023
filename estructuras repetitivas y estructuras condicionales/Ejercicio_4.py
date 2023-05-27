# Leer 10 números y mostrar solamente los números positivos, y su
# sumatoria.

numeros=[]
for x in range (10):
    numero=int (input("ingrese cualquier numero: "))
    numeros.append(numero)

positivos=[]
for i in numeros:
    if(i>0):
        positivos.append(i)
sumatoria=0
for y in positivos:
    sumatoria +=y

print ("Los numeros positivos son : {}".format(positivos))
print("La sumatoria de los positivos es {}".format(sumatoria)) 