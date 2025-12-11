height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("You need to pay $7")
        bill += 7
    elif age <= 18:
        print("You need to pay $12")
        bill += 12
    elif age >= 45 and age <= 55:
        print("You got a free ride!")
    else:
        print("You need to pay $15")
        bill += 15
    photo = input("Do you want photo? y or n: ")
    
    if photo == "y":
        print("Photos added, $5 more in the bill")
        bill += 5
    else:
        print("no photos")
    print("your bill is $" + str(bill))
else:
    print("Sorry, you have to grow taller")