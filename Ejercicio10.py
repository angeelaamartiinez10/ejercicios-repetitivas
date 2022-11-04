#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

'''for i in range (0,11):
    resultado=i*tabla1
    print("
    '''


for i in range(1,6):
	print(f'Tabla de multiplicar del {i}:') 
	for b in range(0, 11):
		print(f'{i} x {b} = {i * b}')