with open('acertijo1.txt', 'r') as file:
	lineas = file.readlines()

numeros1 = []
numeros2 = []
# Creo un bucle for para convertir a ints las 2 columnas y guardarlas en un array de ints
for linea in lineas:
	partes = linea.split()
	num1 = int(partes[0])
	num2 = int(partes[1])
	numeros1.append(num1)
	numeros2.append(num2)

primera_columna = sorted(numeros1) # Ordeno los ints de la primera columna
#for i in range(len(primera_columna)):
#	print("Columna 1: ", primera_columna[i])
segunda_columna = sorted(numeros2) # Ordeno los ints de la segunda columna
#for i in range(len(primera_columna)):
#	print("Columna 1: ", segunda_columna[i])

total = 0
# Creo un bucle for para ir restando los numeros y calcular la distancia e ir suamndo
# el total de las distancias
for i in range(len(primera_columna)):
	if (primera_columna[i] >= segunda_columna[i]):
		resultado = primera_columna[i] - segunda_columna[i]
	elif (segunda_columna[i] > primera_columna[i]):
		resultado = segunda_columna[i] - primera_columna[i]
	total += resultado
#	print(total, "\n")

print("El total es: ", total, "\n")