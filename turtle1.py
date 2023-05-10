import turtle as tu 
import colorsys

tu.Screen().bgcolor("black")
t = tu.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(n):
    t.forward(n)
    t.circle(-60,120)
    t.forward(n)
    t.circle(60,240)

t.setpos(-90,0)
for i in range (150):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)
    design(i*0.5)
    design(i)
    h += 0.6766

t.ht()

tu.done()