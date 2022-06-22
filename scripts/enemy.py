import pygame

from random import randint

from scripts.constantes import *
from scripts.explosion import Explosion
from scripts.powerup import Powerup
from scripts.bullet import Bullet
from scripts.enemy_shield_bar import Shield_bar

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, shield, animation_list, sprite_group, enemy_shot_group, explosion_sprite_sheet, score):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0 # Frame de animação
        self.action = 0 # Ação do Enemy
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list # Lista de animação

        self.shield = shield # É a "vida" do Enemy

        self.sprite_group = sprite_group
        self.explosion_sprite_sheet = explosion_sprite_sheet
        self.score = score
        self.enemy_shot_group = enemy_shot_group

        self.vel_y = 1 # Velocidade no eixo Y

        self.shoot_delay = 1500
        self.last_shoot = pygame.time.get_ticks()

        # Imagem
        self.image = self.animation_list[self.action][self.frame_index]
        self.image = pygame.transform.scale(self.image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y) # Posição na tela

    # Update de animação
    def update_animation(self):
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 5, 7)
            self.sprite_group.add(bullet)
            self.enemy_shot_group.add(bullet)


    def update(self):
        self.update_animation()
        #self.shoot_collision()
        self.shoot()

        # Verifica se o Enemy saiu da tela, e se saiu exclui o mesmo
        if self.rect.top > SCREEN_Y:
            self.kill()

        # Faz o Enemy se mover
        self.rect.y += self.vel_y

        #self.shield_bar.draw_shield_bar()




