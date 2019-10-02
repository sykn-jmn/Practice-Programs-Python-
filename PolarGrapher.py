import turtle
import math

don = turtle.Turtle()
screen = turtle.Screen()
don.hideturtle()

don.speed(0)
screen.delay(0)
screen.tracer(0,0)
screen.bgcolor('black')
don.pencolor('white')

don.setpos(300,0)
don.setpos(-300,0)
don.setpos(0,0)
don.setpos(0,300)
don.setpos(0,-300)
don.setpos(0,0)
don.penup()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,drawer):
        drawer.pensize(1)
        drawer.penup()
        drawer.setpos(self.x,self.y)
        drawer.pendown()
        for i in range(0,4):
            drawer.forward(1)
            drawer.left(90)

class Line:
    def __init__(self,P1,P2):
        self.P1 = P1
        self.P2 = P2

    def draw(self,drawer):
        drawer.pensize(1)
        drawer.penup()
        drawer.setpos(self.P1.x,self.P1.y)
        drawer.pendown()
        drawer.setpos(self.P2.x, self.P2.y)

def drawAll(drawable,drawer):
    for p in drawable:
        p.draw(drawer)
        screen.update()

points = []
lines = []
angle = 1
while angle <360:
    radius = 200
    try:
        #radius = math.sqrt(4*4*math.cos(2*math.radians(angle))) *30        #supposed to be a lemniscate
        #radius = (   4*math.cos(3*math.radians(angle))   )      *40        #Rose with 3 petals
        #radius = (   6*math.cos(4*math.radians(angle))   )      *30        #Rose with 8 petals
        #radius = (  1-(2*math.sin(math.radians(angle)))  )      *20        #Cardiod |a/b| is equal to 1
        #radius = (  3+(5*math.cos(math.radians(angle)))  )      *20        #Loop    |a/b| is between 0 and 1
        #radius = (  7+(5*math.cos(math.radians(angle)))  )      *14        #Dent    |a/b| is between 1 and 2
        #radius = (  13+(5*math.cos(math.radians(angle))) )      *8         #Convex  |a/b| is greater than or equal 2
        #radius = (     1*(math.pow(1.017,angle))         )      *1         #Logarithmic Spiral
        #radius = (             2*angle                   )      /20        #Spiral of Archimedes
        #radius = (           1/(1*angle)                 )      *10000     #Reciprocal Spiral

        don.left(angle)
        don.forward(radius)
        points.append(Point(don.xcor(),don.ycor()))
        don.backward(radius)
        don.right(angle)
    except ValueError:
        print('Error')

    angle+=0.2  #The lesser, the more accurate the graph is
don.pendown()


for p in points:
    if points.index(p)+1 == len(points):
        break
    else:
        lines.append(Line(p,points[points.index(p)+1]))


drawAll(lines, don)

print('Done')
screen.exitonclick()