import turtle as t
import random as rd

t.colormode(255)

directions = [0, 90, 180, 270]

def get_random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def choose_random_direction(directions):
    random_direction = rd.choice(directions)
    return random_direction
    
turtle = t.Turtle()
turtle.speed(100)
turtle.pensize(8)

for i in range(500):
    turtle.setheading(choose_random_direction(directions))
    turtle.pencolor(get_random_color())
    turtle.forward(30)
    
screen = t.Screen()
screen.exitonclick()