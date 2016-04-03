def maxWidth(road, a, b):
    smallest = road[a]
    for i in range(a, b+1):
        t = road[i]
        if smallest > t:
            smallest = t
    return smallest

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(x) for x in input().strip().split(' ')]

output = []
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    output.append(maxWidth(width, i, j))

for t in output:
    print(t)