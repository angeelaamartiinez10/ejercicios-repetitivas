'''Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados
'''

horas=0
trabajadores=0
sxh=0
semanal=0
pago=0

horas=(int)(input("¿Cuántas horas trabaja cada dia? "))
trabajadores=(int)(input("¿Cuántos trabajadores tiene la empresa? "))
sxh=(int)(input("¿Cúanto es tu sueldo por hora? "))


for i in range(0,5): #trabaja 5 dias a la semana
    semanal=semanal+(sxh*horas)
pago=trabajadores*semanal
print("El sueldo semanal que recibe un trabajador es:" ,semanal)
print("La empresa paga trabajador",pago, "por los", trabajadores, " trabajadores que hay en la empresa")