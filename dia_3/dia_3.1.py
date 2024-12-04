import re

patron = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

with open('acertijo3.txt', 'r') as file:
	lineas = file.readlines()

total = 0
for linea in lineas:
	coincidencias = patron.findall(linea)
	for coincidencia in coincidencias:
		x, y = map(int, coincidencia)
		"""print(f"Encontrado mult({x}, {y})\n")"""
		total += x * y

print(f"El total es: {total}\n")
	