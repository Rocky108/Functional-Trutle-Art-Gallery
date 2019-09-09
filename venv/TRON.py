import turtle

turtle.bgcolor("Black")
turtle.color("Deepskyblue")
turtle.speed(1000)
turtle.pu()
turtle.backward(400)
turtle.pd()
turtle.pensize(10)
turtle.right(90)
turtle.circle(400)
turtle.left(90)
turtle.pu()
turtle.forward(125)
turtle.right(90)
turtle.forward(10)
turtle.pd()
turtle.circle(275)
turtle.right(90)
turtle.pu()
turtle.forward(60)
turtle.goto(-175,290)
turtle.left(36)
turtle.pd()
def trondisk():
    for i in range(1,31):
        turtle.forward(60)
        turtle.left(10)

trondisk()
turtle.pu()
turtle.goto(-50,0)
turtle.left(90)
turtle.forward(100)
turtle.pd()
turtle.color("Orangered")


turtle.right(155)
turtle.forward(175)
turtle.right(90)
turtle.forward(60)

def TronTitle(sidelength):
    for i in range(1,10):
        turtle.forward(sidelength)
        turtle.left(20)
TronTitle(10)

turtle.forward(175)

TronTitle(10)
turtle.forward(60)
turtle.right(90)
turtle.forward(165)
TronTitle(10)

turtle.right(90)
turtle.pu()
turtle.forward(30)
turtle.pd()
turtle.right(90)

def TronT():
    for i in range(1,10):
        turtle.forward(5)
        turtle.left(20)
TronT()
turtle.forward(50)

def TronR():
    for i in range(1,10):
        turtle.forward(5)
        turtle.right(20)
TronR()
TronT()
TronTitle(15)
turtle.forward(58)
turtle.pu()
turtle.forward(15)
turtle.left(90)
turtle.forward(130)
turtle.pd()
turtle.circle(40)
turtle.pu()
turtle.forward(15)
turtle.left(90)
turtle.forward(40)
turtle.pd()
turtle.circle(15)

turtle.pu()
turtle.backward(30)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.pd()
TronTitle(5)
turtle.forward(40)
TronR()
turtle.forward(40)
TronTitle(5)
turtle.forward(40)
TronTitle(15)
turtle.forward(45)

turtle.exitonclick()