OUTPUT_PATH = "21-Mail_Merge/Output/ReadyToSend"
TEMPLATE_PATH = "21-Mail_Merge/Input/Letters/starting_letter.txt"
NAMES_PATH = "21-Mail_Merge/Input/Names/invited_names.txt"

#This function read any file
def read_file(path):
    with open(path, "r") as file:
        content = file.read()
        return content
    
#This function separates each line of the text file into a list
def read_file_lines(path):
    with open(path, "r") as file:
        content = file.readlines()
        return content

#This function create the letters with the names and creates it into the output path
def create_letters(names, path):
    for name in names:
        with open(f"{path}/letter_for_{name}.docx", "w") as output:
            letter = template.replace("[name]", name)
            output.write(letter)

#this function eliminates the \n created in the list of names        
def format_names(names):
    formated_names = []
    for name in names:
        formated_name = name.strip()
        formated_names.append(formated_name)
    return formated_names
        
template = read_file(TEMPLATE_PATH)
names = read_file_lines(NAMES_PATH)
formated_names = format_names(names)
create_letters(formated_names, OUTPUT_PATH)
    

