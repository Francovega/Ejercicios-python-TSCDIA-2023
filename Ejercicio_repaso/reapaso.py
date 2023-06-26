# 5. Realice un programa que contenga una función que se llame “conversion”, 
# que la misma contenga tres parámetros. Se pide convertir los segundos ingresados
# en horas, minutos y segundos

def conversion(segundos):
    horas = segundos // 3600
    min = (segundos % 3600) // 60
    seg = (segundos % 3600) % 60
    return horas, min, seg

segundos = int(input("Ingrese la cantidad de segundos: "))
horas, minutos, segundos = conversion(segundos)
print("La conversión es: {} horas, {} minutos, {} segundos".format(horas, minutos, segundos))
