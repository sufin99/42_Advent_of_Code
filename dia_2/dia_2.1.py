with open('acertijo2.txt', 'r') as file:
	lineas = file.readlines()

secure = 0
for linea in lineas:
	numeros = []
	partes = linea.split()
	for i in range(len(partes)):
		num = int(partes[i])
		numeros.append(num)
	if (sorted(numeros) == numeros or sorted(numeros, reverse=True) == numeros):
		j = 0
		contador = 0
		while (j < len(numeros) - 1):
			if (abs(numeros[j] - numeros[j + 1]) in [1, 2, 3]):
				contador += 1
			j += 1
		if (contador == j):
			secure += 1

print("Los niveles seguros son: ", secure)