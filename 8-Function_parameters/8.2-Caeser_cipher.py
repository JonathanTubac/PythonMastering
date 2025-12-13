alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
menu = False

#This function return the message encrypted
def encrypt(message, shift):
    #we convert the message into a list with lower case
    m = list(message.lower())
    index = 0
    for letter in m:
        #Check if its a letter
        if letter.isalpha():
            #we calculte the modulo 26 to get the shifted letter index
            m[index] = alphabet[(alphabet.index(letter) + shift) % 26]
        else:
            pass
        #We increment the index for each iteraction
        index += 1
    #we return the list joined
    return "".join(map(str, m))
        
#This function return the message decrypted
def decrypt(message, shift):
    #we convert the message into a list with lower case
    m = list(message.lower())
    index = 0
    for letter in m:
        #Check if its a letter
        if letter.isalpha():
            #we calculte the modulo 26 to get the shifted letter index
            m[index] = alphabet[(alphabet.index(letter) - shift) % 26]
        else:
            pass
        #We increment the index for each iteraction
        index += 1
    #we return the list joined
    return "".join(map(str, m))



while menu != True:
    
    instruction = input("Type 'encrypt' or 'decrypt': ").lower()
    if instruction != "encrypt" and instruction != "decrypt":
        print("Please enter a valid option")
        continue
    else:
        shifts = int(input("How many shifts do you want? "))
        message = input("Type your message: ").lower()

    if instruction == "encrypt":
        en_message = encrypt(message, shifts)
        print("your encrypted message: " + en_message)
    elif instruction == "decrypt":
        de_message = decrypt(message, shifts)
        print("your decrypted message: " + de_message)
    else:
        pass
    continue_menu = input("Type yes to try again or no to exit: ").lower()
    if continue_menu == "no":
        menu = True
    else:
        pass
    


