from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for _ in range(5):
            self.create_snake_body()   

    
    def create_snake_body(self):
        snake_body = Turtle()
        snake_body.penup()
        snake_body.speed("fastest")
        snake_body.shape("square")
        snake_body.color("green")
        self.snake.append(snake_body)
    
    def reset(self):
        for snake_body in self.snake:
            snake_body.goto(10000, 10000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
         
    def move(self):
        for snake_body in range(len(self.snake) - 1, 0, -1):
            next_body_x = self.snake[snake_body - 1].xcor()
            next_body_y = self.snake[snake_body - 1].ycor()
            self.snake[snake_body].goto(next_body_x, next_body_y)
        self.snake[0].fd(MOVE_DISTANCE)
    
    def rotate_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def rotate_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def rotate_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def rotate_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def get_head_x(self):
        return self.head.xcor()
    
    def get_head_y(self):
        return self.head.ycor()