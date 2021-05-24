import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("Sprites/Player.png")
        self.rect = pygame.Rect(50, 400, 64, 100)
        self.speed = 5
        self.timer = 0
        self.rect.x = 280

    def update(self, *args):
        # LOGICA
        #Keys recebe um dicionario de teclas que estão sendo pressionadas
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]: 
            self.rect.x += self.speed

        elif keys[pygame.K_a]:
            self.rect.x -= self.speed

        if self.rect.left < 100:
            self.rect.left = 100

        elif self.rect.right > 500:
            self.rect.right = 500

        if self.timer == 3600:
            self.speed += 2
            self.timer = 0

        self.timer += 1

        if self.speed >= 25:
            self.speed = 25
