import pygame
import math
import random

class Zone(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
 
        self.image = pygame.image.load("Sprites/Killzone.png")
        self.rect = self.image.get_rect()


        self.timer = 0
        self.value = 1

        self.speed = 100

    def update(self, *args):
        self.rect.y -= self.speed

        if self.rect.bottom < -400:
            self.kill()
