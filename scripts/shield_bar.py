import pygame

from scripts.constantes import *

class Shield_bar(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.__surface = surface
        self.temp = 0

    def draw_shield_bar(self, shield, enemy_rect, additional_x_position=0, additional_y_position=0, margin=0):
        
        if shield > self.temp:
            self.temp = shield

        self.__image = pygame.Surface(((shield * (enemy_rect.width + margin)) / self.temp, SHIELD_BAR_HEIGHT))
        self.__image.fill(GREEN)
        self.__rect = self.__image.get_rect()
        self.__rect.x = enemy_rect.x + additional_x_position
        self.__rect.y = enemy_rect.y + additional_y_position
        self.__surface.blit(self.__image, self.__rect)

       