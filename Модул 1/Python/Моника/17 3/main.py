import turtle

t = turtle.Pen()
t.pensize(5)
t.pencolor("cyan")
length = 5
t.speed(50)
for i in range(10000000):
    #t.pencolor(length, length, length)
    t.forward(length)
    t.right(246)
    length = length + 5
turtle.Done()
