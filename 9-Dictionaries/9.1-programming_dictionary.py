programming_dictionary = {
    "Bug": "An error in a program that prevents the program running as expected",
    "Functions": "A piece od code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

#Creating data into the dictionary
programming_dictionary["Variable"] = "A place to store data localy"
print(programming_dictionary)

#Wipe an existing dictionary
#programming_dictionary = {}

#Edit an item
programming_dictionary["Bug"] = "An insect"

print(programming_dictionary)

#looping a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
