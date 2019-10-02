import turtle
import time

don = turtle.Turtle()
screen = turtle.Screen()
don.hideturtle()
don.speed(0)
don.pensize(3)
don.penup()
screen.delay(0)
screen.tracer(0)

print('Left, Right, Up and Down Arrows')
class Player:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velX=0
        self.velY=0

    def draw(self):
        draw_square(self.x,self.y,50)

    def update(self):
        self.x += self.velX
        self.y += self.velY
        self.gravity()
        self.friction()


    def gravity(self):
        if self.y<=-200:
            self.y = -199
        elif self.y>-200:
            self.velY-=1

    def friction(self):
        if (self.velX>-0.1) and (self.velX < 0.1):
            self.velX = 0
        if self.velX!=0:
            self.velX -= (self.velX*1/10)


    def jump(self):
        self.velY=20

    def left(self):
        self.velX = -2

    def right(self):
        self.velX = 2

    def stop(self):
        self.velX = 0

player = Player(0,0)

screen.onkey(player.jump,"Up")
screen.onkeypress(player.left,"Left")
screen.onkeypress(player.right,"Right")
screen.listen()



class Game:

    def __init__(self, object):
        self.object = object

    def draw(self):
        self.object.draw()

    def update(self):
        self.object.update()


game = Game(player)


def draw_square(x,y,side):
    don.setpos(x,y)
    don.pendown()
    for i in range(4):
        don.forward(side)
        don.right(90)
    don.penup()

def draw():
    don.clear()
    game.draw()
    game.update()
    screen.update()


def loop():
    fps = 1 / 60
    current_time = 0
    time_passed = 0
    past_time = time.time()
    while True:
        current_time = time.time()
        time_passed += current_time - past_time
        past_time = current_time
        if time_passed >= fps:
            draw()
            time_passed = 0


loop()


screen.exitonclick()
