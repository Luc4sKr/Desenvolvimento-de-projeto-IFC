import pygame

from scripts.constantes import *
from scripts.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_group, bullet_group):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(getcwd() + "/assets/images/spaceship_1.png"))
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.rect = pygame.Rect((SCREEN_X / 2) - (PLAYER_SIZE_X / 2), SCREEN_Y - 100, PLAYER_SIZE_X, PLAYER_SIZE_Y)
        self.shoot_delay = 250
        self.last_shoot = pygame.time.get_ticks()

        self.sprite_group = sprite_group
        self.bullet_group = bullet_group

    def movement(self):
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
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.sprite_group.add(bullet)
            self.bullet_group.add(bullet)

    def update(self):
        self.movement()
        self.collision()

