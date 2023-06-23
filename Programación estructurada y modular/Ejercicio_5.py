# Realice un programa que contenga una función que se llame “sumayresta”
# que la misma contenga dos variables locales nombradas suma y resta, respectivamente. 
# Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumaYresta (num1,num2):
    suma = num1 + num2
    resta = num1 - num2
    restainvertida= num2 - num1
    print ("La suma de {} + {} = {}" .format (num1,num2,suma))
    print ("La resta de {} - {} = {}" .format (num1,num2,resta))
    print ("La resta de {} - {} = {}" .format (num2,num1,restainvertida))

# Menu
print ("Elija 2 numeros")
num1 = int(input ("Numero 1: "))
num2 = int(input ("Numero 2: "))
sumaYresta (num1,num2)
