'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
*La suma de los números que están dentro del intervalo (intervalo abierto).
*Cuantos números están fuera del intervalo.
*He informa si hemos introducido algún número igual a los límites del intervalo.
'''

limInferior=0
limSuperior=0

limInferior=(int)(input("Dime el limite inferior de tu intervalo "))
limSuperior=(int)(input("Dime el limite superior de tu intervalo "))

while limInferior>limSuperior:
    print("El limite inferior no puede ser mayor que el limite superior")
    limInferior=(int)(input("Dime el limite inferior de tu intervalo "))

num=0
num=(int)(input("Dime un numero"))

while num!=0:
    if lim