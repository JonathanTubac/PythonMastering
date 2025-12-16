#global scope
enemies = 1

#Local scope
def increase_enemies(enemy):
    #global enemies, try to avoid naming local variables with global variable names
    enemy = 2
    print(f"enemies inside function: {enemy}")
    return enemy

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")