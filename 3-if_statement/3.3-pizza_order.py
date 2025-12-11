print("Welcome to mordex pizza delivery!")
size = input("Enter the size of your pizza(S, M or L): ")
pep = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want it with extra cheese? Y or N: ")
bill = 0
if size.lower() == "s":
    print("Small size cost $15")
    bill += 15
elif size.lower() == "m":
    print("Medium size cost $20")
    bill += 20
elif size.lower() == "l":
    print("Large size cost $25")
    bill += 25

if pep.lower() == "y":
    if size.lower() == "s":
        print("for small pizza, pepperoni cost $2")
        bill += 2
    elif size.lower() == "m":
        print("for medium pizza, pepperoni cost $3")
        bill += 3
    else:
        print("for large pizza, pepperoni cost $4")
        bill += 4        
else:
        print("No pepperoni")
        
if extra_cheese.lower() == "y":
    print("Extra cheese for any pizza cost $1")
    bill += 1
else:
    print("No extra cheese")

print("Your final bill is $" + str(bill))