'''
Crea una aplicación que pida un número y calcule su factorial (El factorial de un
número es el producto de todos los enteros entre 1 y el propio número y se
representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
1x2x3x4x5=120),
'''

'''
num=0
num=(int)(input("Dime un número "))

resultado=1

for fact in range(1,num+1):     #fact--->variable donde se va a inicializar (1.2.3...)
    resultado=resultado*fact
print ("El factorial de " ,num, "es" ,resultado,)


'''


#SE PUEDE HACER TMB CON EL BUCLE WHILE       (no funciona)

resultado=1
num=0
contador=num

num=(int)(input("Dime un número "))

while(contador>0):
    resultado*=contador
    contador-=1
print ("El factorial de " ,num, "es" ,resultado,)