import pygame

from scripts.constantes import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__animation_list = animation_list

        self.__frame_index = 0
        self.__update_time = pygame.time.get_ticks()
        self.__image = self.__animation_list[0]
        self.__rect = self.__image.get_rect()
        self.__rect.center = center

        pygame.mixer.Sound.play(EXPLOSION_SOUND)

    def update_animation(self):
        if pygame.time.get_ticks() - self.__update_time > EXPLOSION_ANIMATION_COOLDOWN:
            self.__update_time = pygame.time.get_ticks()
            self.__frame_index += 1
            if self.__frame_index == len(self.__animation_list):
                self.kill()
            else:
                center = self.__rect.center
                self.__image = self.__animation_list[self.__frame_index]
                self.__rect.center = center

    def update(self):
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
