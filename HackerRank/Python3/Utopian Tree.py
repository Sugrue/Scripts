SUMMER = False
SPRING = True

def recurse_cycle(season, height, cycle):
    if season == SUMMER:
        height += 1
        season = SPRING
    else:
        height *= 2
        season = SUMMER

    if cycle > 0:
        return recurse_cycle(season, height, cycle - 1)
    else:
        return height

def getheight(cycles):
    return recurse_cycle(SUMMER, 0, cycles)

output = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    output.append(getheight(n))

for t in output:
    print(t)