import pygame

from scripts.constantes import *

from scripts.bullet import Bullet


class Boss(pygame.sprite.Sprite):

    frame_index = 0  # Frame de animação
    update_time = pygame.time.get_ticks()  # Tempo de atualização
    boss_ready = False

    class Boss_wing(pygame.sprite.Sprite):
        def __init__(self, wing_animation_list, direction, shoot_group):
            pygame.sprite.Sprite.__init__(self)

            self.direction = direction
            self.wing_animatin_list = wing_animation_list
            self.shoot_group = shoot_group

            # Imagem
            self.image = wing_animation_list[Boss.frame_index]
            self.rect = self.image.get_rect()
            pygame.Surface.set_colorkey(self.image, BLACK)

            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, False, False)

            if self.direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)

            self.shield = WING_BOSS_SHIELD
            self.damage = 30
            self.last_big_shoot = pygame.time.get_ticks()

        def get_body_rect(self, body_rect):
            self.body_rect = body_rect

        def movement(self):
            if self.direction == "left":
                self.rect.y = self.body_rect.y - 15
                self.rect.right = self.body_rect.left + 15

            if self.direction == "right":
                self.rect.y = self.body_rect.y - 15
                self.rect.left = self.body_rect.right - 15

        def update_animation(self):
            self.image = Boss.update_animation(self.image, self.wing_animatin_list, self.direction)

        def big_shoot(self):
            if self.rect.x < SCREEN_X / 2:
                pos_x_add = -3
            if self.rect.x > SCREEN_X / 2:
                pos_x_add = 3

            if pygame.time.get_ticks() - self.last_big_shoot > BOSS_BIG_SHOOT_DELAY:
                self.last_big_shoot = pygame.time.get_ticks()
                big_bullet = Bullet(self.rect.centerx + pos_x_add, self.rect.bottom - 20, "boss-bullet-1", self.damage,
                                    BOSS_BIG_SHOOT_VELY, scale_x=32, scale_y=32)
                self.shoot_group.add(big_bullet)

        def update(self):
            self.movement()
            self.update_animation()

            if Boss.boss_ready:
                self.big_shoot()

    # Update de animação
    def update_animation(image, animation_list, direction="left"):
        image = animation_list[Boss.frame_index]
        if direction == "right":
            image = pygame.transform.flip(image, True, False)
        if pygame.time.get_ticks() - Boss.update_time > ENEMIES_ANIMATION_COOLDOWN:
            Boss.update_time = pygame.time.get_ticks()
            Boss.frame_index += 1
        if Boss.frame_index >= len(animation_list):
            Boss.frame_index = 0
        return image

    def __init__(self, body_animation_list, wing_animation_list, shoot_group):
        pygame.sprite.Sprite.__init__(self)

        self.body_animation_list = body_animation_list
        self.wing_animation_list = wing_animation_list
        self.shoot_group = shoot_group

        self.image = self.body_animation_list[Boss.frame_index]
        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_X / 2, -110)

        self.left_wing = Boss.Boss_wing(self.wing_animation_list, "left", self.shoot_group)
        self.right_wing = Boss.Boss_wing(self.wing_animation_list, "right", self.shoot_group)

        self.shield = 100

    def movement(self):
        if self.rect.y < 50:
            self.rect.y += 1
        if self.rect.y >= 50:
            Boss.boss_ready = True

        self.left_wing.get_body_rect(self.rect)
        self.right_wing.get_body_rect(self.rect)

    def update(self):
        self.movement()

        self.image = Boss.update_animation(self.image, self.body_animation_list)
