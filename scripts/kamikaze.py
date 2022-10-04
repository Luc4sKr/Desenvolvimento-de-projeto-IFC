import pygame

from scripts.constants import Constants as Const


class Kamikaze(pygame.sprite.Sprite):
    def __init__(self, x, shield, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__frame_index = 0                        # Frame de animação
        self.__update_time = pygame.time.get_ticks()  # Ajuda no update de animação
        self.__animation_list = animation_list        # Lista de animação
        self.__shield = shield                        # Shield
        self.__damage = Const.KAMIKAZE_DAMAGE         # Dano

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__image = pygame.transform.scale(self.__image, (Const.ENEMY_SIZE_X, Const.ENEMY_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (x, -20)  # Posição onde o inimigo vai surgir

        # Define a rotação do kamikaze dependendo de qual lado da tela ele está
        if self.__rect.x > Const.SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 340)
        if self.__rect.x < Const.SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 20)

        self.__image.convert_alpha()

    # Update de animação
    def update_animation(self):
        self.__image = self.__animation_list[self.__frame_index]
        self.update_image()

        if pygame.time.get_ticks() - self.__update_time > Const.KAMIKAZE_ANIMATION_COOLDOWN:
            self.__update_time = pygame.time.get_ticks()
            self.__frame_index += 1
        if self.__frame_index >= len(self.__animation_list):
            self.__frame_index = 0

    def movement(self):
        self.__rect.y += 4.8
        if self.__rect.x > Const.SCREEN_X / 2:
            self.__rect.x -= 0.9
        if self.__rect.x < Const.SCREEN_X / 2:
            self.__rect.x += 1.1

    def collision_botton(self):
        if self.__rect.top > Const.SCREEN_Y:
            self.kill()

    def update_image(self):
        # Define a rotação do kamikaze dependendo de qual lado da tela ele está
        if self.__rect.x > Const.SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 340)
        if self.__rect.x < Const.SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 20)
        self.__image.convert_alpha()

    def update(self):
        self.collision_botton()
        self.update_animation()
        self.movement()

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
