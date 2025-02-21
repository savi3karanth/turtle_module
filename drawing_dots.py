import random
import turtle
from turtle import Turtle, Screen

colour_list = [(253, 251, 247), (253, 247, 250), (236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]

tim = Turtle()  #gave turtle name tim
tim.speed("fastest")    # we say the turtle speed to be the fastest
tim.penup()     # Here turtle should not draw a line for every dot
tim.hideturtle()    # This is to hide the arrow/turtle direction
turtle.colormode(255)   # We use this for all the rgb colours
num_of_counts = 100 # no of dots to display on screen

tim.setheading(225)     # to start the dot
tim.forward(300)        # to move fwd
tim.setheading(0)

for dot_count in range(1, num_of_counts + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()