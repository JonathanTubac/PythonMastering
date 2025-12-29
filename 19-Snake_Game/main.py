from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game = True
screen = Screen()
screen.setup(width=600, height=600)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.title("Snake Game")
screen.listen()
screen.onkey(key="Up", fun=snake.rotate_up)
screen.onkey(key="Down", fun=snake.rotate_down)
screen.onkey(key="Right", fun=snake.rotate_right)
screen.onkey(key="Left", fun=snake.rotate_left)

while game:  
    screen.update()
    time.sleep(0.01)
    snake.move()    
    
    if snake.head.distance(food) < 15:
        food.move_random_xy()
        snake.create_snake_body()
        scoreboard.add_score()
    
    for snake_body in snake.snake[1:]:
        if snake.head.distance(snake_body) < 10:
            scoreboard.reset()
            food.move_random_xy()
            snake.reset()
            
    #screen edges collision validation
    if snake.get_head_x() > 280 or snake.get_head_x() < -280 or snake.get_head_y() > 280 or snake.get_head_y() < -280:
        scoreboard.reset()
        snake.reset()
        food.move_random_xy()
screen.exitonclick()