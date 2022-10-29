'''Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,a
demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.
'''

import random
numero=random.randint(1,100)
print (numero)

contador=1
num=0
num=(int)(input("Dime un numero "))

while(contador<=9 and num!=numero):
    if num!=numero and num<numero:
        print("EL número aleatorio es mayor")
    elif num!=numero and num>numero:
        print("El numero aleatorio es menor")        

    num=(int)(input("Dime otro numero "))
    contador +=1
    print("Llevas",contador, "intentos")

if contador==10 and num!=numero:
    print("Lo siento has agotado tus 10 intentos")
else:
    print("HAS ACERTADO.El numero aleatorio es: " ,numero,)
