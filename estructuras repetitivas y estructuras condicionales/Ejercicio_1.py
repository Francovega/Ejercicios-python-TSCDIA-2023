# Realice un programa que lea 4 números y diga cuántos son pares y
# cuantos impares y devuelva la sumatoria de los pares.

numeros=[]
i=1
while(i<5):
    numero=int(input("ingrese un numero: "))
    numeros.append(numero)
    i += 1

for num in numeros:
    resto= num % 2
    if (resto==0):
        print ("el numero {} es par".format(num))
    else:
        print ("el numero {} es impar".format(num))  
