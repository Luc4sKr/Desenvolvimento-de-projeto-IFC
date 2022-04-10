import pygame

from scripts.constantes import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list

        self.image = self.animation_list[self.action][self.frame_index]
        #self.image = pygame.transform.scale(self.image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        #self.rect = pygame.Rect(0, 0, ENEMY_SIZE_X, ENEMY_SIZE_Y)
        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_X/2, SCREEN_Y/2)

    
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    def update(self):
        self.update_animation()
