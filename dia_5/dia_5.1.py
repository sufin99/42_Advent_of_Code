from collections import defaultdict

def parse_rules(rules):
    """Parse the rules into a dictionary."""
    order_rules = defaultdict(set)
    for rule in rules.split('\n'):
        if rule.strip():
            before, after = map(int, rule.split('|'))
            order_rules[after].add(before)
    return order_rules

def is_order_correct(update, rules):
    """Check if an update is in correct order based on the rules."""
    index_map = {page: i for i, page in enumerate(update)}
    for after, befores in rules.items():
        if after in index_map:
            for before in befores:
                if before in index_map and index_map[before] > index_map[after]:
                    return False
    return True

def find_middle_page(update):
    """Find the middle page of a correctly ordered update."""
    return update[len(update) // 2]

def main():
    # Input rules and updates
    with open('acertijo5_actualizaciones.txt', 'r') as file:
        updates_input = file.readlines()
    
    with open('acertijo5_reglas.txt', 'r') as file:
    	rules_input = file.read()

    # Parse the rules
    rules = parse_rules(rules_input)
    
    updates_input = [list(map(int, update.strip().split(','))) for update in updates_input if update.strip()]

    # Process updates
    correct_updates = []
    for update in updates_input:
        if is_order_correct(update, rules):
            correct_updates.append(update)

    # Find the middle pages of correctly ordered updates
    middle_pages = [find_middle_page(update) for update in correct_updates]

    # Calculate the sum of middle pages
    result = sum(middle_pages)

    print("Correct Updates:", correct_updates)
    print("Middle Pages:", middle_pages)
    print("Sum of Middle Pages:", result)

if __name__ == "__main__":
    main()


