import pygame

from scripts.constantes import *

from scripts.bullet import Bullet

# Inimigo normal
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, shield, animation_list, enemy_shot_group, shoot_delay_multiplier):
        pygame.sprite.Sprite.__init__(self)

        self.__enemy_shot_group = enemy_shot_group
        self.__shoot_delay_multiplier = shoot_delay_multiplier

        self.__frame_index = 0 # Frame de animação
        self.__update_time = pygame.time.get_ticks()
        self.__animation_list = animation_list # Lista de animação

        self.__shield = shield # É a "vida" do Enemy
        self.__damage = 30 # Dano

        self.__vel_y = 1 # Velocidade no eixo Y

        self.__last_shoot = pygame.time.get_ticks()

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__image = pygame.transform.scale(self.__image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (x, y) # Posição na tela

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
            bullet = Bullet(self.__rect.centerx, self.__rect.bottom, "enemy-bullet", self.__damage, 7)
            self.__enemy_shot_group.add(bullet)

    def movement(self):
        self.__rect.y += self.__vel_y

    # Verifica se o Enemy saiu da tela, e se saiu exclui o mesmo
    def collision_botton(self):
        if self.__rect.top > SCREEN_Y:
            self.kill()

    def update(self):
        self.update_animation()
        self.shoot()
        self.movement()
        self.collision_botton()



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

    
    # Frame index
    @property
    def frame_index(self):
        return self.__frame_index

    @frame_index.setter
    def frame_index(self, frame_index):
        self.__frame_index = frame_index


    # Update time
    @property
    def update_time(self):
        return self.__update_time

    @update_time.setter
    def update_time(self, update_time):
        self.__update_time = update_time


    # Amimarion list
    @property
    def animation_list(self):
        return self.__animation_list

    @animation_list.setter
    def animation_list(self, animation_list):
        self.__animation_list = animation_list


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


    # Shoot delay
    @property
    def shoot_delay(self):
        return self.__shoot_delay

    @shoot_delay.setter
    def shoot_delay(self, shoot_delay):
        self.__shoot_delay = shoot_delay




# Kamikaze
class Kamikaze(pygame.sprite.Sprite):
    def __init__(self, x, shield, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.__frame_index = 0 # Frame de animação
        self.__update_time = pygame.time.get_ticks()
        self.__animation_list = animation_list # Lista de animação

        self.__shield = shield # É a "vida" do Enemy
        self.__damage = 50 # Dano

        # Imagem
        self.__image = self.__animation_list[self.__frame_index]
        self.__image = pygame.transform.scale(self.__image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (x, -10)

        if self.__rect.x > SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 350)
        if self.__rect.x < SCREEN_X / 2:
            self.__image = pygame.transform.rotate(self.__image, 10)

    def collision_botton(self):
        if self.__rect.top > SCREEN_Y:
            self.kill()


    def update(self):
        self.collision_botton()


        if self.__rect.x > SCREEN_X / 2:
            self.__rect.x -= 0.9
            self.__rect.y += 5
        if self.__rect.x < SCREEN_X / 2:
            self.__rect.x += 1.1
            self.__rect.y += 5
    



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







