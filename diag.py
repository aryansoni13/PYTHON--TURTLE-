import turtle


t = turtle.Turtle()
t.speed(0)  
t.screen.bgcolor('black')


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


for i in range(600):
    t.color(colors[i % 6])  
    t.forward(i * 2)  
    t.left(59)  


t.hideturtle()


turtle.done()
