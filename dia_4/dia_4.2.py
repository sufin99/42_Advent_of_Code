# Creo una función para leer el archivo .txt.
def archivo_leer(filename):	
	with open(filename, 'r') as file:
		matriz = []
		# Creo un bucle for para leer cada línea, elimino los espacios en blanco del principio y final con strip(),
		# convierto la línea en una lista de caracteres con list() y la agrego a la matriz.
		for line in file.readlines():
			texto = list(line.strip())
			matriz.append(texto)
		return (matriz)

# Creo una función para ver que coordenadas coinciden.
def comp_sets(set1, set2):
	count = 0
	for coord in set1:
		if (coord in set2):
			count += 1
	return (count)

# Creo una función para encontrar la palabra en diagonal, también del revés.
def diagonal(matriz, palabra):
	count = 0
	set1 = []
	set2 = []
	n = len(matriz)
	m = len(matriz[0])
	len_palabra = len(palabra)
	# Creo un bucle for para iterar sobre cada fila, hasta (n - len_palabra + 1) para evitar desbordamientos.
	for i in range(n - len_palabra + 1):
		# Creo otro bucle for para iterar sobre cada columna j de la matriz hasta (m - len_palabra + 1)
		# para evitar desbordamientos.
		for j in range(m - len_palabra + 1):
			# En cada if voy guardando las coordenadas de A en set1(diagonal de izquierda a derecha, y del reves tambien) y en set2(diagonal de derecha a izquierda, y del reves tambien). 
			if (all(matriz[i + k][j + k] == palabra[k] for k in range(len_palabra))):
				set1.append((i + 1, j + 1))
			if (all(matriz[i + k][j + k] == palabra[-k-1] for k in range(len_palabra))):
				set1.append((i + 1, j + 1))
			if (all(matriz[i + k][j + len_palabra - k - 1] == palabra[k] for k in range(len_palabra))):
				set2.append((i + 1, j + 1))
			if (all(matriz[i + k][j + len_palabra - k - 1] == palabra[-k-1] for k in range(len_palabra))):
				set2.append((i + 1, j + 1))
	# Guardo las veces que coincide las coordenadas de A entre los 2 sets, que es sinónimo que salen count veces el X-MAS.
	count = comp_sets(set1, set2)
	return (count)

# Creo una función para contar las veces que encuentro la palabra.
def conteo_coordenada(matriz, palabra):
	total = 0
	total += diagonal(matriz, palabra)
	return (total)

matriz = archivo_leer('acertijo4.txt')
palabra = 'MAS'
total_palabra = conteo_coordenada(matriz, palabra)
print(f'XMAS aparece: {total_palabra}\n')