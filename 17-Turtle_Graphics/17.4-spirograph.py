import turtle as t
import random as rd

#Adjust the color to a 255 rgb mode
t.colormode(255)

#Global variables
turtle = t.Turtle()
screen = t.Screen()
angle = 0
r = 100
angle_separation = 5

#This function will return a random rbg tuple
def get_random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

#Draw a spirograph
def draw_spirograph(angle_separation):
    angle = 0
    for i in range(int(360/angle_separation) + 1):
        turtle.pencolor(get_random_color())
        turtle.setheading(angle)
        turtle.circle(r)
        angle += angle_separation
        
#Adjusting the turtle draw speed
turtle.speed(1000)

draw_spirograph(2)
    
screen.exitonclick()