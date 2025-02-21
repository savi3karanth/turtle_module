from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen", "Red", "blue"]

timmy = Turtle()
direction = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
