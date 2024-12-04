import re

patron_mult = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
patron_do = re.compile(r'do\(\)')
patron_dont = re.compile(r'don\'t\(\)')

with open('acertijo3.txt', 'r') as file:
	lineas = file.readlines()

total = 0
habilitar = True
for linea in lineas:
	i = 0
	while (i < len(linea)):
		if (patron_do.match(linea, i)):
			habilitar = True
			i += 4
		elif (patron_dont.match(linea, i)):
			habilitar = False
			i += 6
		elif (habilitar == True):
			match = patron_mult.match(linea, i)
			if (match):
				x, y = map(int, match.groups())
				"""print(f"Encontrado mult({x}, {y})\n")"""
				total += x * y
				i += match.end() - match.start()
			else:
				i += 1
		else:
			i += 1


print(f"El total es: {total}\n")