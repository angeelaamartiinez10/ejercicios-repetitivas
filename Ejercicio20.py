'''Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''

'''
EJERCICIO 11
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
    print(num,"no es primo")'''


num=1
divisible=0

primo=(int)(num**(1/2))
contador=(int)(input("¿cuantos números primos quiere mostrar? "))

vPrimos=[]

repe=0
for i in range (1,contador):
    while repe!=contador:
        if (num%i==0):
            True
            divisible+=1
        elif(num%i!=0):
            False
            divisible-=1
        repe+=1        
print("los numeros primos son: ",)
