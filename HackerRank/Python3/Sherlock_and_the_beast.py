#Pre-research attempt Fails miserably with large numbers

class DecentNumber():
    def __init__(self, length):
        starting = ""
        result = 0

        for i in range (0, length):
            starting += "5"
        num = int(starting)

        while True:
            if self._isdecent(num):
                self.result = num
                break
            print("D START")
            t = self._decrement(num)
            print("D END")
            if t == num:
                self.result = -1
                break
            else:
                num = t


    def _isdecent(self, number):
        print(number)
        if str(number).strip("5").strip("3") == "":
            threes = len(str(number).strip("5"))
            fives = len(str(number).strip("3"))
            if threes % 5 != 0:
                return False
            if fives % 3 != 0:
                return False
            return True
        else:
            return False

    def _decrement(self, num):

        for i in range(len(str(num))-1, -1, -1):
            if str(num)[i] == "5":
                num = int( str(num)[:i] + "3" + str(num)[i+1:])
                for j in range(i, len(str(num))):

                    if j == i:
                        continue

                    if str(num)[j] == "3":
                        num = int( str(num)[:j] + "5" + str(num)[j+1:])
                    else:
                        print("ERROR")
                        break
                break
            else:
                continue
            break


        return num

    def getresult(self):
        return self.result


def decentnumber(fives):
    threes = 0

    while fives >= 0:
        if fives % 3 == 0:
            if threes % 5 == 0:
                return '5'*fives+'3'*threes
        fives -= 1
        threes += 1
    return -1


def main():
#Pre-research attempt Fails miserably with large numbers
#    test = DecentNumber(1000000)
#    print(test.getresult())

#   Neat!
    output = []
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        output.append(decentnumber(n))

    for t in output:
        print(t)



main()