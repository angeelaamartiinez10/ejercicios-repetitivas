'''Escribe un programa que diga si un número introducido por teclado es o no
primo. Un número primo es aquel que sólo es divisible entre él mismo y la
unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
es divisible por algún otro número
'''

num=0
primo=0
divisible=0

num=(int)(input("Dime un numero "))
primo=(int)(num**(1/2))

for i in range (1, primo+1):
    if (num%i==0):
        divisible+=1

if(primo==1):
    print(num,"es primo")
else:
    print(num,"no es primo")