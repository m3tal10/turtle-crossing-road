from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.pu()
        self.hideturtle()
        self.goto(-250,250)
        self.increase_score()
    
    def increase_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", move=False, align= 'left', font=FONT)
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align= 'center', font=FONT)

