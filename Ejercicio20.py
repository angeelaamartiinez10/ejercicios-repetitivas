'''Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''

num=0
divisible=0

primo=(int)(num**(1/2))
primos=(int)(input("¿cuantos números primos quiere mostrar?"))


for i in range (1, primos):
    if (num%i==0):
        divisible+=1
print(divisible)