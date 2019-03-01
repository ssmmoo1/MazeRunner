from random import randint


class Cell:

    def __init__(self, r, c):
        self.sides = [1,1,1,1] #top, right,bottom, left
        self.visited = False
        self.row =r
        self.col = c

    def __str__(self):
        return (str(self.row) + "," + str(self.col))


    def getNeighbors(self):
        neighbors = []

        neighbors.append([self.row-1, self.col])
        neighbors.append( [self.row + 1, self.col])
        neighbors.append( [self.row, self.col-1])
        neighbors.append(  [self.row, self.col+1])
        return neighbors







class Map:

    def __init__(self, size):
        self.cells = []
        self.size =size
        for r in range(0, size):
            row = []
            for c in range(0, self.size):
                row.append(Cell(r, c))

            self.cells.append(row)

    def printMap(self):
        for i in self.cells:
            for x in i:
                print(x)


    def elimNeighbors(self, neighbors):
        i = 0
        while i < len(neighbors):
            r = neighbors[i][0]
            c = neighbors[i][1]


            if r < 0 or r >= self.size or c < 0 or c >= self.size or self.getCell(r,c).visited == True:
                del neighbors[i]
                i-=1
            i+=1
        return neighbors


    def getCell(self, r ,c):
        return self.cells[r][c]


    def getUnvisited(self):
        unvisited = []
        for i in self.cells:
            for j in i:
                if j.visited == False:
                    unvisited.append(j)

        return unvisited
        return False

    def breakWall(self, cell1, cell2):
        r1 = cell1.row
        r2 = cell2.row

        c1 = cell1.col
        c2 = cell2.col

        if r1 - r2 == 1:
            cell1.sides[0] = 0
            cell2.sides[2] = 0

        elif r1 - r2 == -1:
            cell1.sides[2]=0
            cell2.sides[0]=0

        elif c1-c2 == 1:
            cell1.sides[3] = 0
            cell2.sides[1] = 0

        elif c1-c2 == -1:
            cell1.sides[1]=0
            cell2.sides[3]=0

        else:
            print("ERROR BREAKING WALLS")



    def makeMaze(self):

        row = randint(0, self.size-1)
        col = randint(0, self.size-1)


        current = self.getCell(row,col)
        stack = []
        unvisited = len(self.getUnvisited())

        while unvisited > 0:

            neighbors = current.getNeighbors()
            neighbors = self.elimNeighbors(neighbors)

            if len(neighbors) == 0:
                if current.visited == False:
                    current.visited = True
                    unvisited -= 1
                current = stack.pop()
                continue

            newPos = neighbors[randint(0, len(neighbors) - 1)]
            #newPos = neighbors[0]
            next = self.getCell(newPos[0], newPos[1])

            self.breakWall(current, next)
            stack.append(current)
            if current.visited == False:
                current.visited = True
                unvisited-=1
            current = next