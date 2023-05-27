# Realizar un programa que permita ingresar “f” o “m” y determinar si vota
# en mesa femenina o masculina.

genero= input ("Por favor ingrese M si su genero es masculino o F si su genero es femenino: ")

if (genero == "M" or genero== "m"):
    print("Usted vota en la mesa masculina")
elif genero=="F" or genero=="f":
    print("Usted vota en la mesa femenina")
else:
    print ("Por favor ingrese solamente F o M ")
