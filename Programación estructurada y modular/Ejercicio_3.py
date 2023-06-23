# Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. 
# Mostrar el resultado dos veces.

def sumar (numero1,numero2,numero3):
    resultado1= numero1 + numero2
    print ("{} + {} = {}".format (numero1,numero2,resultado1))
    total= resultado1 + numero3
    print  ("{} + {} = {}".format (resultado1,numero3,total))

# Menu
print ("Elija 3 numeros")
numero1 = int(input ("Elija el numero 1: "))
numero2 = int(input ("Elija el numero 2: "))
numero3 = int(input ("Elija el numero 3: "))
sumar (numero1,numero2,numero3)