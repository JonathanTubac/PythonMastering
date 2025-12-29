from turtle import Turtle

FILE_PATH = "19-Snake_Game\data.txt"
ALIGN = "center"
FONT = ("Comic Sans ms", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE_PATH) as file:
            content = file.read()
            self.high_score = int(content)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(0, 270)
        self.update_score()
    
    def add_score(self):
        self.score += 1
        self.update_score()
            
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGN, FONT)
        
    '''def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)
    '''
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()