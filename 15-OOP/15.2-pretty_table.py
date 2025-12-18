import prettytable as ptab

table = ptab.PrettyTable()
pokemons = ["Pikachu", "Squirtle", "Charmander"]
table.add_column("Pokemon name", pokemons)
table.add_column("Type", ["Electro", "Water", "Fire"])
table.align["Pokemon name"] = "l"
table.align["Type"] = "l"
print(table)