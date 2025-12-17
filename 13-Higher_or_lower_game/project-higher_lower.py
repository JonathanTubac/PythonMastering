import random as rd
import game_data as gd
import os
import platform

#Global variables
game = True
score = 0

#Function for cleaning console in Linux or Windows
def clean_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#Function to choose a random artist from the list
def choose_random_artist(artists):
    random_index = rd.randint(0, len(artists) - 1)
    random_artist = artists[random_index]
    artists.pop(random_index)
    return random_artist

#Initial random artist
first_artist = choose_random_artist(gd.artists)

while game:
    clean_console()
    
    if len(gd.artists) == 0:
        game = False
        print("Congtrats! you win, you guessed all correctly")
        print(f"Your score: {score}")

    user_decision_menu = True
    print("Welcome to, who has more follores on instagram?")
    print(f"Actual score: {score}")
    print("---A. Compare " + first_artist["name"] + ", " + first_artist["description"] + " from " + first_artist["country"] + "---")
    second_artist = choose_random_artist(gd.artists)
    print("VS")
    print("---B. Compare " + second_artist["name"] + ", " + second_artist["description"] + " from " + second_artist["country"] + "---")
    
    while user_decision_menu:
        user_decision = input("Who has more followers, A or B? ").lower()
        if user_decision == "a":
            if first_artist["followers"] > second_artist["followers"]:
                score += 1
                pass
            else:
                game = False
                print(f"Sorry, you lose. " + second_artist["name"] + " has more followers than " + first_artist["name"] + f". Your final score: {score}")
            user_decision_menu = False
        elif user_decision == "b":
            if second_artist["followers"] > first_artist["followers"]:
                first_artist = second_artist
                score += 1      
                pass
            else:
                game = False
                print("Sorry, you lose. " + first_artist["name"] + " has more followers than " + second_artist["name"] + f". Your final score: {score}")
            user_decision_menu = False
        else:
            print("Enter a valid option")
    