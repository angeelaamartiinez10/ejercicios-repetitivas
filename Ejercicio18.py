'''Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.
'''
import time

for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print(horas,minutos,segundos)
            for i in range(7):
                print()
            time.sleep(1)
            

