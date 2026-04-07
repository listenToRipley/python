from turtle import *
from random import *

bgcolor("black")
hideturtle()# make the triangle "turtle" invisible

#find size of screen
width = window_width()
height = window_height()

speed(0)# quick

def  draw_star(xpos, ypos):
    size = randrange(4, 10)  # change size
    penup()
    ## start position is (0,0) center of the page
    ## go to is "teleport"
    goto(xpos, ypos)
    pendown()
    dot(size, "white")


draw_star(0,0)

# add randomness
for i in range(100):
    print("draw star")
    rand_y = randrange(-height //2, height//2)
    rand_x = randrange(-width //2, width//2)
    
    draw_star(rand_x, rand_y)

done()
