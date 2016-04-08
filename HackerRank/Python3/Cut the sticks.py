def cut(sticks):
    smallest = sticks[0]
    output = []
    for t in sticks:
        if t < smallest:
            smallest = t

    for t in sticks:
        if t - smallest > 0:
            output.append(t)
    return output

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while len(arr) > 0:
   print(len(arr))
   arr = cut(arr)