import turtle
import random as r
import time
import math
don = turtle.Turtle()
screen = turtle.Screen()

don.hideturtle()
don.speed(0)
don.pencolor('white')
screen.colormode(255)


screen.bgcolor('black')
screen.setup(900,650,200,0)
screen.tracer(0,0)
screen.title('POLYGON')

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self,drawer):
        drawer.pensize(3)
        drawer.penup()
        drawer.setpos(self.x-1,self.y-1)
        drawer.pendown()
        for i in range(0,4):
            drawer.forward(3)
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



points = []
lines = []

def drawAll(_points,drawer):
    for p in _points:
        drawer.pencolor(r.randint(150,255),r.randint(150,255),r.randint(150,255))
        p.draw(drawer)
    screen.update()
    time.sleep(0.2)


def polygon(number,radius,pointlist):
    print('Polygon with ', number, ' sides')
    angle = 360/number
    don.penup()
    don.setpos(0,radius)
    edgelength = 2*radius*math.sin(math.radians(angle/2))

    print('Initializing and Printing...')

    pointlist.append(Point(don.xcor(), don.ycor()))
    don.right(angle/2)
    don.forward(edgelength)

    for i in range(0,number-1):
        pointlist.append(Point(don.xcor(),don.ycor()))
        don.right(angle)
        don.forward(edgelength)


    p1 = pointlist[0]
    already_exist = False
    while True:
        for p2 in pointlist:
            if p1 == p2:
                continue

            already_exist = False

            for line in lines:
                if (line.P1 == p1 and line.P2 == p2) or (line.P1 == p2 and line.P2 == p1):
                    already_exist = True
                    break

            if already_exist:
                continue

            else:
                lines.append(Line(p1,p2))

                don.pencolor((r.randint(100,255),r.randint(100,255),r.randint(100,255)))
                lines[len(lines)-1].draw(don)

                screen.update()

                time.sleep(0.1)  #remove for faster display

                templist = pointlist[pointlist.index(p2):len(pointlist)]
                templist.extend(pointlist[0:pointlist.index(p2)])
                pointlist = templist
                break

        p1 = p2

        if already_exist:
            break

    print('Done')
    don.pendown()


    time.sleep(2)
    pointlist.clear()
    lines.clear()
    don.clear()
    don.penup()
    don.setheading(0)
    don.setpos(0,0)
    polygon(number+1,radius,pointlist)

polygon(2,300,points)

screen.exitonclick()