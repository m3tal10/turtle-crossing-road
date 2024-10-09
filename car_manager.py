from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self) -> None:
        self.cars=[]

    def generate_car(self):
        random_chance= random.randint(1,6)
        if len(self.cars)<=20:
            if random_chance==1:
                car= Turtle()
                car.pu()
                car.color(random.choice(COLORS))
                car.shape('square')
                car.shapesize(1,2)
                car.goto(300,random.randint(-250,250))
                self.cars.append(car)

    def move_cars(self, player):
        for index,car in enumerate(self.cars):
            car.setheading(180)
            car.forward(STARTING_MOVE_DISTANCE)
            if(car.xcor()<-300):
                if(index == len(self.cars)-1):
                    car.hideturtle()
                    self.cars.pop()
                else:
                    self.cars[index]= self.cars.pop()
                    car.hideturtle()
            if(player.distance(car)<25):
                return False
    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+= MOVE_INCREMENT