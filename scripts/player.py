import pygame

from scripts.constantes import *

from scripts.bullet import Bullet
from scripts.missil import Missil

class Player(pygame.sprite.Sprite):
    def __init__(self, image, shield, shoot_delay, sprite_group, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(path.join(getcwd() + f"/assets/images/{image}")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (SCREEN_X / 2,  600)

        # Grupos de sprites
        self.__sprite_group = sprite_group
        self.__bullet_group = bullet_group

        self.__shield = shield # Escudo/vida da nave
        self.__shoot_delay = shoot_delay # Delay do tiro
        self.__last_shoot = pygame.time.get_ticks() # Tempo do ultimo tiro
        self.__lives = 3 # Vidas
        self.__damage = 1 # Dano
        self.__hidden = False 
        self.__hide_timer = pygame.time.get_ticks()
        self.__velocity = 0
        self.__key = None

        # Powerups
        self.__power = 1
        self.__power_time = pygame.time.get_ticks()

    def movement(self):
        self.__key = pygame.key.get_pressed()
        self.__velocity = PLAYER_VEL

        if self.__key[pygame.K_w] or self.__key[pygame.K_UP]:
            if self.__key[pygame.K_d] or self.__key[pygame.K_a] or self.__key[pygame.K_LEFT] or self.__key[pygame.K_RIGHT]:
                self.__velocity -= 1
            self.__rect.y -= self.__velocity
        if self.__key[pygame.K_s] or self.__key[pygame.K_DOWN]:
            if self.__key[pygame.K_d] or self.__key[pygame.K_a] or self.__key[pygame.K_LEFT] or self.__key[pygame.K_RIGHT]:
                self.__velocity -= 1
            self.__rect.y += self.__velocity
        if self.__key[pygame.K_a] or self.__key[pygame.K_LEFT]:
            self.__rect.x -= self.__velocity
        if self.__key[pygame.K_d] or self.__key[pygame.K_RIGHT]:
            self.__rect.x += self.__velocity

    def collision(self):
        if self.__rect.left <= 0:
            self.__rect.left = 0
        if self.__rect.right >= SCREEN_X:
            self.__rect.right = SCREEN_X
        
        if self.__rect.top <= 0:
            self.__rect.top = 0
        if self.__rect.bottom >= SCREEN_Y:
            self.__rect.bottom = SCREEN_Y

    def shoot(self):
        if pygame.time.get_ticks() - self.__last_shoot > self.__shoot_delay:
            self.__last_shoot = pygame.time.get_ticks()
            bullet_1 = Bullet(self.__rect.centerx + 10, self.__rect.top, 5, -10)
            bullet_2 = Bullet(self.__rect.centerx - 10, self.__rect.top, 5, -10)
            self.__sprite_group.add(bullet_1, bullet_2)
            self.__bullet_group.add(bullet_1, bullet_2)

            if self.__power >= 2:
                bullet_3 = Bullet(self.__rect.right, self.__rect.centery, 5, -10)
                bullet_4 = Bullet(self.__rect.left, self.__rect.centery, 5, -10)
                self.__sprite_group.add(bullet_3, bullet_4)
                self.__bullet_group.add(bullet_3, bullet_4)

    def shoot_missil(self, obj_pos):
        self.__missil = Missil(self.__rect.centerx - 5, self.__rect.top, 10, obj_pos)

    # Esconde o player temporariamente depois da sua barra de shiel chegar a 0
    def hide(self):
        self.__hidden = True
        self.__hide_timer = pygame.time.get_ticks()
        self.__rect.center = (SCREEN_X /2, 600)

        self.__image = pygame.image.load(path.join(getcwd() + "/assets/images/invisible_sprite.png"))


    def powerup(self):
        self.__power += 1
        self.__power_time = pygame.time.get_ticks()

    def update(self):
        self.movement()

        # Shoot
        if self.__key[pygame.K_SPACE]:
            self.shoot()

        self.collision()

        if self.__hidden and pygame.time.get_ticks() - self.__hide_timer > 1000:
            self.__hidden = False
            self.__rect.center = (SCREEN_X /2, 600)

            self.__image = pygame.image.load(path.join(getcwd() + "/assets/images/spaceship_1.png"))
            self.__image = pygame.transform.scale(self.__image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))


        # Timeout para os powerups
        if self.__power >= 2 and pygame.time.get_ticks() - self.__power_time > POWERUP_TIME:
            self.__power -= 1
            self.__power_time = pygame.time.get_ticks()



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
        if shield < 0:
            shield = 0
        self.__shield = shield


    # Lives
    @property
    def lives(self):
        return self.__lives
    
    @lives.setter
    def lives(self, lives):
        if lives < 0:
            lives = 0
        self.__lives = lives


    # Damage
    @property
    def damage(self):
        return self.damage
    
    @damage.setter
    def damage(self, damage):
        if damage < 1:
            damage = 1
        self.__damage = damage


    # Power
    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power


    # Power time
    @property
    def power_time(self):
        return self.__power_time

    @power_time.setter
    def power_time(self, power_time):
        self.__power_time = power_time


    # Velocity
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity


