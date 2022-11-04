'''
Escribe un programa que dados dos números, uno real (base) y un entero
positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
utilizar el operador de potencia.
'''

base=0
exponente=0
solucion=1

base=(float)(input("Dime la base ")) #float--> numeros reales
exponente=(int)(input("Dime un exponente "))


for i in range (0,exponente):
    solucion=solucion*base
print("la solucion es ",solucion)