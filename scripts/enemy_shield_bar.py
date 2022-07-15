import pygame

from scripts.constantes import *
from __main__ import *

class Shield_bar(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.__surface = surface

    def draw_shield_bar(self, shield, x, y):
        self.__image = pygame.Surface((shield * ENEMY_BAR_WIDTH, ENEMY_BAR_HEIGHT))
        self.__image.fill(GREEN)
        self.__rect = self.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y
        self.__surface.blit(self.__image, self.__rect)
        if shield < 0:
            self.kill()


