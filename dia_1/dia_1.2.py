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

total = 0
for i in range(len(numeros1)):
	multiplicador = 0
	for j in range(len(numeros2)):	
		if (numeros1[i] == numeros2[j]):
			multiplicador += 1
	total += (numeros1[i] * multiplicador)

print("El resultado es: ", total)
	