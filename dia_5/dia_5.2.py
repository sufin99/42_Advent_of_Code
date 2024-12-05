# Importo defaultdict de collections para crear un diccionario que inicializa automáticamente un conjunto
# vacío para cada nueva clave.
from collections import defaultdict

# Le paso las reglas en forma de cadena de texto. 
def parse_rules(rules):
	# Creo el diccionario con defaultdict.
	order_rules = defaultdict(set)
	# Creo un bucle for para saltarme el salto de línea y añadir los números a int saltandome '|'.
	# Voy añadiendo y al conjunto de x en el diccionario
	for rule in rules.split('\n'):
		if (rule.strip()):
			before, after = map(int, rule.split('|'))
			order_rules[after].add(before)
	return (order_rules)

# Creo una función para ver si una actualización está en el orden correcto según las reglas.
def is_order_correct(update, rules):
	# Creo un diccionario que maoea cada página a su índice en la lista.
	index_map = {page: i for i, page in enumerate(update)}
	# Creo un bucle for para iterar sobre cada par en las reglas. Si el indicde de before es mayor que after
	# retorna False porque tiene que ir antes.
	for after, befores in rules.items():
		if (after in index_map):
			for before in befores:
				if (before in index_map and index_map[before] > index_map[after]):
					return (False)
	return (True)

# Creo una función para encontrar el número que está en la mitad de la actualización.
def find_middle_page(update):
    return (update[len(update) // 2])

# Creo una función para ordenar una actualización incorrecta según las reglas.
def sort_update(update, rules):
	# Creo una lista vacía para ir guardando las actualizaciones cuando se ordenen y se validen. Y remaining tiene todas
	# las páginas de update para ver que actualizaciones queda por ordenar y dejarlas válidas.
	sorted_update = []
	remaining = set(update)
	# Creo un bucle while para vaciar remaining.
	while (remaining):
		# Creo un bucle for para iterar en una copia de remaining.
		for page in list(remaining):
			# Se verifica si todas las páginas que deben precederla ya han sido ordenadas. Si no estan en remaining.
			if (all(before not in remaining for before in rules[page])):
				# Si la página cumple con las reglas, se agrega a sorted_update y se elimina de remaining.
				sorted_update.append(page)
				remaining.remove(page)
	#print(sorted_update)
	return (sorted_update)

# Leo las reglas.
with open('acertijo5_reglas.txt', 'r') as file:
	rules_input = file.read()

# Leo las actualizaciones.
with open('acertijo5_actualizaciones.txt', 'r') as file:
    updates_input = file.readlines()

# Llamo al parseo de reglas y lo guardo en una variable
rules = parse_rules(rules_input)

# Aquí me salto las comas y mapeo a ints las actualizaciones.
updates_input = [list(map(int, update.strip().split(','))) for update in updates_input if (update.strip())]

# Se inicializa una lista para guardar las actualizaciones incorrectas.
incorrect_updates = []
# Creo un bucle for para verificar las actualizaciones incorrectas e ir guardándolas.
for update in updates_input:
	if (not is_order_correct(update, rules)):
		incorrect_updates.append(update)

# Ordeno las actualizaciones incorrectas y encuentro los números de página del medio.
sorted_incorrect_updates = [sort_update(update, rules) for update in incorrect_updates]

# Llamo a la función para encontrar el número de en medio de las actualizaciones anteriormente incorrectas e ir guardándolas.
middle_pages_incorrects = [find_middle_page(update) for update in sorted_incorrect_updates]

# Calculo la suma total de los números de en medio de las actualizaciones.
result_incorrects = sum(middle_pages_incorrects)

print("EL total es: ", result_incorrects)
