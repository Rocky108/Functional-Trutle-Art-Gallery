import turtle

turtle.speed(1000000000)

def starspiral(howMany):
    for num in range (howMany):
        turtle.forward(num)
        turtle.right(144)
        turtle.forward(num)
        turtle.right(144)
        turtle.forward(num)
        turtle.right(144)
        turtle.forward(num)
        turtle.right(144)
        turtle.forward(num)
        turtle.right(144)
        turtle.right(5)

starspiral(100)
turtle.color("red")
turtle.penup()
turtle.forward(300)
turtle.pendown()
starspiral(100)
turtle.color("darkgreen")
turtle.penup()
turtle.forward(300)
turtle.pendown()
starspiral(100)

turtle.exitonclick()