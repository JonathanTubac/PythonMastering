import colorgram as cg
import turtle as t
import random as rd

t.colormode(255)

raw = cg.extract("17-Turtle_Graphics/17.5-hirst-dots/dots.PNG", 30)
colors = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in raw]

turtle = t.Turtle()
turtle.hideturtle()
turtle.speed("fastest")

def get_random_color(colors):
    random_color = rd.choice(colors)
    return random_color

def draw_circle_line(n_circles, radio_circles, colors):
    for i in range(0, n_circles + 1):
        turtle.pencolor("white")
        turtle.fillcolor(get_random_color(colors))
        turtle.begin_fill()
        turtle.circle(radio_circles)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(radio_circles + 50)
        turtle.pendown()

x = -400
y = -300
lines = 6    
for i in range(lines + 1):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_circle_line(10, 20, colors)
    y += 70
    
t.Screen().exitonclick()
    
