'''Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.
'''

producto=10
i=0
contador=0
precio=0

for i in range(0,20):
    contador+=1
    print("El", contador ,"º mes tienes que pagar=>",producto, "€")
    producto*=2
    precio=producto+precio

print("El total de lo quer has pagado despues de los 20 meses:" ,precio, "€")                                   