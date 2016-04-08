def chocolateFeast(n, c, m):
    return n//c + recurse_wrapper(n//c, m)

def recurse_wrapper(wrappers, m):
    if wrappers >= m:
        return 1 + recurse_wrapper(wrappers-m+1, m)
    elif wrappers < m:
        return 0


t = int(input().strip())
output = []
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    output.append(chocolateFeast(n,c,m))

for t in output:
    print(t)