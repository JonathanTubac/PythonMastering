import random as rd

print("Welcome to the game! 0 rock, 1 paper, 2 scissors")

options = ["Rock", "Paper", "Scissors"]
user_option = int(input("Enter your decision: "))
computer_decision = rd.randint(0, 2)

print("Your decision: " + options[user_option])
print("Computer option: " + options[computer_decision])
if (user_option == 0 and computer_decision == 1) or (user_option == 1 and computer_decision == 2) or (user_option == 2 and computer_decision == 0):
    print("You lose")
elif user_option == computer_decision:
    print("Draw")
elif (user_option == 0 and computer_decision == 2) or (user_option == 1 and computer_decision == 0) or (user_option == 2 and computer_decision == 1):
    print("you win!")
