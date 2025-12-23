import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("aquamarine")

square = 100

#draw a square
for i in range(4):
    timmy.fd(square)
    timmy.rt(90)

timmy.goto(19, 20)
for i in range(10):
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()

screen = t.Screen()
screen.exitonclick()