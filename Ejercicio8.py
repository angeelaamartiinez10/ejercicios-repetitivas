'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
*La suma de los números que están dentro del intervalo (intervalo abierto).
*Cuantos números están fuera del intervalo.
*He informa si hemos introducido algún número igual a los límites del intervalo.
'''


#funcion que devuelve una lista de números introducidos

def pideNumeros():
    vNum=[]
    num=1
    while (num!=0):
        try:
            contador=len(vNum)
            num=(int)(input(f"Dime el numero {contador} : "))
            vNum.append(num)
        except:
            print("Tienes que introducir numeros")
    return vNum


def realizarCalculos(vDatos,limInferior,limSuperior):
    suma=0
    fuera=0
    igualLim=0
    vLimites= list(range(limInferior+1,limSuperior))
    for i in vDatos:
        if (i in vLimites):
            suma+=i
        else:
            fuera+=1
            if (i == limInferior or i == limSuperior):
                igualLim +=1
    print("La suma total dentro de los límites es:",suma)
    print("Has introducido",fuera,"números fuera de los limites")
    print ("Has introducido",igualLim," iguales a los limites")





limInferior=1
limSuperior=0

while limInferior>limSuperior:
    try: #para que si pones una letra te de error
        limInferior=(int)(input("Dime el limite inferior de tu intervalo "))
        limSuperior=(int)(input("Dime el limite superior de tu intervalo "))
        if limInferior>limSuperior:
            print("Es obligatorio qeu el limite infeior")
    except:
        print("TIenes que introducir numeros")

#pido los numeros

vNum=pideNumeros()

#realizar calculos

realizarCalculos(vNum,limInferior,limSuperior)