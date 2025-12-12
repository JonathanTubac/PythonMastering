import random as rd
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "¡", "*", "+", "-", "."]
password = []

print("Welcome to the password generator!")

n_letters = int(input("How many letters do you want?  "))
n_symbols = int(input("How many symbols do you want? "))
n_numbers = int(input("How many numbers do you want? "))

#easy version, making every for by each character
'''
for letter in range(1, n_letters + 1):
    random_letter = rd.randint(0, len(letters) - 1)
    up_lo_random = rd.randint(0, 1)
    if up_lo_random == 1:
        password.append(letters[random_letter].upper())
    else:
        password.append(letters[random_letter])
for symbol in range(1, n_symbols + 1):
    random_symbol = rd.randint(0, len(symbols) - 1)
    password.append(symbols[random_symbol])
for number in range(1, n_numbers + 1):
    random_number = rd.randint(0, len(numbers) - 1)
    password.append(numbers[random_number])
password_print = ("".join(map(str, password)))
print("Your password is " + password_print) 
'''

#hard version, randomizing the position of each type of character
letters_used = 0
numbers_used = 0
symbols_used = 0

for decision in range(1, (n_letters + n_numbers + n_symbols) + 1):
    available = []
    if letters_used < n_letters:
        available.append("letter")
    if symbols_used < n_symbols:
        available.append("symbol")
    if numbers_used < n_numbers:
        available.append("number")

    random_character = rd.choice(available)

    if random_character == "letter":
        random_letter = rd.randint(0, len(letters) - 1)
        up_lo_random = rd.randint(0, 1)
        if up_lo_random == 1:
            password.append(letters[random_letter].upper())
        else:
            password.append(letters[random_letter])
        letters_used += 1
    elif random_character == "symbol":
        random_symbol = rd.randint(0, len(symbols) - 1)
        password.append(symbols[random_symbol])
        symbols_used += 1
    elif random_character == "number":
        random_number = rd.randint(0, len(numbers) - 1)
        password.append(numbers[random_number])
        numbers_used += 1
print("Your password is " + "".join(map(str, password)))   

#PD: you can use the shuffle() function for randomize the position instead doing this
 