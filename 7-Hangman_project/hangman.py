import random as rd

#global variables
words = ["Hello", "Python", "CSharp", "Password"]
random_word = list(rd.choice(words).lower())
lifes = 6
game = False
user_guess = []

#Functions
def header(text):
    print("********" + text + "********")

#Logic
header("Welcome to hangman game")

for letter in random_word:
    user_guess.append("_")

while game != True:
    if lifes == 0:
        game = True
        header("You lose, you don't have more lifes!")
        continue
    elif "_" not in user_guess:
        game = True
        header("You win, you guessed the word " + "".join(map(str, random_word)))
        continue
        
    print("The secret word is: " + " ".join(map(str, user_guess)))
    user_letter = input("Guess a letter: ").lower()
    
    if user_letter in random_word:
        index = 0
        for letter in random_word:
            if user_letter == letter:
                user_guess[index] = letter
            else:
                pass
            index += 1
    else:
        lifes -= 1
        header("You guessed wrong! you lose a life")
        print("Curret lifes " + str(lifes) + "/6")