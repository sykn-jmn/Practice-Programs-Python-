import turtle
don = turtle.Turtle()
don.hideturtle()
screen = turtle.Screen()
don.speed(0)
screen.setup(width=1300, height=670, startx=10, starty=0)



import random
class Node:
    def __init__(self, value,x,y):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = []
        self.traversed = False

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_neighbor(self, n):
        for i in self.neighbors:
            if i == n:
                return
        don.penup()
        don.setpos(self.x,self.y)
        don.pendown()
        don.setpos(n.x,n.y)
        self.neighbors.append(n)

    def is_traversed(self):
        self.traversed = True

    def not_travered(self):
        self.traversed = False

    def startBFS(self):
        print(self.get_value(), end = ' ')
        self.is_traversed()
        self.BFSPrint()

    def BFSPrint(self):
        alltraversed = True
        for i in self.neighbors:
            if not i.traversed:
                print(i.get_value(), end = ' ')
                i.is_traversed()
                alltraversed = False
        if alltraversed:
            return
        for i in self.neighbors:
            i.BFSPrint()

class Graph:
    def __init__(self):
        self.nodes = []

    def set_nodes(self, nodes):
        self.nodes = nodes

    def printnodes(self):
        for i in self.nodes:
            print(i.get_value(),end = '; ')
            a = i.neighbors
            for j in a:
                print(j.get_value(), end = ' ')
            print()

    def printnumbers(self):
        for i in self.nodes:
            don.penup()
            don.setpos(i.x,i.y)
            don.pendown()
            don.fillcolor('white')
            don.backward(7)
            don.right(90)
            don.forward(7)
            don.left(90)
            don.begin_fill()
            for j in range(0,4):
                don.forward(15)
                don.left(90)
            don.end_fill()
            don.forward(5)
            don.write(i.get_value())

    def BFS(self):
        self.printnumbers()
        start = random.choice(self.nodes)
        print('BFS: ', end = '')
        start.startBFS()
        print()
        print('Done')

# MAIN ---------------------------------------------------
l1 = [] #1,2,3,5,6,7,8,10
nodes1 = [] #9,4
            #node = 4;9   9;4

for i in range(1,11):
    l1.append(i)

for i in range(0,len(l1)):
    c = random.choice(l1)
    node = Node(c,random.randint(-600,600),random.randint(-300,300))

    if len(nodes1) != 0:
        for i in range(0,random.randint(1,len(nodes1))):
            randneighbor = random.choice(nodes1)
            node.add_neighbor(randneighbor)
            randneighbor.add_neighbor(node)

    nodes1.append(node)
    l1.remove(c)
#--------------------------------------------------------
g = Graph()
g.set_nodes(nodes1)
g.printnodes()
g.BFS()


screen.exitonclick()