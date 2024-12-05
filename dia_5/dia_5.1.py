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

# Leo las reglas.
with open('acertijo5_reglas.txt', 'r') as file:
	rules_input = file.read()

# Leo las actualizaciones.
with open('acertijo5_actualizaciones.txt', 'r') as file:
    updates_input = file.readlines()

# Llamo al parseo de reglas y lo guardo en una variable
rules = parse_rules(rules_input)

# Aquí me salto las comas y mapeo a ints las actualizaciones.
updates_input = [list(map(int, update.strip().split(','))) for update in updates_input if update.strip()]

# Se inicializa una lista para guardas las actualizaciones correctas.
correct_updates = []
# Creo un bucle for para verificar las actualizaciones correctas e ir guardandonlas.
for update in updates_input:
    if (is_order_correct(update, rules)):
        correct_updates.append(update)

# Llamo a la función para encontrar el número de en medio de las actualizaciones e ir guardándolas.
middle_pages = [find_middle_page(update) for update in correct_updates]

# Calculo la suma total de los números de en medio de las actualizaciones.
result = sum(middle_pages)

#print("Correct Updates:", correct_updates)
#print("Middle Pages:", middle_pages)
print("El total es:", result)
