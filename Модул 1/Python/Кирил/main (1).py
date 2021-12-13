import turtle
t = turtle.Pen()
t.color('red', 'pink')
t.begin_fill()
t.speed(600)
while True:
    t.forward(200)
    t.left(137)
    if abs(t.pos()) < 1:
        break
t.end_fill()
turtle.done()
