'''Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
al final de cada mes deposita cantidades variables de dinero; además, se quiere
saber cuánto lleva ahorrado cada mes.
'''
ahorromes=0
ahorroaño=0

vMes=[]

for i in range(0,12):
    ahorromes=(int(input("¿Cúanto has ahorrado este mes? " )))
    ahorroaño=ahorromes+ahorroaño
    vMes=ahorroaño
    print("Llevas ahorrado: ",vMes, "€")

print("Este año has ahorrado: ",ahorroaño, "€")
