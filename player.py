from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape('turtle')

    def goto_start(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)