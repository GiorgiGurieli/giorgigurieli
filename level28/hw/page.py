from turtle import *
speed(30)

def triangle():
    color("blue")
    begin_fill()
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    end_fill()
    left(30)
    penup()
    forward(100)
    pendown()
    left(90)

for i in range(120):
    triangle()
exitonclick()

