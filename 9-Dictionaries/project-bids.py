import os
import platform

people = {}
other_person = False

def clean_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def find_highest_bid(people_dictionary):
    max_bid = 0
    max_bidder = ""
    for person in people_dictionary:
        bid_am = people_dictionary[person]
        if bid_am > max_bid:
            max_bid = bid_am
            max_bidder = person
        else:
            pass
    max_bidder_list = [max_bidder, max_bid]
    return max_bidder_list

print("Welcome to the bids program!")
while not other_person:
    user = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    
    people[user] = bid

    continue_people = input("is there other person? y or n: ")
    
    if continue_people == "n":
        other_person = True
    else:
        clean_console()
        
max_bidder = find_highest_bid(people)

print(f"The winner is {max_bidder[0]} with a bif of ${max_bidder[1]}")

   
    
