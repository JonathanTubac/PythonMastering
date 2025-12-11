print("Welcome to the calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("what percentaje tip do you want to give? "))
number_people = int(input("how many people to split the bill? "))



percentaje_tip = bill * (tip / 100)
total_bill = bill + percentaje_tip
each_one_bill = total_bill / number_people

print(f"Each person should pay: ${round(each_one_bill, 2)}")