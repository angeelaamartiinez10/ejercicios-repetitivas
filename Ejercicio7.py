#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num1=0

num1=(int)(input("Dime un numero"))

print("la tabla de multiplicar de" ,num1, "es:")

for num in range (0,11):
    print (num1*num)

