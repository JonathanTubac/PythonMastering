def greet_with_name(name, location):
    print("Hello " + name)
    print(f"What is it like in {location}")

greet_with_name(location = "United States" , name = "Jonathan")

def calculate_love_score(name1, name2):
    n1 = list(name1.lower())
    n2 = list(name2.lower())
    true_counter = 0
    love_counter = 0
    for letter in n1:
        if letter == "t":
            true_counter += 1
        elif letter == "r":
            true_counter += 1
        elif letter == "u":
            true_counter += 1
        elif letter == "e":
            true_counter += 1
            love_counter += 1
        elif letter == "l":
            love_counter += 1
        elif letter == "o":
            love_counter += 1
        elif letter == "v":
            love_counter += 1
        else:
            pass
    for letter in n2:
        if letter == "t":
            true_counter += 1
        elif letter == "r":
            true_counter += 1
        elif letter == "u":
            true_counter += 1
        elif letter == "e":
            true_counter += 1
            love_counter += 1
        elif letter == "l":
            love_counter += 1
        elif letter == "o":
            love_counter += 1
        elif letter == "v":
            love_counter += 1
        else:
            pass   
        
    print(str(true_counter) + str(love_counter))
    
calculate_love_score("Kanye West", "Kim Kardashian")
    