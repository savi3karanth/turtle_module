import random
from turtle import Turtle, Screen


screen = Screen()
new_turtle = Turtle()
user_bet = screen.textinput(title="Bet on Turtle", prompt="Which color turtle will win. Enter the colour")
colour = ["red", "blue", "green", "orange", "black", "pink", "purple", "cyan"]
screen.setup(width=500, height=400)
all_turtle = []
y_position = [-150, -110, -70, -30, 10, 50, 90, 130]
is_race_on = True

for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colour[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_colour = turtle.pencolor()
            if winner_colour == user_bet:
                print(f"You win. The winner turtle colour is {winner_colour}")
            else:
                print(f"You lose. The winner turtle colour is {winner_colour}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
