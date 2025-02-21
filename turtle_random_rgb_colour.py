import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

turtle = Turtle()

direction = [0, 90, 180, 270]
turtle.speed("fastest")
turtle.pensize(12)

screen = Screen()




def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r,g,b)
    return random_colour


for _ in range(200):
    turtle.color(random_colours())
    turtle.forward(30)
    turtle.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
