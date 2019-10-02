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
screen.setup(900,700,200,0)
screen.tracer(0,0)

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

def lop(number):
    x = 400
    y = 200
    for i in range(0,number):
        points.append(Point(r.randint(-x,x),r.randint(-y,y)))

    go = True
    print('Printing...')
    drawAll(points, don)
    counter = 0

    for p1 in points:
        counter+=1
        for p2 in points:
            go = True
            tempLine = Line(p1,p2)
            for ch in lines:
                if (ch.P1 == p1 and ch.P2 == p2) or (ch.P1 == p2 and ch.P2 == p1):
                    go = False
            if go:
                lines.append(tempLine)
        print('Point ', counter, ' Finished')
        drawAll(lines, don)
        lines.clear()

    print('Done')
    time.sleep(2)
    don.clear()
    lines.clear()
    points.clear()
    lop(number+1)


def drawAll(_points,drawer):
    for p in _points:
        drawer.pencolor(r.randint(150,255),r.randint(150,255),r.randint(150,255))
        p.draw(drawer)
    screen.update()
    time.sleep(0.2)

lop(5)
screen.exitonclick()