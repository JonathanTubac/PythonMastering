import random as rd

#GLobal constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

#Global variables
lifes = 0
game = True
choose_diff = True

#Function to check the user number with the random number
def estimate_number(number, user_number):
    if user_number < number:
        return "Too low"
    elif user_number > number:
        return "Too high"
    else:
        return "Correct!"

#Fucntion to set the difficulty
def set_difficulty(diff):
    if diff == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif diff == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("---enter a valid option---")
        return 0

print("Welcome to the number guessing game!")
print("I'm thinking in a number between 1 and 100")
number = rd.randint(1, 100)

while choose_diff:
    difficult = input("Choose a difficulty. 'easy' or 'hard': ").lower()
    lifes = set_difficulty(difficult)
    if lifes != 0:
        choose_diff = False
        
while game:
    if lifes == 0:
        print("Sorry, you lose")
        game = False
        continue
    print(f"You have {lifes} attempts remaining")
    user_guess = int(input("Make your guess: "))
    print(estimate_number(number, user_guess))
    if user_guess == number:
        print("Congrats! i was thinking in that number")
        game = False
    elif user_guess != number:
        lifes -= 1