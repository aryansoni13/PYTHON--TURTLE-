import turtle as tu 
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(ang,n):
    t.circle(70+n,90)
    t.left(ang)
    t.circle(70+n,90)

for i in range(65):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)

    design(120,i)
    design(60,i)
    design(90,i)
    design(60,i)
    design(120,i)

    h += 0.6766



tu.done()