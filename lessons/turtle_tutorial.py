"""Fun with turtle software!"""

__author__ = "730229417"

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# done()
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1
# done()
leo.color(63, 171, 8)
leo.begin_fill()
leo.penup()
leo.goto(-120, -100)
leo.pendown()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.color("orange")
bob.penup()
bob.goto(-120, -100) 
bob.pendown()
bob.speed(150)
side_length: int = 300

i: int = 0
while (i < 250):
    side_length = side_length * 0.96
    bob.forward(side_length)
    bob.left(121)
    i = i + 1
done()