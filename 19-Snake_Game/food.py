from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
    
    def create_food(self):
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("brown")
        self.speed("fastest")
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)
    
    def move_random_xy(self):
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)
    
        
        