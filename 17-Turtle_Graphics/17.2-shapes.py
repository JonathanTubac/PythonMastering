import turtle as t
import random as rd

t.colormode(255)

def get_random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)

def draw_shape(sides, size):
    angle = 360/sides
    for i in range(sides):
        turtle.fd(size)
        turtle.rt(angle)
        
turtle = t.Turtle()

draw = True
sides = 4

while draw:
    random_color = get_random_color()
    turtle.pencolor(random_color)
    if sides == 10:
        draw = False
        continue
    draw_shape(sides, 100)
    sides += 1
    

screen = t.Screen()
screen.exitonclick()