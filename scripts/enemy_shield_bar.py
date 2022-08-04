import pygame

from scripts.constantes import *
from __main__ import *

class Shield_bar(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.__surface = surface
        self.temp = 0

    def draw_shield_bar(self, shield, enemy_rect):
        
        if shield > self.temp:
            self.temp = shield

        self.__image = pygame.Surface(((shield * enemy_rect.width) / self.temp, ENEMY_BAR_HEIGHT))
        self.__image.fill(GREEN)
        self.__rect = self.__image.get_rect()
        self.__rect.x = enemy_rect.x
        self.__rect.y = enemy_rect.y
        self.__surface.blit(self.__image, self.__rect)

        if shield <= 0:
            self.kill()


