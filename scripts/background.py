from scripts.constants import *


class Background(pygame.sprite.Sprite):
    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(path.join(getcwd() + f"/assets/images/backgrounds/{background}")).convert()
        self.__rect = self.__image.get_rect()
        self.reset()

    def update(self):
        self.__rect.top += BACKGROUND_MOVEMENT_SPEED_Y
        if self.__rect.top >= 0:
            self.reset()

    def reset(self):
        self.__rect.bottom = SCREEN_Y

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
