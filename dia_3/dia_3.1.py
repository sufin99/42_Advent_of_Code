import re
# Creo un patrón y lo guardo que sería: mul(x , y) donde x e y pueden ser números de entre 1 y 3 cifras.
patron = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

with open('acertijo3.txt', 'r') as file:
	lineas = file.readlines()

total = 0
# Creo un bucle for para encontrar ese mismo patrón línea por línea.
for linea in lineas:
	coincidencias = patron.findall(linea)
	# Creo otro bucle for para que todas las coincidencias que se encuentren en cada línea
	# los convierta en ints y los vaya sumando el resultado de su multiplicación en el total.
	for coincidencia in coincidencias:
		x, y = map(int, coincidencia)
		#print(f"Encontrado mult({x}, {y})\n")
		total += x * y

print(f"El total es: {total}\n")
	