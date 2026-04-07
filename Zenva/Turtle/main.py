from turtle import * 
from random import *
from turtle import *

forward(randrange(20, 200))
right(randrange(0, 360))
forward(randrange(20, 200))

done()
# Notes for turtle: https://academy.zenva.com/lesson/full-source-code-intro-to-python-turtle/?zva_less_compl=3600314
# squares
# forward(50)
# right(90)

# forward(50)
# right(90)

# forward(50)
# right(90)

# forward(50)

# circle(50) # radius
# forward(150)
# circle(80)

# add color
# color("red") # change stroke
# forward(150)
# color("#ffc929") #use color picker with HEX color
# right(90)
# left(90)
# # fill shape
# begin_fill()
# circle(50)
# end_fill()

# triangle

# begin_fill()

# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)

# end_fill()

# change background
# getscreen().bgcolor("#9ef9ff")
# color("red")

# forward(100)

# lift the pen - creating independent images
# circle(50)
# penup()
# forward(150)
# pendown()
# circle(50)

# solar system
# Screen().setup(800, 500)

# # set speed to 0 so the animation is instant
# speed(0)

# # set the background color to BLACK
# # this line is altered for the live coding example
# Screen().bgcolor("black")

# # create the ORANGE planet
# color("orange")
# begin_fill()
# circle(60)
# end_fill()

# # move forwards
# penup()
# forward(100)
# pendown()

# # create the GREY planet
# color("grey")
# begin_fill()
# circle(20)
# end_fill()

# # move forwards
# penup()
# forward(80)
# pendown()

# # create the RED planet
# color("red")
# begin_fill()
# circle(40)
# end_fill()

# # move forwards
# penup()
# forward(90)
# pendown()

# # create the GREEN planet
# color("green")
# begin_fill()
# circle(30)
# end_fill()

# done()


# def say_hello(name):
#     print("Hello " + name)


# say_hello("Bob")
# say_hello("Steve")
# say_hello("Mary")


# # using Turtle
# def move_and_turn(distance, angle):
#     forward(distance)
#     right(angle)


# move_and_turn(100, 80)
# move_and_turn(150, 30)

# done()

# diameter = 40
# pop_diameter = 100

# def draw_balloon():
#     global diameter
#     color("red")
#     dot(diameter)

# def inflate_balloon():
#     global diameter
#     diameter = diameter + 10
#     draw_balloon()
#     if diameter >= pop_diameter:
#         clear()
#         diameter=40
#         write("POP!")

# # call inflate_balloon when we press the Up arrow key
# # Screen() is required before onkey and listen due to the way this snippet compiles the code.
# # Screen() accesses the screen property, then inside of that we access the onkey and listen functions.
# Screen().onkey(inflate_balloon, "Up")
# Screen().listen()
# done()
