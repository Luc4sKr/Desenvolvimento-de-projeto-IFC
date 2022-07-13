import pygame

from math import sqrt

from scripts.constantes import *

class Missil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, damage, obj_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy

        self.vely = 3

        self.damage = damage

        self.obj_pos = obj_pos
        self.obj_pos_x = obj_pos[0]
        self.obj_pos_y = obj_pos[1]


    def update(self):
        if self.rect.centerx >= self.obj_pos_x:
            self.rect.centerx += 0
            self.rect.y -= self.vely
        if self.rect.centerx < self.obj_pos_x:
            self.rect.centerx -= 0
            self.rect.y -= self.vely

