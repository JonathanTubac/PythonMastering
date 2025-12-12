import random as rd
print("Welcome to the restaurant")

friends = ["Jonathan", "Pablo", "Angel", "Mike"]
#we make the length - 1 because the max index is 3 not 4
random_number = rd.randint(0, len(friends) - 1)

#other way to make it
# print(rd.choice(friends))
print(friends[random_number] + " will pay the bill")