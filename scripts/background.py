import pygame

from os import path, getcwd

from scripts.constantes import *

class Background(pygame.sprite.Sprite):
    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(getcwd() + f"/assets/images/{background}"))
        #self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.direction_y = 4
        self.reset()

    def update(self):
        self.rect.top += self.direction_y
        if self.rect.top >= 0:
            self.reset()

    def reset(self):
        self.rect.bottom = SCREEN_Y