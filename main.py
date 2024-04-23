from turtle import Turtle, Screen
import random

red = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
purple = Turtle()

screen = Screen()
screen.setup(width=500,height=400)

def start_race(racers, is_race_on,user_bet):
    while is_race_on:
        for turtle in racers:
            turtle.forward(random.randint(0,10))
            if turtle.xcor() > 230:
                if turtle.pencolor() == user_bet:
                    print(f"You win! The {user_bet} turtle won the race!")
                    is_race_on = False
                else:
                    print(f"You lose! The {turtle.pencolor()} turtle won the race!")
                    is_race_on = False



# Turtle set up
red.color("red")
blue.color("blue")
green.color("green")
yellow.color("yellow")
orange.color("orange")
purple.color("purple")
racers = [red, blue, green, yellow, orange, purple]
starting_y = 165
for turtle in racers:
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x=-225,y=starting_y)
    starting_y -= 66

race_on = False
user_turtle = screen.textinput(title="Choose your turtle!", prompt="Which turtle will win the race? Enter a color:")
if user_turtle:
    race_on = True
start_race(racers, race_on,user_turtle)


screen.exitonclick()

