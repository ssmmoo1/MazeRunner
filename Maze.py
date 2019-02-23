from random import randint
import tkinter as tk

#******************
mapSize = int(input("Grid Size: "))
cellSize =int( input("Pixel size of each square (try like 20):")) #number of pixels for each line that makes up a square


#************



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


    def checkUnvisited(self):
        for i in self.cells:
            for j in i:
                if j.visited == False:
                    return True
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

        while self.checkUnvisited():

            neighbors = current.getNeighbors()
            neighbors = self.elimNeighbors(neighbors)

            if len(neighbors) == 0:
                current.visited = True
                current = stack.pop()
                continue

            newPos = neighbors[randint(0, len(neighbors) - 1)]
            next = self.getCell(newPos[0], newPos[1])

            self.breakWall(current, next)
            stack.append(current)
            current.visited = True
            current = next


def drawMaze(map,w, root, cellSize):
    xCounter =cellSize
    yCounter =cellSize

    for i in map.cells:
        for j in i:

            sides = j.sides
            top = sides[0]
            right = sides[1]
            bottom = sides[2]
            left = sides[3]

            if top:
                w.create_line(xCounter, yCounter, xCounter + cellSize, yCounter)
            if right:
                w.create_line(xCounter+cellSize, yCounter, xCounter+cellSize, yCounter+cellSize )
            if bottom:
                w.create_line(xCounter, yCounter+cellSize, xCounter + cellSize, yCounter+cellSize)
            if left:
                w.create_line(xCounter, yCounter, xCounter, yCounter+cellSize)

            xCounter += cellSize

        xCounter = cellSize
        yCounter +=cellSize





map = Map(mapSize)
map.makeMaze()
root=tk.Tk()
w = tk.Canvas(root,width=((map.size + 1)* cellSize ), height=((map.size + 1) *cellSize  ))
w.pack()
drawMaze(map, w, root, cellSize)
for i in map.cells:
    for j in i:
        print(str(j.sides))

    print("\n")
tk.mainloop()

