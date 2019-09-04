import turtle
turtle.shape("turtle")

turtle.speed(100000)
def square():
    for i in range(1,60):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.right(5)


square()
turtle.right(5)


turtle.exitonclick()