import pygame

from scripts.constantes import *

class Boss(pygame.sprite.Sprite):
    def __init__(self, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__frame_index = 0 # Frame de animação
        self.__update_time = pygame.time.get_ticks() # Tempo de atualização
        self.__animation_list = animation_list

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__rect = self.__image.get_rect()

        self.__rect.center = (SCREEN_X/2, SCREEN_Y/2)





    # Image
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, body_image):
        self.__image = body_image


    # Rect
    @property
    def rect(self):
        return self.__rect