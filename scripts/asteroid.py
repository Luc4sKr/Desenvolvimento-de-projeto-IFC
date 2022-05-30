import pygame

from random import randrange

from scripts.constantes import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()

        self.rect.x = randrange(SCREEN_X - self.rect.width)
        self.rect.y = randrange(-150, -100)
        self.speedx = randrange(-3, 3)
        self.speedy = randrange(3, 5)

    def update_animation(self):
        self.image = self.animation_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > SCREEN_Y + 10 or self.rect.left < -100 or self.rect.right > SCREEN_X + 100:
            self.rect.x = randrange(SCREEN_X - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speedy = randrange(1, 8)

        self.update_animation()
