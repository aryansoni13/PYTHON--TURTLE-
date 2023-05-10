import turtle
import time

# create a turtle object
t = turtle.Turtle()
t.screen.bgcolor('black')


# set the turtle speed and color
t.speed(0)
t.color('red')

# define a function to draw the heart
def draw_heart(size):
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(size)
    t.circle(size/2, 180)
    t.right(90)
    t.circle(size/2, 180)
    t.forward(size)
    t.end_fill()
    t.right(135)

# define a function to morph the heart
def morph_heart(size):
    t.clear()
    for i in range(20):
        t.penup()
        t.goto(0, -size)
        t.pendown()
        t.begin_fill()
        t.left(45)
        t.forward(size)
        t.circle(size/2 + i*5, 180)
        t.right(90)
        t.circle(size/2 + i*5, 180)
        t.forward(size)
        t.end_fill()
        t.right(135)
        time.sleep(0.1)
        t.clear()

# draw the heart and morph it
size = 100
draw_heart(size)
morph_heart(size)
