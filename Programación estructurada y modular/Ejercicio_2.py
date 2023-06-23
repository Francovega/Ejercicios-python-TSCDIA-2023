# A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del 
# mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. 
# Recuerda: en estos ejercicios trabajamos argumentos.

def saludo (nombre):
    print ("Hola {},¿Que tal?" .format (nombre))


nombres = ["Ana","Jose","Maria"]
for nombre in nombres:
    saludo (nombre)