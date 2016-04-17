class node:
    def __init__(self, num):
        self.neighbors = []
        self.num = num
        self.current = 0
        self.hop = -1
        self.bestpath = -1

    def append(self, t):
        for a in self.neighbors:
            if a == t:
                return False
        self.neighbors.append(t)

def calculate(n, edges, s):
    nodes = []
    output = ""
    for i in range(n):
        nodes.append(node(i))

    for edge in edges:
        edge = edge.split()
        addNeighbor(nodes[int(edge[0])-1], nodes[int(edge[1])-1])

    source = nodes[s-1]
    source.hop = 0
    expand(source, 0)

    for i in range(len(nodes)):
        if s-1 == i:
            continue
        #print("running for " + str(i) +" "+ str(s-1))
        output += " " + str(trace(nodes[i]))

    return output.strip()

def trace(node):
    if node.hop == 0:
        return 0
    elif node.hop == -1:
        return -1
    else:
        return 6 + trace(node.bestpath)

def expand(source, current_hop):
    

    for neighbor in source.neighbors:


        if neighbor.hop > current_hop + 1 or neighbor.hop == -1:
            #print("--------------\nnighbor: hop:" + str(neighbor.hop) + " / " + str(current_hop+1)+"\n-------------------")
            neighbor.hop = current_hop + 1
            neighbor.bestpath = source
            expand(neighbor, current_hop + 1)


def addNeighbor(n1, n2):
    n1.append(n2)
    n2.append(n1)
1


output = []
t = int(input().strip())
for a0 in range(t):
    temp = input().split()
    nodes = int(temp[0])
    edge = int(temp[1])
    edges = []
    for a1 in range(edge):
        edges.append(input())
    s = int(input())
    output.append(calculate(nodes,edges,s))

for t in output:
    print(t)