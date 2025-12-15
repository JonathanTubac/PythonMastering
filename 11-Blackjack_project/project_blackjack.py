import random as rd

#This function will return a random card generated in the list
def generate_random_card(cards, current_hand):
    random_card = rd.choice(cards)
    '''
    the card with value 11 in the list is an ace, 
    this card change its value to 1 or 11, 
    depending the situation, we validate this here
    '''
    if sum(current_hand) == 10 and random_card == 11:
        random_card = 11
    elif sum(current_hand) > 10 and random_card == 11:
        random_card = 1
    return random_card

#This function will add a card into someone hand
def append_random_card(r_card, current_hand):
    current_hand.append(r_card)

#This function will generate the dealer's hand after standing
def generate_dealer_hand(dealer_hand):
    while sum(dealer_hand) < 17:
        random_dealer_card = generate_random_card(cards, dealer_hand)
        append_random_card(random_dealer_card, dealer_hand)
 
#list of cards, 11 is an Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#repeat until game is false
game = True
initial_credits = 1000
while game:
    #in game variables
    menu_bet = True
    stand = False
    lose = False
    user_bet = 0
    user_hand = []
    dealer_hand = []
    initial_bet_menu = True
    
    #Repeat until user refuses to add more to his bet
    while menu_bet:
        print("---Credits: " + str(initial_credits) + "---")
        print(f"Actual bet: {user_bet}")
        if user_bet == 0:
            while initial_bet_menu:
                user_bet = int(input("Enter your bet: "))
                if user_bet > initial_credits:
                    print("---you don't have that amount of credits yet, try again---")
                    print(f"---Credits: {initial_credits}---")
                else:
                    initial_bet_menu = False
                    initial_credits -= user_bet
        else:
            user_bet_add = int(input("How much do you want to add?: "))
            if user_bet_add <= initial_credits:
                user_bet += user_bet_add
                initial_credits -= user_bet_add
            else:
                print("---this amount exceed your available credits---")
        more_bet = input("Do you want to add more to your bet? y or n: ").lower()
        if more_bet == "n":
            menu_bet = False
        elif more_bet == "y":
            pass
        else:
            print("---Enter a valid option---")
    print(f"Your bet: {user_bet}")
    
    #first 2 card for initial user_hand
    for i in range(0, 1 + 1):
        random_card = generate_random_card(cards, user_hand)
        append_random_card(random_card, user_hand)
    print(f"your hand: {user_hand}")
    
    #initial dealer hand
    for i in range(0, 1 + 1):
        random_card = generate_random_card(cards, dealer_hand)
        append_random_card(random_card, dealer_hand)
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")

    #Repeat until user decides to stand
    while stand != True:
        hit_or_stand = input("hit or stand? ").lower()
        if hit_or_stand == "hit":
            random_card = generate_random_card(cards, user_hand)
            append_random_card(random_card, user_hand)
            print(f"Your new hand: {user_hand}")
            if sum(user_hand) > 21:
                print("You lose, you have more than 21")
                stand = True
                lose = True
            else:
                pass
        elif hit_or_stand == "stand":
            generate_dealer_hand(dealer_hand)
            stand = True
        else:
            print("---Enter a valid option---")
    print(f"Dealer's final hand: {dealer_hand}")
    
    #Conditions for losing or winning
    if sum(dealer_hand) < sum(user_hand) and not lose:
        print(f"Congrats! you win {user_bet * 2}")
        initial_credits += user_bet * 2
    elif sum(dealer_hand) > 21 and not lose:
        print(f"Dealer has more than 21, you win {user_bet * 2}")
        initial_credits += user_bet * 2
    elif sum(dealer_hand) == sum(user_hand) and not lose:
        print(f"it's a draw! take your {user_bet}")
        initial_credits += user_bet
    else:
        print(f"Dealer wins, you lose {user_bet}")
    
    #Condition for exit the program in case the credits are 0
    if initial_credits == 0:
        game = False
        print("You don't have more credits, sorry, game over!")
        continue
    play_again = input("Play again? y or n: ").lower()
    if play_again == "y":
        pass
    elif play_again == "n":
        game = False
    else:
        print("---Enter a valid option---")