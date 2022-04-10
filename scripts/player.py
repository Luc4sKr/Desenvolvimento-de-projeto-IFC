import pygame

from scripts.constantes import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(path.join(getcwd() + "/assets/images/spaceship_1.png"))
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE_X, PLAYER_SIZE_Y))
        self.rect = pygame.Rect((SCREEN_X / 2) - (PLAYER_SIZE_X / 2), SCREEN_Y - 100, PLAYER_SIZE_X, PLAYER_SIZE_Y)


    def movement(self):
        self.key = pygame.key.get_pressed()
        self.vel = PLAYER_VEL

        if self.key[pygame.K_w]:
            if self.key[pygame.K_d] or self.key[pygame.K_a]:
                self.vel -= 1
            self.rect.y -= self.vel
        if self.key[pygame.K_s]:
            if self.key[pygame.K_d] or self.key[pygame.K_a]:
                self.vel -= 1
            self.rect.y += self.vel
        if self.key[pygame.K_a]:
            self.rect.x -= self.vel
        if self.key[pygame.K_d]:
            self.rect.x += self.vel

        
    def collision(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_X:
            self.rect.right = SCREEN_X
        
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_Y:
            self.rect.bottom = SCREEN_Y


    def update(self):
        self.movement()
        self.collision()
