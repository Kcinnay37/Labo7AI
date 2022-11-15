from Actor import Actor
import pytmx
import pygame
from pytmx.util_pygame import load_pygame
from Obstacle import Obstacle

class Map(Actor):
    image:pytmx.TiledMap
    obstacle:Obstacle = []

    def __init__(self, tag:str, path:str):
        super().__init__(tag)

        self.image = load_pygame(path)


    def AddObstacle(self, mousePos):
        temp = Obstacle(int(mousePos[0] / 64), int(mousePos[1] / 64), 64, 64)
        self.obstacle.append(temp)

    def Render(self, screen):
        for x, y, image in self.image.layers[0].tiles():
            screen.blit(image, (x * 64, y * 64))

        for o in self.obstacle:
            o.Render(screen)

    def CheckObstacle(self, point):
        x = int(point[0] / 64)
        y = int(point[1] / 64)

        for o in self.obstacle:
            if o.ComparPos([x, y]):
                return [x, y]
        return None

    def Start(self):
        pass

    def Update(self, dt:float):
        pass