import pygame

from scripts.constantes import *

from scripts.bullet import Bullet

# Inimigo normal
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, shield, animation_list, sprite_group, enemy_shot_group, explosion_sprite_sheet, score):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0 # Frame de animação
        self.update_time = pygame.time.get_ticks()
        self.animation_list = animation_list # Lista de animação

        self.shield = shield # É a "vida" do Enemy

        self.sprite_group = sprite_group
        self.explosion_sprite_sheet = explosion_sprite_sheet
        self.score = score
        self.enemy_shot_group = enemy_shot_group

        self.damage = 30

        self.vel_y = 1 # Velocidade no eixo Y

        self.shoot_delay = 1700
        self.last_shoot = pygame.time.get_ticks()

        # Imagem
        self.image = self.animation_list[self.frame_index]
        self.image = pygame.transform.scale(self.image, (ENEMY_SIZE_X, ENEMY_SIZE_Y))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y) # Posição na tela

    # Update de animação
    def update_animation(self):
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            now = pygame.time.get_ticks()
            self.last_shoot = pygame.time.get_ticks()
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.damage, 7)
            self.sprite_group.add(bullet)
            self.enemy_shot_group.add(bullet)


    def update(self):
        self.update_animation()
        self.shoot()

        # Verifica se o Enemy saiu da tela, e se saiu exclui o mesmo
        if self.rect.top > SCREEN_Y:
            self.kill()

        # Faz o Enemy se mover
        self.rect.y += self.vel_y


# Kamikaze
class Kamikaze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)




