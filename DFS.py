import random as r
class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []
        self.explored = False

    def is_explored(self):
        return self.explored

    def explore(self):
        self.explored = True

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbors(self):
        return self.neighbors

    def is_neighbor(self, node):
        isneighbor = False
        for i in self.neighbors:
            if i == node:
                isneighbor = True
                break
        return isneighbor

    def get_value(self):
        return self.value

    def is_not_neighbor(self, node):
        return not self.is_neighbor(node)

    def display(self):
        print(self.value,':',end = ' ')
        for i in self.neighbors:
            print(i.get_value(),end=',')
        print()

def generate_random_graph(n):
    addedlist = []
    for i in range(0,n):
        node = Node(i)
        if len(addedlist) != 0:
            randnode = r.choice(addedlist)
            node.add_neighbor(randnode)
            randnode.add_neighbor(node)
        for j in range(0,len(addedlist)):
            if (r.randint(0,10) < 3) and (node.is_not_neighbor(addedlist[j])):
                node.add_neighbor(addedlist[j])
                addedlist[j].add_neighbor(node)
        addedlist.append(node)
    return addedlist

def loop_bfs():
    node = stack.pop()
    print(node.get_value(),end=',')
    neighbors = node.get_neighbors()
    for k in neighbors:
        if not k.is_explored():
            stack.append(k)
            k.explore()
    if len(stack) == 0:
        return
    loop_bfs()
    return

nodelist = generate_random_graph(6)
for i in nodelist:
    i.display()

stack = []
rnode = r.choice(nodelist)
rnode.explore()
stack.append(rnode)
loop_bfs()
