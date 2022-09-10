import pygame

from random import choice
from os import path, getcwd

from scripts.constants import *


class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        powerup_images = {
            "shield": pygame.image.load(path.join(getcwd() + "/assets/images/powerups/shield.png")).convert_alpha(),
            "gun": pygame.image.load(path.join(getcwd() + "/assets/images/powerups/gun.png")).convert_alpha()
        }

        # Imagem
        self.__type = choice(["shield", "gun"]) # Escolhe aleatoriamente o tipo
        self.__image = powerup_images[self.__type]

        if self.__type == "shield":
            self.__image = pygame.transform.scale(self.__image, (40, 40))
        else:
            self.__image = pygame.transform.scale(self.__image, (40, 40))

        self.__rect = self.__image.get_rect()
        self.__rect.center = center

        # Velocidade y
        self.__speedy = 3

    def update(self):
        self.__rect.y += self.__speedy

        if self.__rect.top > SCREEN_Y:
            self.kill()



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


    # Speedy
    @property
    def speedy(self):
        return self.__speedy

    @speedy.setter
    def speedy(self, speedy):
        self.__speedy = speedy


    # Type
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type


