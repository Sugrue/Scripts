# def solve(array):
#     if len(array) == 1:
#         return "YES"
#
#     for i in range (1, len(array)-1):
#         if sum(array[:i]) == sum(array[i+1:]):
#             return "YES"
#
#     return "NO"
#
def sum(array):
    output = 0
    for i in array:
        output += i
    return output

def solve(array):
    if len(array) == 1: return "YES"

    left = 0
    right = sum(array) - array[0]

    for i in range(1, len(array)-1):
        left += array[i-1]
        right -= array[i]

        if left == right:
            return "YES"

    return "NO"



for i in range(0, int(input())):
    input()
    array = input().split(" ")
    for t in range(0, len(array)):
        array[t] = int(array[t])
    print(solve(array))
