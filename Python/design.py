import turtle
t = turtle.Pen()
t.pensize(4)
for i in range(0,10):
    t.forward(100)
    t.left(200)
    t.color("turquoise")
    t.circle(10)
    t.up()
    for x in range(0,3):
        t.pensize(2)
        t.color("lime")
        t.forward(20)
        t.down()
        t.forward(10)
        t.right(120)
    t.color("violet")
    for j in range(0,6):
        t.pensize(4)
        t.forward(25)
    t.color("orange")
    
