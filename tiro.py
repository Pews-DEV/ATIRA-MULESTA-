import pygame
import math
import random

class Tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Sprites/Tiro.png")
        self.rect = self.image.get_rect()


        self.timer = 0
        self.value = 1

        self.speed = 8

    def update(self, *args):
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
 