import pygame

from scripts.constantes import *

from scripts.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, image, attributes, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(path.join(getcwd() + f"/assets/images/{image}.png")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (SCREEN_X / 2,  600)

        # Grupos de sprites
        self.__bullet_group = bullet_group

        self.__shield = attributes["shield"]  # Escudo/vida da nave
        self.__shoot_delay = attributes["shoot_delay"]  # Delay do tiro
        self.__lives = attributes["lives"]  # Vidas
        self.__damage = attributes["damage"]  # Dano
        self.__spaceship_velocity = attributes["velocity"]  # Velocidade

        self.__last_shoot = pygame.time.get_ticks()  # Tempo do ultimo tiro
        self.__hidden = False 
        self.__hide_timer = pygame.time.get_ticks()
        self.__key = None
        self.__velocity = None

        # Powerups
        self.__power = 1
        self.__power_time = pygame.time.get_ticks()

    # Movimentação da nave
    def movement(self):
        self.__key = pygame.key.get_pressed()
        self.__velocity = self.__spaceship_velocity

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

    # Colisão com a borda da tela
    def collision(self):
        if self.__rect.left <= 0:
            self.__rect.left = 0
        if self.__rect.right >= SCREEN_X:
            self.__rect.right = SCREEN_X
        
        if self.__rect.top <= 0:
            self.__rect.top = 0
        if self.__rect.bottom >= SCREEN_Y:
            self.__rect.bottom = SCREEN_Y

    # Tiro da nave
    def shoot(self):
        self.__key = pygame.key.get_pressed()
        if not self.__hidden:
            if self.__key[pygame.K_SPACE]:
                if pygame.time.get_ticks() - self.__last_shoot > self.__shoot_delay:
                    self.__last_shoot = pygame.time.get_ticks()
                    bullet_1 = Bullet(self.__rect.centerx + 10, self.__rect.top, "player-bullet", 5, -10)
                    bullet_2 = Bullet(self.__rect.centerx - 10, self.__rect.top, "player-bullet", 5, -10)
                    self.__bullet_group.add(bullet_1, bullet_2)

                    if self.__power >= 2:
                        bullet_3 = Bullet(self.__rect.right, self.__rect.centery, "player-bullet", 5, -10)
                        bullet_4 = Bullet(self.__rect.left, self.__rect.centery, "player-bullet", 5, -10)
                        self.__bullet_group.add(bullet_3, bullet_4)

    # Esconde o player temporariamente depois da sua barra de shiel chegar a 0
    def hide(self):
        self.__hidden = True
        self.__hide_timer = pygame.time.get_ticks()
        self.__rect.center = (SCREEN_X / 2, 600)

        self.__image = pygame.image.load(path.join(getcwd() + "/assets/images/invisible_sprite.png")).convert_alpha()

    # Timeout que deixa o player invisivel
    def hide_timeout(self):
        if self.__hidden and pygame.time.get_ticks() - self.__hide_timer > 1000:
            self.__hidden = False
            self.__rect.center = (SCREEN_X / 2, 600)

            self.__image = pygame.image.load(path.join(getcwd() + "/assets/images/spaceship-1.png")).convert_alpha()
            self.__image = pygame.transform.scale(self.__image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))

    # Ativa o powerup
    def powerup(self):
        self.__power += 1
        self.__power_time = pygame.time.get_ticks()

    # Timeout do powerup
    def powerup_timeout(self):
        # Timeout para os powerups
        if self.__power >= 2 and pygame.time.get_ticks() - self.__power_time > POWERUP_TIME:
            self.__power -= 1
            self.__power_time = pygame.time.get_ticks()

    # Atualiza tudo
    def update(self):
        self.movement()
        self.collision()
        self.powerup_timeout()
        self.shoot()
        self.hide_timeout()
        



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
        return self.__damage
    
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


