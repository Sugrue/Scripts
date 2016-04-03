if __name__ == '__main__':

    num = int(input())
    students = {}
    for i in range (0, num):
        t = input()
        t = t.split(" ")
        students[t[0]] = (float(t[1]) + float(t[2]) + float(t[3]))/3

    print("%0.2f" % students[input()])