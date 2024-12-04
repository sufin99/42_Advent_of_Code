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

total = 0
# Creo un bucle for para ir viendo cuantas veces sale el mismo número
for i in range(len(numeros1)):
	multiplicador = 0
	# Creo un segundo bucle for para la comparativa e ir aumenatando el multiplicador
	for j in range(len(numeros2)):	
		if (numeros1[i] == numeros2[j]):
			multiplicador += 1
	# Sumo todos los resultados de las multiplicaciones
	total += (numeros1[i] * multiplicador)

print("El resultado es: ", total)
	