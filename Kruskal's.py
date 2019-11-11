import random as r

class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node, weight):
        self.neighbors.append((node,weight))

    def remove_neighbor(self, node):
        for k in range(0, len(self.neighbors)):
            neighbor = self.neighbors[k]
            if neighbor[0] == node:
                self.neighbors.pop(k)
                return

    def clear_neighbors(self):
        self.neighbors.clear()

    def get_neighbors(self):
        return self.neighbors

    def is_neighbor(self,node):
        isneighbor = False
        for i in self.neighbors:
            if i[0] == node:
                isneighbor = True
                break
        return isneighbor
    def get_value(self):
        return self.value

    def is_not_neighbor(self,node):
        return not self.is_neighbor(node)

    def display(self):
        print(self.value,':',end = ' ')
        for i in self.neighbors:
            print('(',i[0].get_value(),',',i[1],')', end = ' ')
        print()


def generate_random_graph(n):
    addedlist = []
    for i in range(0,n):
        node = Node(i)
        if len(addedlist) != 0:
            randnode = r.choice(addedlist)
            randweight = r.randint(1,20)
            node.add_neighbor(randnode,randweight)
            randnode.add_neighbor(node,randweight)
        for j in range(0,len(addedlist)):
            if (r.randint(0,10) < 3) and (node.is_not_neighbor(addedlist[j])):
                randweight = r.randint(1,20)
                node.add_neighbor(addedlist[j],randweight)
                addedlist[j].add_neighbor(node,randweight)
        addedlist.append(node)
    return addedlist


class Kruskal:
    def __init__(self, nodelist):
        self.edges = self.edgify(nodelist)
        self.parent_list = []
        for k in range(0, len(nodelist)):
            self.parent_list.append(k)
        self.edges = self.kruskalify(self.edges,len(nodelist))
        self.nodelist = nodelist
        for k in self.nodelist:
            k.clear_neighbors()
        for k in self.edges:
            k[0].add_neighbor(k[1],k[2])
            k[1].add_neighbor(k[0],k[2])



    def kruskalify(self, edgelist, n):
        finallist = []
        while len(finallist) < n-1:
            minimum = self.get_minimum(edgelist)
            first_parent = self.get_parent(minimum[0].get_value())
            second_parent = self.get_parent(minimum[1].get_value())
            if not first_parent == second_parent:
                finallist.append(minimum)
                self.parent_list[second_parent] = first_parent
            edgelist.remove(minimum)
        return finallist

    def get_parent(self, index):
        if self.parent_list[index] == index:
            return index
        else:
            return self.get_parent(self.parent_list[index])

    def get_minimum(self, edgelist):
        minimum = edgelist[0]
        for k in edgelist:
            if k[2] < minimum[2]:
                minimum = k
        return minimum

    def edgify(self, nodelist):
        allneighbors = []
        for k in nodelist:
            for j in k.get_neighbors():
                allneighbors.append((k, j[0], j[1]))
        for k in allneighbors:
            for j in allneighbors:
                if not k == j:
                    if (j[2] == k[2]) and ((j[1] == k[1] and j[0] == k[0]) or (j[0] == k[1] and j[1] == k[0])):
                        allneighbors.remove(j)
        return allneighbors

    def display_edges(self):
        for k in self.edges:
            print(k[0].get_value(),',',k[1].get_value(),'=',k[2])

    def display_nodes(self):
        for k in self.nodelist:
            k.display()



node_num = 6
nodes = generate_random_graph(node_num)
for i in nodes:
    i.display()
print('---------------------------')
kruskal = Kruskal(nodes)
kruskal.display_edges()
print('- - - - - - - - - - - - - -')
kruskal.display_nodes()
