from scripts.constants import *
from scripts.bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, shield, damage, animation_list, enemy_shot_group, shoot_delay_multiplier):
        pygame.sprite.Sprite.__init__(self)

        self.__enemy_shot_group = enemy_shot_group              # Grupo de das sprites de tiro
        self.__shoot_delay_multiplier = shoot_delay_multiplier  # Multiplicador de dalay dos tiros
        self.__frame_index = 0                                  # Frame de animação
        self.__update_time = pygame.time.get_ticks()            # Ajuda no update de animação
        self.__animation_list = animation_list                  # Lista de animação
        self.__shield = shield                                  # Shield
        self.__damage = damage                                  # Dano
        self.__last_shoot = pygame.time.get_ticks()             # Ajuda a clcular quando foi disparado o último tiro

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__image = pygame.transform.scale(self.__image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (x, y)  # Posição onde o inimigo vai surgir

    # Update de animação
    def update_animation(self):
        self.__image = self.__animation_list[self.__frame_index]
        if pygame.time.get_ticks() - self.__update_time > ENEMIES_ANIMATION_COOLDOWN:
            self.__update_time = pygame.time.get_ticks()
            self.__frame_index += 1
        if self.__frame_index >= len(self.__animation_list):
            self.__frame_index = 0

    def shoot(self):
        if pygame.time.get_ticks() - self.__last_shoot > ENEMY_SHOOT_DELAY - self.__shoot_delay_multiplier:
            self.__last_shoot = pygame.time.get_ticks()
            pygame.mixer.Sound.play(SHOOT_SOUND_2)
            bullet = Bullet(self.__rect.centerx, self.__rect.bottom, "enemy-bullet", self.__damage, ENEMY_SHOOT_SPEED_Y)
            self.__enemy_shot_group.add(bullet)

    def movement(self):
        self.__rect.y += ENEMY_SPEED_Y

    # Verifica se o Enemy saiu da tela, e se saiu exclui o mesmo
    def collision_botton(self):
        if self.__rect.top > SCREEN_Y:
            self.kill()

    def update(self):
        self.update_animation()
        self.shoot()
        self.movement()
        self.collision_botton()

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

    # --Shield
    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, shield):
        self.__shield = shield

    # --Damage
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, damage):
        if damage <= 0:
            self.__damage = 10
