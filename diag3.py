import turtle


# Draw a Sierpinski Triangle
def sierpinski(size, depth):
    if depth == 0:
        for i in range(3):
            turtle.forward(size)
            turtle.left(120)
            
    else:
        sierpinski(size / 2, depth - 1)
        turtle.forward(size / 2)
        sierpinski(size / 2, depth - 1)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        sierpinski(size / 2, depth - 1)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)

sierpinski(200, 4)
