capitals = {
    "France": "Paris",
    "Germany": " Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuugart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 4,
        "cities_visited": ["Paris", "Lille", "Dijon"],  
    },
    "Germany": {
        "num_times_visited": 3,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],  
    },
}

print(travel_log["Germany"]["cities_visited"][2])