with open('acertijo1.txt', 'r') as file:
	lineas = file.readlines()

numeros1 = []
numeros2 = []
for linea in lineas:
	partes = linea.split()
	num1 = int(partes[0])
	num2 = int(partes[1])
	numeros1.append(num1)
	numeros2.append(num2)

primera_columna = sorted(numeros1)
"""for i in range(len(primera_columna)):
	print("Columna 1: ", primera_columna[i])"""
segunda_columna = sorted(numeros2)
"""for i in range(len(primera_columna)):
	print("Columna 1: ", segunda_columna[i])"""

total = 0
for i in range(len(primera_columna)):
	if (primera_columna[i] >= segunda_columna[i]):
		resultado = primera_columna[i] - segunda_columna[i]
	elif (segunda_columna[i] > primera_columna[i]):
		resultado = segunda_columna[i] - primera_columna[i]
	resultado = abs(primera_columna[i] - segunda_columna[i])
	total += resultado
"""	print(total, "\n")"""

print("El total es: ", total, "\n")