from scripts.constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_image, damage, shoot_sound, vely, scale_x=8, scale_y=12):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(bullet_image).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (scale_x, scale_y))
        self.__rect = self.__image.get_rect()

        self.__rect.bottom = y
        self.__rect.centerx = x
        self.__speed_y = vely
        self.__damage = damage
        self.__shoot_sound = shoot_sound

        pygame.mixer.Sound.play(shoot_sound)

    def update(self):
        self.__rect.y += self.__speed_y
        if self.__rect.bottom < 0 or self.__rect.top > SCREEN_Y:
            self.kill()

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

    # --Damage
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    # --Speed
    @property
    def speed_y(self):
        return self.__speed_y

    @speed_y.setter
    def speed_y(self, speed_y):
        self.__speed_y = speed_y
