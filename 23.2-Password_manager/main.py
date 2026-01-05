from tkinter import *
import random as rd
from tkinter import messagebox
import json
#Constants
PASSWORD_FILE_PATH = "./23.2-Password_manager/data.json"

#Global variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "w", "y", "z"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '|', '*']

#Dictionary
characters = {
    "letters": letters,
    "numbers": numbers,
    "symbols": symbols
}

#This function generates and return a totally random character
def choose_random_character(characters):
    random_type = rd.randint(1, 3)
    random_upper = rd.randint(0, 1)
    if random_type == 1:
        random_character = rd.choice(characters["letters"])
        if random_upper == 1:
            return random_character.upper()
        else:
            return random_character
    elif random_type == 2:
        random_character = rd.choice(characters["numbers"])
        return random_character
    elif random_type == 3:
        random_character = rd.choice(characters["symbols"])
        return random_character

#This function updates the variable entry for the input fields
def update_password_entry(new_entry):
    password_string.set(new_entry)

#This function is triggered by the generate button
def generate_password():
    password = []
    for i in range(0, 16):
        character = choose_random_character(characters)
        password.append(character)
    update_password_entry("".join(map(str, password)))

#This function checks if one of the entries is null
def check_entries_null():
    if len(user_input.get()) == 0 or len(website_input.get()) == 0 or len(password_input.get()) == 0:
        return True
    else:
        return False
    
#This function is triggered by the add button
def add_info_to_file():
    is_ok = messagebox.askokcancel(title="Title", message=f"These are the details, please check it: \nEmail:{user_input.get()}\nPassword: {password_input.get()} \nAre you sure?")
    is_null_entries = check_entries_null()
    new_data = {
        website_input.get(): {
            "email": user_input.get(),
            "password": password_input.get()
        }
    }
    
    if is_ok and not is_null_entries:
        try:
            with open(PASSWORD_FILE_PATH, "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(PASSWORD_FILE_PATH, "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(PASSWORD_FILE_PATH, "w") as file:
                json.dump(data, file, indent=4)
                
    elif is_null_entries:
        messagebox.showwarning(title="Fields missing", message="Please don't enter null data")

#Window and image
window = Tk()
window.config(padx=50, pady=50)
window.title("Password manager")
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="23.2-Password_manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#Inputs
password_string = StringVar()

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)

user_input = Entry(width=40)
user_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=28, textvariable=password_string)
password_input.grid(column=1, row=3)

#Buttons
generate_btn = Button(text="Generate password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=add_info_to_file)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
