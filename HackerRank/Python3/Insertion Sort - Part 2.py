def sort(arr):
    index = 0
    while index < len(arr)-1:
        print_arr(arr)
        for j in range(index, -1, -1):
            if arr[j] > arr[j+1]:
                swap(j+1, j, arr)
            elif arr[j] < arr[j+1]:
                break
        index += 1


def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def print_arr(arr):
    output = str()
    for a in arr:
        output += " " + str(a)
    print(output.strip())

size = int(input().strip())
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

sort(arr)