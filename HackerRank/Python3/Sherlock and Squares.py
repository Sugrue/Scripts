import math

def watson_counts(a, b):
    n = math.ceil(math.sqrt(a))
    output = 0
    while True:
        if n**2 > b:
            break
        else:
            output += 1
        n += 1
    return output

output = []
t = int(input().strip())
for a0 in range(t):
    n = input().strip().split(" ")
    output.append(watson_counts(int(n[0]), int(n[1])))

for t in output:
    print(t)