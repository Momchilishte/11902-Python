import turtle

t = turtle.Pen()
t.color("blue" , "purple" )
t.begin_fill()
t.speed(100)
while True:
    t.forward(301)
    t.left(1234)
    if abs(t.pos()) < 1:
        break
t.end_fill()
turtle.done()
