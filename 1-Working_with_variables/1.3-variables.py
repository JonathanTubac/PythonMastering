name = input("Enter a name: ")
length = len(name)
#you can't combine int with strings, so you need to parse the length to string using str()
print("The name: " + name + " has " + str(length) + " characters")