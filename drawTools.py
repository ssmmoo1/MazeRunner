import pygame
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
def drawMaze(map, cellSize, screen):
    xCounter =cellSize
    yCounter =cellSize
    global BLACK
    global WHITE

    for i in map.cells:
        for j in i:

            sides = j.sides
            top = sides[0]
            right = sides[1]
            bottom = sides[2]
            left = sides[3]

            if top:
                pygame.draw.line(screen, BLACK, [xCounter, yCounter], [xCounter + cellSize, yCounter],1)
            if right:
                pygame.draw.line(screen, BLACK, [xCounter+cellSize, yCounter], [xCounter + cellSize, yCounter+cellSize],1)

            if bottom:
                pygame.draw.line(screen, BLACK, [xCounter, yCounter+cellSize], [xCounter + cellSize, yCounter+cellSize],1)

            if left:
                pygame.draw.line(screen, BLACK, [xCounter, yCounter], [xCounter, yCounter+cellSize],1)


            xCounter += cellSize

        xCounter = cellSize
        yCounter +=cellSize

def drawRoom(currentCell, screenSize, screen):
    sidesArr = currentCell.sides
    sides=""
    for n in sidesArr:
        sides+=str(n)
    screen.fill(WHITE)

    global BLACK
    oneThird = int(screenSize / 3)
    twoThirds = int(screenSize/3*2)
    thick = 10

    if sides == "0000":
        raise Exception

    elif sides =="0001":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, screenSize], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [twoThirds, screenSize], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [screenSize, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [screenSize, twoThirds], thick)

    elif sides == "0010":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, oneThird], thick)

        pygame.draw.line(screen, BLACK, [0, oneThird], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [screenSize, oneThird], thick)

        pygame.draw.line(screen, BLACK, [0, twoThirds], [screenSize, twoThirds], thick)

    elif sides == "0011":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, twoThirds], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, oneThird],thick)

        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [screenSize, oneThird], thick)
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [screenSize, twoThirds], thick)


    elif sides == "0100":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [oneThird, screenSize], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, screenSize], thick)

        pygame.draw.line(screen, BLACK, [0, oneThird], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [0, twoThirds], [oneThird, twoThirds], thick)

    elif sides == "0101":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, screenSize],thick)
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, screenSize], thick)

    elif sides == "0110":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, twoThirds], thick)

        pygame.draw.line(screen, BLACK, [0, oneThird], [oneThird, oneThird],thick)
        pygame.draw.line(screen, BLACK, [0, twoThirds], [twoThirds, twoThirds],thick)

    elif sides == "0111":
        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, twoThirds],thick)
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, twoThirds], thick)

        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [twoThirds, twoThirds],thick)


    elif sides == "1000":
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds ], [oneThird,screenSize ],thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds ], [twoThirds, screenSize ],thick)

        pygame.draw.line(screen, BLACK, [0, oneThird ], [screenSize,oneThird ], thick)

        pygame.draw.line(screen, BLACK, [0, twoThirds ], [oneThird,twoThirds ],thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds ], [screenSize, twoThirds ], thick)

    elif sides == "1001":
        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [oneThird, screenSize], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [twoThirds, screenSize],thick)

        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [screenSize, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [screenSize, twoThirds], thick)

    elif sides == "1010":
        pygame.draw.line(screen, BLACK, [0, oneThird], [screenSize, oneThird],thick)
        pygame.draw.line(screen, BLACK, [0, twoThirds], [screenSize, twoThirds],thick)

    elif sides == "1011":
        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [screenSize, oneThird],thick)
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [screenSize, twoThirds], thick)

        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [oneThird, twoThirds], thick)
    elif sides == "1100":
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [oneThird, screenSize], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [twoThirds, screenSize],thick)

        pygame.draw.line(screen, BLACK, [0, oneThird], [twoThirds, oneThird], thick)
        pygame.draw.line(screen, BLACK, [0, twoThirds], [oneThird, twoThirds],thick)

    elif sides == "1101":
        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [oneThird, screenSize], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [twoThirds, screenSize], thick)

        pygame.draw.line(screen, BLACK, [oneThird, oneThird], [twoThirds, oneThird], thick)


    elif sides == "1110":
        pygame.draw.line(screen, BLACK, [0, oneThird], [twoThirds, oneThird], thick)

        pygame.draw.line(screen, BLACK, [0, twoThirds], [twoThirds, twoThirds], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [twoThirds, twoThirds],thick)

    elif sides == "1111":
        pygame.draw.line(screen, BLACK, [twoThirds, 0], [twoThirds, oneThird], thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [twoThirds, screenSize], thick)

        pygame.draw.line(screen, BLACK, [twoThirds, oneThird], [screenSize, oneThird],thick)
        pygame.draw.line(screen, BLACK, [twoThirds, twoThirds], [screenSize, twoThirds], thick)

        pygame.draw.line(screen, BLACK, [oneThird, 0], [oneThird, oneThird],thick)
        pygame.draw.line(screen, BLACK, [oneThird, twoThirds], [oneThird, screenSize], thick)



        pygame.draw.line(screen, BLACK, [0, oneThird], [oneThird, oneThird], thick)
        pygame.draw.line(screen, BLACK, [0, twoThirds], [oneThird, twoThirds], thick)


    else:
        raise Exception

