import pygame
from Engine import Engine
from AI import AI
from Timer import Timer
from Player import Player
from Apple import Apple
from Map import Map

class Game:
    isRun:bool

    width:int = 1000
    height:int = 800
    size:float = []

    screen:pygame.display.set_mode

    BGColor:int = [2, 0, 102]

    engine:Engine

    timer:Timer

    AI:AI

    player:Player

    apple:Apple

    map:Map

    def __init__(self):
        self.isRun = True
        self.engine = Engine()
        self.timer = Timer()
        pygame.init()
        self.GameInit()

    def GameInit(self):
        self.size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.size)

        self.map = Map("Map", "Image\\Map.tmx")
        self.engine.AddActor(self.map)

        self.AI = AI("AI", "Image\\Zombi.png")
        self.AI.SetMap(self.map)
        self.engine.AddActor(self.AI)

        self.engine.Start()

    def GameLoop(self):
        self.timer.Update()

        self.ProcessInput()

        self.engine.Update(self.timer.GetDeltaTime())

        self.Render()

        return self.isRun

    def ProcessInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRun = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    # update la destination final et la destination a aller
                    self.AI.UpdateFinalDest(pygame.mouse.get_pos())
                    self.AI.UpdateDest(pygame.mouse.get_pos())
                    self.AI.SetTransition("Seek")
                if pygame.mouse.get_pressed()[2]:
                    # ajoute un obstacle dans la map
                    self.map.AddObstacle(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.player.ChangeState()



    def Render(self):
        self.screen.fill(self.BGColor)

        self.engine.Render(self.screen)

        pygame.display.flip()

    def ChangeMode(self, mode:str):
        self.AI.SetState(mode)
