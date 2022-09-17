from scripts.constants import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, coin_group):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(COIN_IMAGE).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (COIN_WIDTH, COIN_HEIGHT))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (pos_x, pos_y)

        coin_group.add(self)

    def update(self):
        self.__rect.y += 2

    # --- GETTERS AND SETTERS --- #

    # --Image
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    # --Rect
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
