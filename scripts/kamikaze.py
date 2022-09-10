from scripts.constants import *


class Kamikaze(pygame.sprite.Sprite):
    def __init__(self, x, shield, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__frame_index = 0  # Frame de animação
        self.__update_time = pygame.time.get_ticks()
        self.__animation_list = animation_list  # Lista de animação

        self.__shield = shield  # É a "vida" do Enemy
        self.__damage = KAMIKAZE_DAMAGE  # Dano

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__image = pygame.transform.scale(self.__image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (x, -20)

        if self.__rect.x > SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 340)
        if self.__rect.x < SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 20)

        self.__image.convert_alpha()

    def collision_botton(self):
        if self.__rect.top > SCREEN_Y:
            self.kill()

    def update(self):
        self.collision_botton()

        self.__rect.y += 4.8
        if self.__rect.x > SCREEN_X / 2:
            self.__rect.x -= 0.9
        if self.__rect.x < SCREEN_X / 2:
            self.__rect.x += 1.1

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

    # Shield
    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, shield):
        self.__shield = shield

    # Damage
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if damage <= 0:
            self.__damage = 10