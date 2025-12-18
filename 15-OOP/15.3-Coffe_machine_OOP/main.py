from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
machine = True

def spacer():
    print("-----------------------")
    
while machine:
    print(menu.get_items())
    user_coffe = input("What do you want? ").lower()
    spacer()
    if user_coffe == "report":
        coffe_machine.report()
        input("Press enter to continue.")
        continue
    coffe_type = menu.find_drink(user_coffe)
    money.make_payment(coffe_type.cost)
    spacer()
    validate_resource = coffe_machine.is_resource_sufficient(menu.find_drink(user_coffe))
    
    if validate_resource:
        coffe_machine.make_coffee(menu.find_drink(user_coffe))
        spacer()
    else:
        pass
    
    
