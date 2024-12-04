# Creo una función con la misma funcionalidad de la parte uno para ver que líneas son seguras.
def es_seguro(numeros):
	secure1 = 0
	if (sorted(numeros) == numeros or sorted(numeros, reverse=True) == numeros):
			j = 0
			contador = 0
			while (j < len(numeros) - 1):
				if (abs(numeros[j] - numeros[j + 1]) in [1, 2, 3]):
					contador += 1
				j += 1
			if (contador == j):
				secure1 += 1
	return (secure1)

# Creo una función para comprobar que si eliminando un int de cada fila se puede convertir en seguro
def es_seguro_del_1(numeros):
	secure2 = 0
	# Creo un bucle for para ir eliminando el número de la posisción i.
	for i in range(len(numeros)):
		new_list = numeros[:i] + numeros[i+1:]
		# Al eliminar el número de la posición i se llama a la función para comprobar si así se convierte en segura.
		# Si no es segura se prueba eliminando otro número para comprobar si así es segura y así sucesivamente.
		if (es_seguro(new_list)):
			secure2 = 1
			return (secure2)
	return (secure2)

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
	# Creo una cadena de if-elif que si es seguro sumo uno al contador de líneas seguras.
	# Si no es seguro entro a la función para comprobar si eliminando un número de la fila se puede convertir en seguro.
	# Si se cumple bien la segunda condición se suma uno más al contador.
	if (es_seguro(numeros) != 0):
		secure += 1
	elif (es_seguro_del_1(numeros) != 0):
		secure += 1

print("Ahora los niveles seguros son: ", secure)