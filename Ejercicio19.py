'''Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.'''

#import itertools  # para rangos infinitos

opcion=0

print("*****MENU*****")
print("opcion1 pulsa1.")
print("opcion2 pulsa2.")
print("opcion3. pulsa3.")
print("para salir. pulsa 0.")
print("*********")
opcion=(int)(input("elige una opcion\n"))

while opcion!=0: 
    print("*****MENU*****")
    print("opcion1 pulsa1.")
    print("opcion2 pulsa2.")
    print("opcion3. pulsa3.")
    print("para salir. pulsa 0.")
    print("*********")
    opcion=(int)(input("elige una opcion\n"))
   
print("programa terminado")
