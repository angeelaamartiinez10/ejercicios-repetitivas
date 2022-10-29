'''Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
en caso contrario, el programa termina cuando se introduce un espacio.
'''


caracter=""

caracter=(input("Dime una letra"))
contadorV=0
contadorN=0

while caracter!="":
    if caracter.lower() in "aeiou":
        contadorV+=1
    else:
        contadorN+=1
    caracter=(input("Dime una letra"))


print("Hay",contadorV, "vocales y",contadorN, "que no son vocales")