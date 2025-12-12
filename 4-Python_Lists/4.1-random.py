import random as rd

#print(rd.randint(1, 10))

random_number = rd.random() * 10
print(round(random_number))


number = rd.randint(0, 1)
if number == 0:
    print("Heads")
else:
    print("Tails")

