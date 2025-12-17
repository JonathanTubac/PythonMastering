import menu as m
import coins as cn
import resources as rsc
import os
import platform

#Global variables
machine = True

#Function for cleaning console in Linux or Windows
def clean_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#Function for decoration for console printing  
def space():
    print("------------------------------")

#Function to prepare the coffe using the machine resources
def prepare_coffe(user_coffe, menu, machine_resource, user_money):
    if machine_resource["water"] >= menu[user_coffe]["ingredients"]["water"] and machine_resource["milk"] >= menu[user_coffe]["ingredients"]["milk"] and machine_resource["coffe"] >= menu[user_coffe]["ingredients"]["coffe"] and user_money >= menu[user_coffe]["cost"]:
        machine_resource["water"] -= menu[user_coffe]["ingredients"]["water"]
        machine_resource["milk"] -= menu[user_coffe]["ingredients"]["milk"]
        machine_resource["coffe"] -= menu[user_coffe]["ingredients"]["coffe"]
        machine_resource["money"] += menu[user_coffe]["cost"]
        return "success"
    elif user_money < menu[user_coffe]["cost"]:
        return "insufficient_money"
    elif machine_resource["water"] < menu[user_coffe]["ingredients"]["water"]:
        return "no_water"
    elif machine_resource["milk"] < menu[user_coffe]["ingredients"]["milk"]:
        return "no_milk"
    elif machine_resource["coffe"] < menu[user_coffe]["ingredients"]["coffe"]:
        return "no_coffe"


#Function to restock the machine
def fill_machine(w, m, c, machine_resources):
    machine_resources["water"] += w
    machine_resources["milk"] += m
    machine_resources["coffe"] += c

#Function to calculate money of the user   
def calculate_user_money(q, n, d, p, coins):
    quarter_value = coins["quarter"] * q
    nickles_value = coins["nickel"] * n
    dime_value = coins["dime"] * d
    penny_value = coins["penny"] * p
    return round(quarter_value + nickles_value + dime_value + penny_value, 2)

#Function to calculate change of the user     
def calculate_change(total, menu, user_coffe):
    if total < menu[user_coffe]["cost"]:
        print("Insufficient money.")
    else:
        return round(total - menu[user_coffe]["cost"], 2)

#Function to validate integers entries
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("You can't enter negative values. Try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

while machine:
    clean_console()
    user_menu = True
    
    while user_menu:
        clean_console()
        print("Welcome to the coffe machine!")

        space()
        print("MENU")
        space()
        for coffe in m.MENU:
            print(coffe + ": $" + str(m.MENU[coffe]["cost"]))
        space()
        print("type 'report' to see the available resources of the coffe machine.")
        print("type 'fill' to restock the machine.")
        print("type 'off' to turn off the machine for maintenance.")
        user_decision = input("What type of coffe do you want? ").lower()
        
        #validate the user input
        if user_decision == "report":
            clean_console()
            print("These are the machine resources.")
            space()
            for ingredient in rsc.resources:
                dolar = ""
                if ingredient == "water" or ingredient == "milk":
                    unit = "mL"
                elif ingredient == "coffe":
                    unit = "g"
                else:
                    dolar = "$"
                    unit = ""
                print(ingredient + ": " + dolar + str(rsc.resources[ingredient]) + unit)
            space()
            input("Press enter to exit.")
            continue
        elif user_decision == "off":
            print("turning off......")
            machine = False
            user_menu = False
            continue
        elif user_decision == "fill":
            space()
            water = int(input("Enter the amount(mL) of water you want to fill: "))
            milk = int(input("Enter the amount(mL) of milk you want to fill: "))
            coffe = int(input("Enter the amount(g) of coffe you want fo fill: "))
            fill_machine(water, milk, coffe, rsc.resources)
            space()
            
            print("Machine filled successfully!")
            input("Press enter to continue.")
        elif user_decision == "espresso" or user_decision == "latte" or user_decision == "cappuccino":
            user_menu = False
        else:
            print("Enter a valid option.")
            continue
        
    if not machine:
        print("Machine turned off. Goodbye.")
        continue

    space()
    print("Please insert coins.")
    n_qu = get_non_negative_int("Enter quarters($0.25): ")
    n_dim = get_non_negative_int("Enter dimes($0.10): ")
    n_nick = get_non_negative_int("Enter nickles($0.05): ")
    n_pen = get_non_negative_int("Enter pennies($0.01): ")
    space()
    
    user_money = calculate_user_money(n_qu, n_nick, n_dim, n_pen, cn.coins)
    change = calculate_change(user_money, m.MENU, user_decision)
    prepare_coffe_status = prepare_coffe(user_decision, m.MENU, rsc.resources, user_money)
    
    if  prepare_coffe_status == "insufficient_money":
        print(f"Sorry, insufficient money to pay {user_decision}. Money refunded, please enter more coins.")
    elif prepare_coffe_status == "no_water":
        print(f"Sorry, insufficient water to prepare {user_decision}. Money refunded. Please refill the machine.")
    elif prepare_coffe_status == "no_milk":
        print(f"Sorry, insufficient milk to prepare {user_decision}. Money refunded. Please refill the machine.")
    elif prepare_coffe_status == "no_coffe":
        print(f"Sorry, insufficient coffe to prepare {user_decision}. Money refunded. Please refill the machine.")
    else:
        space()
        print(f"The coffe machine spent these ingredients in your {user_decision}.")
        for ingredient in m.MENU[user_decision]["ingredients"]:
            if ingredient == "water" or ingredient == "milk":
                unit = "mL"
            else:
                unit = "g"
                
            print(ingredient + ": " + str(m.MENU[user_decision]["ingredients"][ingredient])  + unit)
        space()
        print(f"Your {user_decision} has been prepared successfully!")
        print(f"You paid ${user_money} and your change is ${change}.")
  
    input("Press enter to continue.")
