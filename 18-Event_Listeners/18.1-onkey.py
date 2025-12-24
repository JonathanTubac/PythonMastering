from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_fordward():
    t.fd(10)

screen.listen()
screen.onkey(key="space", fun=move_fordward)

screen.exitonclick()