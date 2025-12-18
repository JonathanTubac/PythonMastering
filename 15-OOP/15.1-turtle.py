import turtle as t

#we use the class Turtle
timmy = t.Turtle()

#we access to its methods
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
my_screen = t.Screen()

#We can see this attribute
print(my_screen.canvheight)
my_screen.exitonclick()