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

def es_seguro_del_1(numeros):
	secure2 = 0
	for i in range(len(numeros)):
		new_list = numeros[:i] + numeros[i+1:]
		if (es_seguro(new_list)):
			secure2 = 1
	return (secure2)

with open('acertijo2.txt', 'r') as file:
	lineas = file.readlines()

secure = 0
for linea in lineas:
	numeros = []
	partes = linea.split()
	for i in range(len(partes)):
		num = int(partes[i])
		numeros.append(num)
	if (es_seguro(numeros) != 0):
		secure += 1
	elif (es_seguro_del_1(numeros) != 0):
		secure += 1

print("Ahora los niveles seguros son: ", secure)