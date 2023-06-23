# Realice un programa que muestre el mensaje “Hola Aula X 
# (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados
# entre ellos otro mensajes a su elección. 

def saludo (aula):
    print ("Hola aula {},¿Que tal?" .format (aula))
    respuesta ()

def respuesta ():
    if x==0:
        print ("Hola profe!!!")
    elif x==1:
        print ("Que onda profe!!! ¿todo bien?") 
    else:
        print ("¡Todo bien!")   

x=0
while(x<3):
    aula= input("¿A que aula quiere saludar? \n Ingrese un numero: ")
    saludo(aula)
    x+=1