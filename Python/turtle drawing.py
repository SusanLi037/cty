import turtle
import random
t = turtle.Pen()
t.screen.bgcolor('black')
for i in range(0, 200, 3):
    t.forward(i)
    t.left(71)
    color = random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
    if color == 'red':
        t.color('red')
    elif color == 'orange':
        t.color('orange')
    elif color == 'yellow':
        t.color('yellow')
    elif color == 'green':
        t.color('green')
    elif color == 'blue':
        t.color('blue')
    elif color == 'purple':
        t.color('purple')

