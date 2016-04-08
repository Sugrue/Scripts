def sort(arr):
    index = counter = 0
    while index < len(arr)-1:
        for j in range(index, -1, -1):
            if arr[j] > arr[j+1]:
                swap(j+1, j, arr)
                counter += 1
        index += 1

    print(counter)

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

size = int(input().strip())
arr = input().split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

sort(arr)