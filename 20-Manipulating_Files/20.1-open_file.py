with open("20-Manipulationg_Files\my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("20-Manipulationg_Files\my_file.txt", mode="a") as file:
    file.write("\nNew Text.")


