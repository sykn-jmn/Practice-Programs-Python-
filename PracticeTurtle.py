import turtle


don = turtle.Turtle()
don.shape('turtle')
screen = turtle.Screen()
don.fillcolor("yellow")

for i in range(4):
    don.forward(100)
    don.left(90)

screen.exitonclick()
