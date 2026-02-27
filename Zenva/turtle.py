from turtle import * 
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
Screen().setup(800, 500)

# set speed to 0 so the animation is instant
speed(0)

# set the background color to BLACK
# this line is altered for the live coding example
Screen().bgcolor("black")

# create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

# move forwards
penup()
forward(100)
pendown()

# create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

# move forwards
penup()
forward(80)
pendown()

# create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# move forwards
penup()
forward(90)
pendown()

# create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

done()
