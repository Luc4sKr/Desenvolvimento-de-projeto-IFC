import pygame

from scripts.constantes import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, damage):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((5, 5))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.damage = damage

        self.rect.bottom = y
        self.rect.centerx = x

        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()