def sort(arr):
    e = arr[-1]
    index = len(arr)-2

    while True:
        if index == -1:
            arr[0] = e
            print_arr(arr)
            break

        if e < arr[index]:
            arr[index + 1] = arr[index]
            print_arr(arr)
        elif e >= arr[index]:
            arr[index+1] = e
            print_arr(arr)
            break
        else:
            print("ERROR")
            break

        index -= 1

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