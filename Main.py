from random import randint
import pygame
import drawTools
import mazeTools
import movingObjects
from time import sleep

#******************
mapSize = int(input("Grid Size: "))
#cellSize =int( input("Pixel size of each square (try like 20):")) #number of pixels for each line that makes up a square
#mapSize = 20
cellSize = 10

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
pygame.init()
screenSize = 500
#screen = pygame.display.set_mode([(mapSize + 2) * cellSize,(mapSize + 2) * cellSize])
screen = pygame.display.set_mode([screenSize, screenSize])

screen.fill(WHITE)
#************

clock = pygame.time.Clock()

player = movingObjects.Player(10,"graphics/DinoPlayer.png", screenSize/2, screenSize/2)

map = mazeTools.Map(mapSize)
map.makeMaze()


currentR = randint(0, mapSize - 1)
currentC = randint(0, mapSize - 1)

currentCell = map.getCell(currentR, currentC)

drawTools.drawRoom(currentCell, screenSize, screen)

pygame.display.flip()

done = False
while(not done):
    clock.tick(30)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    if event.type == pygame.KEYDOWN:
        cellOffset = player.move(screenSize, event=event)
        currentR+= cellOffset[0]
        currentC+= cellOffset[1]

    currentCell = map.getCell(currentR, currentC)

    drawTools.drawRoom(currentCell, screenSize, screen)
    player.update(screen)
    pygame.display.flip()