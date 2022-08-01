import pygame

from random import randrange

from scripts.constantes import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__frame_index = 0
        self.__update_time = pygame.time.get_ticks()
        self.__animation_list = animation_list

        self.__image = self.__animation_list[self.__frame_index]

        self.__rect = self.__image.get_rect()

        self.__rect.x = randrange(SCREEN_X - self.__rect.width)
        self.__rect.y = randrange(-150, -100)
        self.__speedx = randrange(-1, 1)
        self.__speedy = randrange(5, 7)

    def update_animation(self):
        self.__image = self.__animation_list[self.__frame_index]

        if pygame.time.get_ticks() - self.__update_time > ASTEROID_ANIMATION_COOLDOWN:
            self.__update_time = pygame.time.get_ticks()
            self.__frame_index += 1
        if self.__frame_index >= len(self.__animation_list):
            self.__frame_index = 0

    def movement(self):
        self.__rect.x += self.__speedx
        self.__rect.y += self.__speedy

    def check_inside_on_screen(self):
        if self.__rect.top > SCREEN_Y:
            self.kill()

        if self.__rect.right < 0:
            self.kill()

        if self.__rect.left > SCREEN_X:
            self.kill()


    def update(self):
        self.movement()
        self.check_inside_on_screen()
        self.update_animation()



    # Image
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    
    # Rect
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect


    # Speedx
    @property
    def speedx(self):
        return self.__speedx

    @speedx.setter
    def speedx(self, speedx):
        self.__speedx = speedx

    
    # Speedy
    @property
    def speedy(self):
        return self.__speedy
    
    @speedy.setter
    def speedy(self, speedy):
        self.speedy = speedy