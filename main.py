import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
player = Player()
score_board= Scoreboard()
car_manager= CarManager()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down,'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right,'Right')


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    #Detect collision with cars
    if(car_manager.move_cars(player)==False):
        screen.update()
        game_is_on=False
    #Detect successful crossing
    if(player.ycor()>250):
        score_board.increase_score()
        player.goto_start()
        car_manager.increase_speed()

score_board.game_over()
screen.exitonclick()