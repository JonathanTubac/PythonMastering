def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

new_op = True
menu = True
print("Welcome to the calculator")

while menu == True:
    
    if new_op == True:
        first_number = int(input("Enter the first number: "))
    
    operation = input("What do you want to do(+ - * /): ")
    second_number = int(input("Enter your second number: "))
    if operation == "+":
        result = add(first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is: " + str(result)) 
    elif operation == "-":
        result = substract(first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    elif operation == "*":
        result = mult(first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    elif operation == "/":
        result = div(first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is: {result}")
    op_menu = True  
    while op_menu == True:
        continue_op = input(f"Do you want to continue operating with {result} or make a new operation? y or n(type exit to finish): ").lower()
        
        if continue_op == "y":
            first_number = result
            new_op = False
            op_menu = False
        elif continue_op == "n":
            new_op = True
            op_menu = False
        elif continue_op == "exit":
            menu = False
            op_menu = False
        else:
            print("Please enter a valid option.")
    