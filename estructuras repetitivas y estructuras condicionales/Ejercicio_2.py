# Leer 10 números y obtener la cantidad de mayores y la cantidad de
# menores a 100, cuál es el número máximo y cuál es el número mínimo.

numeros=[]
i=1
while(i<11):
    numero=int(input("Ingrese un numero: "))
    numeros.append(numero)
    i+=1

mayores_a_100= 0
menores_a_100=0
igual_a_100=0
for num in numeros:
    if num <100:    
        menores_a_100 +=1
    elif num>100:
        mayores_a_100 +=1
    else:
        igual_a_100 +=1

print("En la lista hay {} numeros menores a 100".format(menores_a_100))
print("En la lista hay {} numeros mayores a 100".format(mayores_a_100))
print("En la lista hay {} numeros iguales a 100".format(igual_a_100))
print("El numero minimo de la lista es: {}".format(min(numeros)))
print("El numero maximo de la lista es: {}".format(max(numeros)))


