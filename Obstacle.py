import pygame

class Obstacle():
    x:float
    y:float
    width:float
    height:float
    image:pygame.image.load

    def __init__(self, x:float, y:float, w:float, h:float):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = pygame.image.load("Image\\Obstacle.png")

    def Render(self, screen):
        screen.blit(self.image, (self.x * 64, self.y * 64))

    def ComparPos(self, pos):
        if self.x == pos[0] and self.y == pos[1]:
            return True

        return False