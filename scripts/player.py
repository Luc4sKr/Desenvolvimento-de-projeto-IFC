import pygame

from scripts.constants import Constants as Const
from scripts.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, spaceship, attributes, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.__image = pygame.image.load(Const.PLAYER_IMAGE).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (Const.PLAYER_SIZE_X, Const.PLAYER_SIZE_Y))
        self.__rect = self.__image.get_rect()

        self.__rect.center = (Const.SCREEN_X / 2,  600)
        self.spaceship = spaceship

        # Grupos de sprites
        self.__bullet_group = bullet_group

        # Atributos do Player
        self.__shield = attributes["shield"]                # Escudo/vida da nave
        self.__shoot_delay = attributes["shoot_delay"]      # Delay do tiro
        self.__lives = attributes["lives"]                  # Vidas
        self.__damage = attributes["damage"]                # Dano
        self.__spaceship_velocity = attributes["velocity"]  # Velocidade

        self.__last_shoot = pygame.time.get_ticks()         # Tempo do ultimo tiro
        self.__hidden = False                               # Serve para deixar o Player invisível
        self.__hide_timer = pygame.time.get_ticks()         # Ajuda a controlar o tempo que o Player fica invisível
        self.__key = None                                   # Botão pressionado
        self.__velocity = None                              # Velocidade que pode sofrer modificações
        self.__shoot_power = False                          # Ativa o powerup de tiro
        self.__shoot_power_time = pygame.time.get_ticks()   # Ajuda a controlar o tempo que o powerup fica ativado

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
        if self.__rect.right >= Const.SCREEN_X:
            self.__rect.right = Const.SCREEN_X
        
        if self.__rect.top <= 0:
            self.__rect.top = 0
        if self.__rect.bottom >= Const.SCREEN_Y:
            self.__rect.bottom = Const.SCREEN_Y

    # Tiro da nave
    def shoot(self):
        self.__key = pygame.key.get_pressed()
        if not self.__hidden:
            if self.__key[pygame.K_SPACE]:
                if pygame.time.get_ticks() - self.__last_shoot > self.__shoot_delay:
                    self.__last_shoot = pygame.time.get_ticks()
                    bullet_1 = Bullet(self.__rect.centerx + 10, self.__rect.top, Const.BULLET_PLAYER_IMAGE, self.__damage, Const.SHOOT_SOUND_1, Const.PLAYER_SHOOT_SPEED)
                    bullet_2 = Bullet(self.__rect.centerx - 10, self.__rect.top, Const.BULLET_PLAYER_IMAGE, self.__damage, Const.SHOOT_SOUND_1, Const.PLAYER_SHOOT_SPEED)
                    self.__bullet_group.add(bullet_1, bullet_2)

                    if self.__shoot_power:
                        bullet_3 = Bullet(self.__rect.right, self.__rect.centery, Const.BULLET_PLAYER_IMAGE, self.__damage, Const.SHOOT_SOUND_1, Const.PLAYER_SHOOT_SPEED)
                        bullet_4 = Bullet(self.__rect.left, self.__rect.centery, Const.BULLET_PLAYER_IMAGE, self.__damage, Const.SHOOT_SOUND_1, Const.PLAYER_SHOOT_SPEED)
                        self.__bullet_group.add(bullet_3, bullet_4)

    # Esconde o player temporariamente depois da sua barra de shiel chegar a 0
    def hide(self):
        self.__hidden = True
        self.__hide_timer = pygame.time.get_ticks()
        self.__rect.center = (Const.SCREEN_X / 2, 600)

        self.__image = pygame.Surface((0, 0))

    # Timeout que deixa o player invisivel
    def hide_timeout(self):
        if self.__hidden and pygame.time.get_ticks() - self.__hide_timer > 1000:
            self.__hidden = False
            self.__rect.center = (Const.SCREEN_X / 2, 600)

            self.__image = pygame.image.load(Const.PLAYER_IMAGE).convert_alpha()
            self.__image = pygame.transform.scale(self.__image, (Const.PLAYER_SIZE_X, Const.PLAYER_SIZE_Y))

    # Ativa o powerup
    def powerup(self):
        self.__shoot_power = True
        self.__shoot_power_time = pygame.time.get_ticks()

    # Timeout do powerup
    def powerup_timeout(self):
        # Timeout para os powerups
        if pygame.time.get_ticks() - self.__shoot_power_time > Const.POWERUP_TIME:
            self.__shoot_power_time = pygame.time.get_ticks()
            self.__shoot_power = False

    # Atualiza tudo
    def update(self):
        self.movement()
        self.collision()
        self.powerup_timeout()
        self.shoot()
        self.hide_timeout()

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
        if shield < 0:
            shield = 0
        self.__shield = shield

    # --Lives
    @property
    def lives(self):
        return self.__lives
    
    @lives.setter
    def lives(self, lives):
        if lives < 0:
            lives = 0
        self.__lives = lives

    # --Damage
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, damage):
        if damage < 1:
            damage = 1
        self.__damage = damage

    # --Power
    @property
    def power(self):
        return self.__shoot_power

    @power.setter
    def power(self, power):
        self.__shoot_power = power

    # --Velocity
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity
