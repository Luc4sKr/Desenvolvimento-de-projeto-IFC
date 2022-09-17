from random import choice
from scripts.constants import *


class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        powerup_images = {
            "shield": pygame.image.load(SHIELD_POWERUP_IMAGE).convert_alpha(),
            "gun": pygame.image.load(GUN_POWERUP_IMAGE).convert_alpha()
        }

        # Imagem
        self.__type = choice(["shield", "gun"])
        self.__image = powerup_images[self.__type]
        self.__image = pygame.transform.scale(self.__image, (POWERUP_WIDTH, POWERUP_HEIGHT))
        self.__rect = self.__image.get_rect()
        self.__rect.center = center

    def update(self):
        self.__rect.y += POWERUP_SPEED_Y
        if self.__rect.top > SCREEN_Y:
            self.kill()

    # --- GETTERS AND SETTERS --- #

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

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
