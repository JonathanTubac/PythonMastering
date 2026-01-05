from tkinter import *
import math

#Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#Inicialization of global variables
reps = 0
timer = None
checkmarks = ""

#This function is triggered by the start button
def start_timer():
    global reps
    
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break)
        tittle_label.config(text="Long break!", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        tittle_label.config(text="Short break!", fg=PINK)
    else:
        tittle_label.config(text="Work", fg=GREEN)
        countdown(work)

#This button displays and decreases the timer  
def countdown(count):
    global checkmarks
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    if minutes < 10:
        minutes = f"0{minutes}"
    if int(seconds) < 10 and int(seconds) != 0:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks += "✓"
        check_marks.config(text=checkmarks, fg=GREEN)

#This function is triggered by the reset button
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    tittle_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

#We create the UI
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro App")

tittle_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
tittle_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#We do this because the create_image method doesn't support a path file
tomato_image = PhotoImage(file="23.1-Pomodoro_App/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()