from turtle import *

shape("turtle")
speed(0)


def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)


def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)


def polygon(num_of_sides, sidelength=100):
    for i in range(num_of_sides):
        forward(sidelength)
        right(360 / num_of_sides)


def bigger_squares():
    length = 5
    for i in range(60):
        square(length)
        right(5)
        length += 5

def star(sidelength=100):
    for i in range(5):
        forward(sidelength)
        right(144)
        
def star_spiral():
    length = 5
    for i in range(60):
        star(length)
        right(5)
        length += 5

def embedded_squares():
    length = 1
    for i in range(60):
        fd(length)
        rt(90)
        length += 1

def spiral():
    length = 1
    for i in range(60):
        rt(30)
        fd(length)
        length += 1

# for i in range(60):
#    square()
#    right(5)

# triangle()

# polygon(6)

#bigger_squares()

#star()

#star_spiral()

spiral()

hideturtle()
mainloop()
