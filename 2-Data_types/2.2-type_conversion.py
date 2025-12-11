len("Hello")

print(type("Hello"))
print(type(123))
print(type(True))
print(type(32.5))

#We parse the numbers in the string to int and this makes the addition.
print(int("123") + int("456"))

#you can parse the data using these funcitons
int()
bool()
float()
str()

print("Your name has " + str(len(input("Enter your name: "))) + " characters")