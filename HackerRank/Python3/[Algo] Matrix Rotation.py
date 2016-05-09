DOWN = 1
RIGHT = 2
UP = 3
LEFT = 4
LEVELUP = 5

class pixel():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        self.level = None

class coor():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        return "COOR: X: " + str(self.x) + " Y: " + str(self.y)

class Matrix():
    def __init__(self, m, n, r):
        self.__row = m
        self.__collumn = n
        self.__r = r
        self.__matrix = [None]*self.__collumn
        for i in range(self.__row):
            self.__matrix[i] = [None]*self.__row
        self.__current_row = 0

    def addrow(self, row):
        assert len(row) == self.__collumn and self.__current_row < self.__row
        for i in range(0, self.__collumn):
            self.__matrix[self.__current_row][i] = pixel(row[i])
        self.__current_row += 1

    def getcoor(self, coor):
        return self.__matrix[coor.x][coor.y]

    def rotate(self):
        self.__plotlevels()
        self.__rotate(self.__r)
        self.__printpath()
        self.__levels()


    def __next_direction(self, previous, coor):

        if coor.x+1 >= self.__collumn or coor.x-1 < 0 or coor.y+1 >= self.__row or coor.y-1 < 0:
            return (previous + 1) % 6
        elif previous == DOWN and self.__matrix[coor.x][coor.y+1].next == None:
            return DOWN
        elif previous == RIGHT and self.__matrix[coor.x+1][coor.y].next == None:
            return RIGHT
        elif previous == UP and self.__matrix[coor.x-1][coor.y].next == None:
            return UP
        elif previous == LEFT and self.__matrix[coor.x-1][coor.y].next == None:
            return LEFT
        else:
            print("ERROR" + str(previous) + coor.print())

        return (previous + 1) % 6

    def __plotlevels(self):
            current = coor(0,0)
            previous = coor(1,0)
            level = 0
            direction = DOWN

            while True:
                if direction == DOWN:
                    next = coor(current.x, current.y+1)
                elif direction == RIGHT:
                    next = coor(current.x+1, current.y)

                elif direction == UP:
                    next = coor(current.x, current.y-1)

                elif direction == LEFT:
                    next = coor(current.x-1, current.y)

                elif direction == LEVELUP:
                    next = coor(current.x-1, current.y)
                    self.getcoor(current).next = self.getcoor(next)
                    self.getcoor(current).previous = self.getcoor(previous)
                    current = coor(next.x+1, next.y+1)
                    previous = coor(next.x+2, next.y+1)
                    if self.getcoor(current).next == None:
                        direction = DOWN
                        continue
                    else:
                        print("COMPLETE")
                        break
                else:
                    break
                self.getcoor(current).previous = self.getcoor(previous)
                self.getcoor(current).next = self.getcoor(next)

                previous = current
                current = next
                direction = self.__next_direction(direction,current)

    def __rotate(self, r):

        for i in range(0, r):
            current_coor = coor(0,0)
            current = self.getcoor(current_coor)
            level = 0

            tmp = current.previous.data
            while current.next.level == None:
                self.__printpath()
                t = tmp
                tmp = current.data
                current.data = t
                current.level = level
                current = current.next


            current.next.data = tmp
            current_coor.x += 1
            current_coor.y += 1
            level += 1

            current = self.getcoor(current_coor)
            if current.level != None or current.next is None:
                break

    def __printpath(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for row in self.__matrix:
            output = ""
            for pixel in row:
                output += pixel.data + " "
            print(output.strip())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def __levels(self):
        for row in self.__matrix:
            output = ""
            for pixel in row:
                output += str(pixel.level) + " "
            print(output.strip())

mnr = input().split(" ")
matrix = Matrix(int(mnr[0]), int(mnr[1]), int(mnr[2]))
for i in range(int(mnr[0])):
    matrix.addrow(input().split(" "))

matrix.rotate()