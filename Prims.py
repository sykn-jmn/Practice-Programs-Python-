import random as r
class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node, weight):
        self.neighbors.append((node,weight))

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

class Prims:
    def __init__(self, nodelist, n):
        self.parentlist=[]
        for k in range(0,len(nodelist)):
            self.parentlist.append(k)
        self.result = self.primify(nodelist,n)

    def get_result(self):
        return self.result

    def primify(self, nodelist, n):
        edgelist = []
        finallist = []

        current_node = nodelist[0]

        while len(finallist) < n-1:
            print(current_node.get_value())
            neighbors = current_node.get_neighbors()
            for j in neighbors:
                if (not self.contains_edge((current_node,j[0],j[1]),edgelist)) and (not self.contains_edge((current_node,j[0],j[1]),finallist)):
                    edgelist.append((current_node,j[0],j[1]))

            copy = edgelist.copy()
            while True:
                minimum = self.get_min(copy)
                first_parent = self.get_parent(minimum[0].get_value())
                second_parent = self.get_parent(minimum[1].get_value())
                if (not first_parent == second_parent) and (not self.contains_edge(minimum,finallist)):
                    print(first_parent,':',second_parent)
                    self.parentlist[minimum[1].get_value()] = minimum[0].get_value()
                    finallist.append(minimum)
                    current_node = minimum[1]
                    break
                copy.remove(minimum)

        return finallist

    def get_parent(self,index):
        if self.parentlist[index] == index:
            return index
        else:
            return self.get_parent(self.parentlist[index])

    def get_min(self,from_list):
        minimum = from_list[0]
        for k in from_list:
            if not k == minimum:
                if k[2]<minimum[2]:
                    minimum = k
        return minimum


    def contains_edge(self,edge,search_from):
        if len(search_from)!=0:
            for k in search_from:
                if (k[0] == edge[0] and k[1] == edge[1]) or (k[0] == edge[1] and k[1] == edge[0]):
                    return True
            return False
        else:
            return False




    def print_edges(self):
        for k in self.result:
            print(k[0].get_value(),',',k[1].get_value(),',',k[2])


node_num = 7
nodes = generate_random_graph(node_num)
for i in nodes:
    i.display()
print('---------------------------')
prim = Prims(nodes,node_num)
print('Done')
prim.print_edges()