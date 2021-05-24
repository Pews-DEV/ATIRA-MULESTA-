import pygame
import math
import random

class Laser(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Sprites/Laser.png")
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.y = 100
        self.rect.x = random.randint(200, 400)

        self.speed = 8

    def update(self, *args):
        self.rect.y += self.speed 

        if self.rect.bottom < 0:
            self.kill()

        
