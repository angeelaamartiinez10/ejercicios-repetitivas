'''Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el
sueldo que recibirá por las horas trabajadas.
'''
hdias=0
htotales=0
sueldo=0

sueldo=(int)(input("¿Qué sueldo recibes por hora?"))

for i in range (0,6):
    hdias=(int)(input("¿Cuántas horas has trabajado hoy?"))
    htotales=hdias+htotales
sueldo=sueldo*htotales

print("Tu sueldo total es", sueldo, "€ y el total de horas que has trabajado es:", htotales)