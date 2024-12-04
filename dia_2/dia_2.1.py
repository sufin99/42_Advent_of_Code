with open('acertijo2.txt', 'r') as file:
	lineas = file.readlines()

secure = 0
# Creo un bucle for para separar la string.
for linea in lineas:
	numeros = []
	partes = linea.split()
	# Creo otro bucle for para convertir numero en int e ir guardandolo en un array de ints.
	for i in range(len(partes)):
		num = int(partes[i])
		numeros.append(num)
	# Creo un if que entra solo si se cumple la condición de que la fila de números esta ordenado de forma ascendente o de forma descendente.
	if (sorted(numeros) == numeros or sorted(numeros, reverse=True) == numeros):
		j = 0
		contador = 0
		# Creo un while para comparar los numeros adayacentes si su diferencia es entre 1 y 3.
		while (j < len(numeros) - 1):
			if (abs(numeros[j] - numeros[j + 1]) in [1, 2, 3]):
				contador += 1
			j += 1
		# Si el contador es igual a j es que todas las diferencias entre los números adyacentes
		# cumple la condición de que esa línea es segura.
		# Y voy contando cuantas lineas son seguras.
		if (contador == j):
			secure += 1

print("Los niveles seguros son: ", secure)