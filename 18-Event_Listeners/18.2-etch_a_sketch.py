from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_fordward():
    t.fd(10)

def move_backward():
    t.backward(10)
    
def rotate_clockwise():
    t.rt(10)

def rotate_anticlockwise():
    t.lt(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
screen.listen()

screen.onkeypress(key="w", fun=move_fordward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeypress(key="a", fun=rotate_anticlockwise)
screen.onkey(key="space", fun=clear_screen)

screen.exitonclick()