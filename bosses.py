import pygame
import math
import random

class Boss(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Sprites/Boss.png")
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.y = 20
        self.rect.x = 200

        self.speed = 4

        self.timer = 0

    def update(self, *args):

        self.timer += 0.01
        self.rect.x = 250 + math.sin(self.timer) * 200 
        
