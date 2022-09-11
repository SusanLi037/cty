#Programmer name: Susan Li
#Program creation date: August 23, 2022

#create different turtle graphics

import turtle
import random
t = turtle.Pen()
#function for an even number of sides 
def even (number_of_sides):
    #set a random side length
    size = random.randint(50, 200)
    #draw the graphic
    for j in range(0, 20):
        t.left(20)
        for i in range(0, number_of_sides):
            t.forward(size)
            t.left(360/number_of_sides)
            t.color(random.random(), random.random(), random.random())
#function for an odd number of sides
def odd (number_of_sides):
    #draw the graphic
    for x in range(0, random.randint(25, 100), random.randint(2, 5)):
        t.forward(x)
        t.left(360/number_of_sides)
        t.color(random.random(), random.random(), random.random())
#draw four graphics
for i in range(0, 4):
    number_of_sides = random.randint(3, 8)
    #draw rotating shape graphic if the number of sides is even
    if number_of_sides % 2 == 0:
        even(number_of_sides)
    #draw spiral lines graphic if the number of sides is odd
    if number_of_sides % 2 == 1:
        odd(number_of_sides)
    #reset the screen and turtle
    t.reset()
