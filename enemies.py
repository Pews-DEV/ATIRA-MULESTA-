import pygame
import math
import random

class Enemies(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Sprites/Inimigo.png")
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.y = -700 + random.randint(2, 400)
        self.rect.x = random.randint(150, 450)

        self.speed = 1 + random.randint(1,5)

    def update(self, *args):
        self.rect.y += self.speed

        if self.rect.bottom > 600:
            self.kill()  

