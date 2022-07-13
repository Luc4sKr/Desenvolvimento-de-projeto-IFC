import pygame

from scripts.constantes import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, vely):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(path.join(getcwd() + "/assets/images/bullet/bullet_1.png"))
        self.__image = pygame.transform.scale(self.__image, (6, 10))
        self.__rect = self.__image.get_rect()

        self.__rect.bottom = y
        self.__rect.centerx = x

        self.__speed_y = vely
        self.__damage = damage

    def update(self):
        self.__rect.y += self.__speed_y

        if self.__rect.bottom < 0 or self.__rect.top > SCREEN_Y:
            self.kill()


    # Image
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, new_image):
        self.__image = new_image

    # Rect
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    # Damage
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    # Speed
    @property
    def speed_y(self):
        return self.__speed_y

    @speed_y.setter
    def speed_y(self, speed_y):
        self.__speed_y = speed_y