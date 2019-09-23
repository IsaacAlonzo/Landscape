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



john.left(90)


























scn.exitonclick()