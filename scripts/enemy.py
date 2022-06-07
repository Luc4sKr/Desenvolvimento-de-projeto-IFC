import pygame

from random import randint

from scripts.constantes import *
from scripts.explosion import Explosion

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, shield, animation_list, bullet_group, sprite_group, explosion_sprite_sheet, score, shield_bar):
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0 # Frame de animação
        self.action = 0 # Ação do Enemy
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list # Lista de animação

        self.shield = shield # É a "vida" do Enemy

        # ----------------------------------------------------
        self.bullet_group = bullet_group
        self.sprite_group = sprite_group
        self.explosion_sprite_sheet = explosion_sprite_sheet
        self.score = score
        self.shield_bar = shield_bar
        # ----------------------------------------------------

        self.vel_y = 1 # Velocidade no eixo Y

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

    # Colisão com o tiro do player
    def shoot_collision(self):
        self.collision = pygame.sprite.spritecollide(self, self.bullet_group, True, pygame.sprite.collide_mask)
        if self.collision:
            self.shield -= 1
            if self.shield <= 0:
                self.score.add_score()
                self.kill()
                explosion = Explosion(self.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(explosion)

    def update(self):
        self.update_animation()
        self.shoot_collision()

        # Verifica se o Enemy saiu da tela, e se saiu exclui o mesmo
        if self.rect.top > SCREEN_Y:
            self.kill()

        # Faz o Enemy "andar" pra frente
        self.rect.y += self.vel_y

        self.shield_bar.draw_shield_bar(self.shield, self.rect.x, self.rect.y)


