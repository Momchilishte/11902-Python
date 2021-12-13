import turtle

t = turtle.Turtle()
length = 5
turtle.speed(100)
for count in range(100):
    t.forward(length)
    t.right(170)
    length = length + 5
turtle.done()