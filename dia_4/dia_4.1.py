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

# Creo una función para encontrar la palabra en horizontal, también del revés.
def horizontal(matriz, palabra):
	count = 0
	n = len(matriz) # Numero de filas.
	m = len(matriz[0]) # Numero de columnas.
	len_palabra = len(palabra)
	# Creo un bucle for para iterar sobre cada fila i de la matriz.
	for i in range(n):
		# Creo otro bucle for para iterar sobre cada columna j de la matriz hasta (m - len_palabra + 1)
		# para evitar desbordamientos.
		for j in range(m - len_palabra + 1):
			# Uso all() para verificar si la palabra coincide horizontalmente. El segundo if es para buscar la
			# palabra en el lado contrario.
			if all(matriz[i][j + k] == palabra[k] for k in range(len_palabra)):
				count += 1
			if all(matriz[i][j + k] == palabra[-k-1] for k in range(len_palabra)):
				count += 1
	return (count)

# Creo una función para encontrar la palabra en vertical, también del revés.
def vertical (matriz, palabra):
	count = 0
	n = len(matriz) # Numero de filas.
	m = len(matriz[0]) # Numero de columnas.
	len_palabra = len(palabra)
	# Creo un bucle for para iterar sobre cada fila, hasta (n - len_palabra + 1) para evitar desbordamientos.
	for i in range(n - len_palabra + 1):
		# Creo otro bucle for para iterar sobre cada columna j.
		for j in range(m):
			# Uso all() para verificar si la palabra coincide verticalmente. El segundo if es para buscar la
			# palabra en el lado contrario.
			if all(matriz[i + k][j] == palabra[k] for k in range(len_palabra)):
				count += 1
			if all(matriz[i + k][j] == palabra[-k-1] for k in range(len_palabra)):
				count += 1
	return (count)

# Creo una función para encontrar la palabra en diagonal, también del revés.
def diagonal(matriz, palabra):
	count = 0
	n = len(matriz)
	m = len(matriz[0])
	len_palabra = len(palabra)
	# Creo un bucle for para iterar sobre cada fila, hasta (n - len_palabra + 1) para evitar desbordamientos.
	for i in range(n - len_palabra + 1):
		# Creo otro bucle for para iterar sobre cada columna j de la matriz hasta (m - len_palabra + 1)
		# para evitar desbordamientos.
		for j in range(m - len_palabra + 1):
			if all(matriz[i + k][j + k] == palabra[k] for k in range(len_palabra)):
				count += 1
			if all(matriz[i + k][j + k] == palabra[-k-1] for k in range(len_palabra)):
				count += 1
			if all(matriz[i + k][j + len_palabra - k - 1] == palabra[k] for k in range(len_palabra)):
				count += 1
			if all(matriz[i + k][j + len_palabra - k - 1] == palabra[-k-1] for k in range(len_palabra)):
				count += 1
	return (count)

# Creo una función para contar las veces que encuentro la palabra.
def conteo_palabra(matriz, palabra):
	total = 0
	total += horizontal(matriz, palabra)
	total += diagonal(matriz, palabra)
	total += vertical(matriz, palabra)
	return (total)

matriz = archivo_leer('acertijo4.txt')
palabra = 'XMAS'
total_palabra = conteo_palabra(matriz, palabra)
print(f'XMAS aparece: {total_palabra}\n')