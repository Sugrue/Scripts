# # WORK IN PROGRESS



class cell():
    def __init__(self, value, next_cell=""):
        self.value = value
        self.next = next_cell
        self.level = None

class matrix():
    def __init__(self, array):
        self.height = len(array)
        self.width = len(array[0])
        self.grid = [cell("TEST")]*self.height

        for i in range(0, self.height):
            self.grid[i] = [cell("test")]*self.width

        self.init_cells(array)

    def init_cells(self, array):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = cell(array[y][x])

        self.nav_right(0,0,1)

    def nav_right(self, x, y, level):
        #print("NAV RIGHT")
        while self.grid[y][x].level is None and self.exist(self.grid[y], x+1) and self.grid[y][x+1].level is None:
            self.grid[y][x].next = self.grid[y][x+1]
            self.grid[y][x].level = level
            #print(str(self.grid[y][x].value) + " -> " + str(self.grid[y][x+1].value))
            x += 1
        self.nav_down(x,y, level)

    def nav_down(self, x, y, level):
        #print("NAV DOWN")
        while self.grid[y][x].level is None and self.exist(self.grid, y+1) and self.grid[y+1][x].level is None:
            self.grid[y][x].next = self.grid[y+1][x]
            self.grid[y][x].level = level
            #print(str(self.grid[y][x].value) + " -> " + str(self.grid[y+1][x].value))
            y += 1
        self.nav_left(x, y, level)

    def nav_left(self, x, y, level):
        #print("NAV LEFT")
        while self.grid[y][x].level is None and self.exist(self.grid[y], x-1) and self.grid[y][x-1].level is None:
            self.grid[y][x].next = self.grid[y][x-1]
            self.grid[y][x].level = level
            #print(str(self.grid[y][x].value) + " -> " + str(self.grid[y][x-1].value))
            x -= 1
        self.nav_up(x, y, level)

    def nav_up(self, x, y, level):
        #print("NAV UP")
        while self.grid[y][x].level is None and self.exist(self.grid, y-1) and (self.grid[y-1][x].level is None or self.grid[y-1][x].level == level):
            self.grid[y][x].next = self.grid[y-1][x]
            self.grid[y][x].level = level
            #print(str(self.grid[y][x].value) + " -> " + str(self.grid[y-1][x].value))
            y -= 1
        if self.grid[x+1][y+1].level is None:
            self.nav_right(x+1, y+1, level+1)

    def exist(self, array, index):
        if index == -1: return False
        try:
            test = array[index]
            return True
        except:
            return False

    def print(self, rotation=0):
        output = ""
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for y in range(0, self.height):
            for x in range(0, self.width):
                target = self.grid[y][x]
                for i in range(rotation):
                    target = target.next
                output += str(target.value) + "\t"
            output += "\n"
        print(output)
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


temp = input().split(" ")
rows = int(temp[0])
array = []
for i in range(rows):
    array.append(input().split(" "))

test = matrix(array)
test.print(int(temp[2]))