import random
from turtle import Turtle

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen", "Red", "blue", "Purple", "Pink", "Violet"]

timmy = Turtle()
timmy.shape("turtle")


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side in range(3, 13):
    timmy.color(random.choice(colours))
    draw_shape(shape_side)
