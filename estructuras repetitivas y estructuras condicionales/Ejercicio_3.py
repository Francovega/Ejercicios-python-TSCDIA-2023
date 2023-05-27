# Ingresar las edades y el sexo de 15 personas y determinar cuántas son
# mujeres, cuántos varones, cuántos mayores de edad y cuántos
# menores de edad.

mayor_de_edad= 0
menor_de_edad= 0
masculino= 0
femenino= 0
for i in range (15):
    while(True):
        edad=int(input("Ingrese su edad: "))
        if (edad>0):
            if (edad>=18):
                mayor_de_edad += 1
            else:
                menor_de_edad += 1
            break
        else:
            print("Ingrese una edad mayor a 0")
    while (True):
        sexo= input("Ingrese m o f segun su genero: ")
        if sexo== "m" or sexo== "M" or sexo== "f" or sexo== "F":
            if( sexo == "m" or sexo=="M"):
                masculino +=1
            else: 
                femenino +=1    
            break
        else:
            print ("Valor Incorrecto")
  

print("De las 15 edades {} son de genero femenino".format(femenino))
print("De las 15 edades {} son de genero masculino".format(masculino))
print("De las 15 edades {} son de mayores de edad".format(mayor_de_edad))
print("De las 15 edades {} son de menores de edad".format(menor_de_edad))

    