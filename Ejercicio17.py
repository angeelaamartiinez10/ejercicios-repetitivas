'''Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados.'''

horas=0
dias=0
trabajadores=0
sueldo=0

total=0

horas=(int)(input("¿Cuántas horas trabajas al día?"))
dias=(int)(input("¿Cuántos días trabajas?"))
trabajadores=(int)(input("¿Cuántos trabajadores hay en la empresa?"))
sueldo=(int)(input("¿Cuanto se cobra por hora?"))

for i in range(0,dias):
    total=total+(horas*sueldo)

print("Esta semana tu sueldoes:",total)
print("Por" ,trabajadores, " la empresa ha pagado:" ,trabajadores*total,)



