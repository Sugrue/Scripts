def calculate(prices):
    peaks = [0]*len(prices)
    peaks[len(prices)-1] = -1
    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            peaks[i-1] = 1 #buy
        elif prices[i-1] > prices[i]:
            peaks[i-1] = -1 #sell
        else:
            peaks[i-1] = 0 #nothing
    #print("Pre Decision: "+ str(peaks))

    for i in range(len(prices)-1, 0, -1):
        j = i -1

        while peaks[i] == -1 and j >= 0:
            if peaks[j] == -1 and prices[j] >= prices[i]:
         #       print("break triggered i:" + str(i) + " j:" + str(j))
                break
            peaks[j] = 1 #buy
            j -= 1

        #print("New Decision: "+ str(peaks))

    money = stocks = 0
    for i in range(len(prices)):
        if peaks[i] == 1:
            money -= prices[i]
            stocks += 1
        elif peaks[i] == -1:
            money += prices[i]*stocks
            stocks = 0
        else:
            print("wut")

    return money

output = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    output.append(calculate([int(i) for i in input().split()]))

for t in output:
    print(t)