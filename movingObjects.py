import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self, speed, image, startX, startY):

        self.speed = speed
        self.imageFile = image
        self.x = startX
        self.y = startY
        self.image = pygame.image.load(self.imageFile).convert_alpha()




    def move(self, screenSize, event=None, ):
        if event != None:
            if event.key == 273:  # UP
                self.y-= 10
            if event.key == 274:  # DOWN
                self.y += 10
            if event.key == 275:  # RIGHT
                self.x += 10
            if event.key == 276:  # LEFT
                self.x -= 10

            if self.x > screenSize:
                self.x = 0
                return (0,1)

            elif self.x < 0:
                self.x = screenSize
                return (0,-1)

            elif self.y > screenSize:
                self.y = 0
                return (1,0)

            elif self.y < 0:
                self.y = screenSize
                return (-1,0)

            else:
                return (0,0)

    def update(self, screen):


        screen.blit(self.image, (self.x, self.y))