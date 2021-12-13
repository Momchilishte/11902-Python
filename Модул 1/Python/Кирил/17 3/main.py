import turtle
t = turtle.Pen()
t.pensize(6)
length = 5
t.speed(100000000000)
for i in range(1000):
    t.forward(length)
    t.right(123)
    length = 5 + length

turtle.done()
