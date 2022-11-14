'''Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''


num=0
divisible=0

primo=(int)(num**(1/2))
contador=(int)(input("¿cuantos números primos quiere mostrar? "))

vPrimos=[]

while contador!=0:
    for i in range (1, primo+1):
        if (num%i==0):
            divisible+=1
    contador-=1
    vPrimos=divisible







print("los numeros primos son: ",vPrimos)
