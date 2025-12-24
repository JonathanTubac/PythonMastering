from turtle import Turtle, Screen
import random as rd

#Global variables and lists
is_race_on = False
turtles = []
colors = ["red", "green", "orange", "purple", "yellow", "aquamarine"]
screen = Screen()
starting_y = -125

#Function for setting the starting position for a turtle
def setup_turtle_position(x, y, turtle):
    turtle.penup()
    turtle.goto(x, y)

#Setup the size and the background color of the screen
screen.setup(width=500, height=400)
screen.bgcolor("gray")

#Request a input to user
user_decision = screen.textinput(title="Make your bet", prompt="Choose a turtle color for yout bet: ")

#Creating 6 turtles for the race
for turtle_index in range(6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[turtle_index])
    setup_turtle_position(-250, starting_y, turtle)
    starting_y += 50
    turtles.append(turtle)
    
#After creating the turtles, start the race
if user_decision:
    is_race_on = True

while is_race_on:
    
    #for each turtle in the list, move randomly and evalueate the x coordinate for winning
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_decision:
                print(f"Congrats, your turtle won!")
            else:
                print(f"Sorry, the winner turtle is: {turtle.pencolor()}")
            is_race_on = False
            continue
        
        random_move = rd.randint(0, 10)
        turtle.fd(random_move)
        
screen.exitonclick()