import pygame

from scripts.constantes import *
from scripts.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, image, shield, shoot_delay, sprite_group, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(getcwd() + f"/assets/images/{image}")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_X / 2,  600)

        self.sprite_group = sprite_group
        self.bullet_group = bullet_group

        self.shield = shield # Escudo/vida da nave
        self.shoot_delay = shoot_delay # Delay do tiro
        self.last_shoot = pygame.time.get_ticks() # Tempo do ultimo tiro
        self.lives = 3 # Vidas
        self.damage = 1

        # Quando o player/nave é "morto", ele fica um tempo "escondido"
        self.hidden = False 
        self.hide_timer = pygame.time.get_ticks()

        # Powerups
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def movement_and_shoot(self):
        self.key = pygame.key.get_pressed()
        self.vel = PLAYER_VEL

        if self.key[pygame.K_w] or self.key[pygame.K_UP]:
            if self.key[pygame.K_d] or self.key[pygame.K_a] or self.key[pygame.K_LEFT] or self.key[pygame.K_RIGHT]:
                self.vel -= 1
            self.rect.y -= self.vel
        if self.key[pygame.K_s] or self.key[pygame.K_DOWN]:
            if self.key[pygame.K_d] or self.key[pygame.K_a] or self.key[pygame.K_LEFT] or self.key[pygame.K_RIGHT]:
                self.vel -= 1
            self.rect.y += self.vel
        if self.key[pygame.K_a] or self.key[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if self.key[pygame.K_d] or self.key[pygame.K_RIGHT]:
            self.rect.x += self.vel

        # Shoot
        if self.key[pygame.K_SPACE]:
            self.shoot()

    def collision(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_X:
            self.rect.right = SCREEN_X
        
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_Y:
            self.rect.bottom = SCREEN_Y

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            bullet_1 = Bullet(self.rect.centerx + 10, self.rect.top, 5, -10)
            bullet_2 = Bullet(self.rect.centerx - 10, self.rect.top, 5, -10)
            self.sprite_group.add(bullet_1, bullet_2)
            self.bullet_group.add(bullet_1, bullet_2)

            if self.power >= 2:
                bullet_3 = Bullet(self.rect.right, self.rect.centery, 5, -10)
                bullet_4 = Bullet(self.rect.left, self.rect.centery, 5, -10)
                self.sprite_group.add(bullet_3, bullet_4)
                self.bullet_group.add(bullet_3, bullet_4)

    # Esconde o player temporariamente depois da sua barra de shiel chegar a 0
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_X /2, 600)

        self.image = pygame.image.load(path.join(getcwd() + "/assets/images/invisible_sprite.png"))


    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        self.movement_and_shoot()
        self.collision()

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.center = (SCREEN_X /2, 600)

            self.image = pygame.image.load(path.join(getcwd() + "/assets/images/spaceship_1.png"))
            self.image = pygame.transform.scale(self.image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))


        # Timeout para os powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()


