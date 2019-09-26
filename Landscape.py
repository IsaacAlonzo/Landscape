import turtle

john = turtle.Turtle()
scn = turtle.Screen()
bob = turtle.Turtle()
phil = turtle.Turtle()
sven = turtle.Turtle()

bob.shape("classic")
phil.shape("classic")
john.shape("classic")
sven.shape("classic")

bob.penup()
phil.penup()
sven.penup()
turtle.bgcolor("light sky blue")

def grass():
    bob.begin_fill()
    bob.color("green")
    bob.forward(400)
    bob.right(90)
    bob.forward(400)
    bob.right(90)
    bob.forward(800)
    bob.right(90)
    bob.forward(400)
    bob.right(90)
    bob.forward(400)
    bob.end_fill()

grass()

def house():
    john.color("brown")
    john.begin_fill()
    for i in range(4):
        john.forward(200)
        john.left(90)
    john.end_fill()
house()

def roof():
    john.left(90)
    john.forward(200)
    john.right(90)
    john.penup()
    john.color("black")
    john.begin_fill()
    john.forward(200)
    for i in range(3):
        john.left(120)
        john.forward(200)
    john.end_fill()

roof()

phil.goto(75, 150)
def window():
    phil.color("cornflower blue")
    phil.begin_fill()
    for i in range(4):
        phil.right(90)
        phil.forward(50)
    phil.end_fill()
    phil.color("black")
    phil.right(90)
    phil.forward(25)
    phil.right(90)
    phil.pendown()
    phil.forward(50)
    phil.right(90)
    phil.penup()
    phil.forward(25)
    phil.right(90)
    phil.forward(25)
    phil.right(90)
    phil.pendown()
    phil.forward(50)
    phil.penup()

window()

phil.goto(175, 100)

window()

def sun():
    sven.begin_fill()
    sven.color("yellow")
    sven.circle(80)
    sven.end_fill()

sven.goto(-250, 200)
sun()

bob.color("saddle brown")
bob.goto(75, 0)

def door():
    bob.left(90)
    bob.begin_fill()
    bob.forward(100)
    bob.right(90)
    bob.forward(50)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(50)
    bob.end_fill()

door()

sven.goto(275, 0)
def tree():
    sven.color("sienna")
    sven.begin_fill()
    sven.left(90)
    sven.forward(150)
    sven.right(90)
    sven.forward(50)
    sven.right(90)
    sven.forward(150)
    sven.right(90)
    sven.forward(50)
    sven.end_fill()
    sven.right(90)
    sven.forward(200)
    sven.left(90)
    sven.back(25)
    sven.begin_fill()
    sven.color("green")
    sven.circle(50)
    sven.end_fill()

tree()

sven.goto(-150, 0)
sven.left(180)
tree()

def orange():
    bob.penup()
    bob.begin_fill()
    bob.color("orange")
    bob.circle(7)
    bob.end_fill()

bob.goto(-140, 175)
orange()
bob.goto(-110, 165)
orange()
bob.goto(-140, 145)
orange()
bob.goto(-120, 135)
orange()

bob.goto(275, 172)
orange()
bob.goto(315, 171)
orange()
bob.goto(295, 143)
orange()














scn.exitonclick()