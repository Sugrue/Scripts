def find_digits(number):
    output = 0
    for n in str(number):
        if int(n) == 0: continue
        if number % int(n) == 0:
            output += 1

    return output

output = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    output.append(find_digits(n))

for t in output:
    print(t)