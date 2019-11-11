import random as r
class Edge:
    def __init__(self,a,b, weight):
        self.weight = weight
        self.vertices = (a,b)

    def source(self):
        return self.vertices[0]
    def destination(self):
        return self.vertices[1]

print('Enter number of vertices:')
vertices_num = int(input())

vertices = []
for i in range(0,vertices_num):
    vertices.append(i)

edges = []
for i in range(0,vertices_num):
    for j in range(i+1,vertices_num):
        edges.append(Edge(i,j,r.randint(1,20)))


for i in range(0,len(edges)):
    for j in range(0,len(edges)):
        if i!=j:
            if edges[i].weight < edges[j].weight:
                temp = edges[i]
                edges[i] = edges[j]
                edges[j] = temp


final_edges = []

parents = []
for i in range(0,vertices_num):
    parents.append(i)

def find_parent(checked):
    if parents[checked]== checked:
        return checked
    else:
        return find_parent(parents[checked])

for edge in edges:
    dest = find_parent(edge.destination())
    source = find_parent(edge.source())
    if dest != source:
        final_edges.append(edge)
        parents[dest] = source

    if len(final_edges)== len(edges)-1:
        break

for e in edges:
    print(e.vertices[0],',',e.vertices[1],',',e.weight)

print('--------------')
for e in final_edges:
    print(e.vertices[0],',',e.vertices[1],',',e.weight)
