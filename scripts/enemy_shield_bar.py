import pygame

from scripts.constantes import *
from __main__ import *

class Shield_bar(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.surface = screen

    def draw_shield_bar(self, shield, x, y):
        self.image = pygame.Surface((shield * ENEMY_BAR_WIDTH, ENEMY_BAR_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface.blit(self.image, self.rect)
        if shield < 0:
            self.kill()



