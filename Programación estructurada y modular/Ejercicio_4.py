# Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, 
# mostrar un mensaje que muestre TRUE. 

def sonIguales (numero1,numero2):
    if numero1 == numero2:
        print ("Resultado: TRUE")
    else:
        print ("Resultado: FALSE")

# Menu
print ("Veamos si dos numeros son iguales\nElige dos numeros")
numero1 = int (input("Numero 1: "))
numero2 = int (input("Numero 2: "))
sonIguales(numero1,numero2)