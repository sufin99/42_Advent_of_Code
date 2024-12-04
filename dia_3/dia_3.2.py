import re

# Creo varios patrones para: mul(x, y), do() y don't().
patron_mult = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
patron_do = re.compile(r'do\(\)')
patron_dont = re.compile(r'don\'t\(\)')

with open('acertijo3.txt', 'r') as file:
	lineas = file.readlines()

total = 0
habilitar = True # Dejo habilitar en True para que las multiplicaciones esten activas desde el principio.
for linea in lineas:
	i = 0
	# Creo un while para ver si encuentra uno de los patrones antes mencionados usando una cadena de ifs.
	while (i < len(linea)):
		# Si encuentro un do() activo las multiplicaciones y me salto el número de caracteres que tiene este patrón.
		if (patron_do.match(linea, i)):
			habilitar = True
			i += 4
		# Si encuentro un don't() desactivo las multiplicaciones y me salto el num de caracteres que tiene este patrón.
		elif (patron_dont.match(linea, i)):
			habilitar = False
			i += 6
		# Si no encuentra ninguno de los patrones anteriores y las multiplicaciones están activas se hace la multiplicación.
		elif (habilitar == True):
			match = patron_mult.match(linea, i)
			# Si encuentra la multiplicación se multiplica y se suma su resultado a total. Y se salta el num de caracteres de este patrón.
			if (match):
				x, y = map(int, match.groups())
				#print(f"Encontrado mult({x}, {y})\n")
				total += x * y
				i += match.end() - match.start()
			# Si no encuentra el patrón aunque este habilitado la multiplicación se va saltando los caracteres.
			else:
				i += 1
		# Si no encuentra do() ni don't() y las multiplicaciones están desactivadas se va saltando los caracteres.
		else:
			i += 1


print(f"El total es: {total}\n")