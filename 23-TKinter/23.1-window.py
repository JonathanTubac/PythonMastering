from tkinter import *

def button_clicked():
    my_label.config(text=input.get())
    
window = Tk()
window.title("My first GUI")
window.minsize(500, 300)

#Label
my_label = Label(text="Hello, i'm a label", font=("Comic Sans ms", 16, "normal"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New Text")

#button

button = Button(text="click me!", command=button_clicked)
button.pack()

#Entry

input = Entry(width=15)
input.pack()
print(input.get())
window.mainloop()