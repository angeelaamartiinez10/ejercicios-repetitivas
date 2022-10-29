'''Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
números a introducir). El programa debe informar de cuantos números
introducidos son mayores que 0, menores que 0 e iguales a 0.
'''

cantidadNumeros=0
cantidadNumeros=(int)(input("¿Cuántos numeros deseas añadir? "))

contadormayores=0
contadormenores=0
contadorigual=0

contador=0
num=int

while (contador!=cantidadNumeros):
    num=(int)(input("Dime un número "))
    if num>0:
        contadormayores+=1
    elif num<0:
        contadormenores+=1
    elif num==0:
        contadorigual+=1
    contador+=1

print("El número de numeros mayores es: ",contadormayores)
print("El número de numeros menores es: ",contadormenores)
print("El número de numeros iguales es: ",contadorigual)
