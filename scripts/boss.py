import pygame

from scripts.constants import Constants as Const
from scripts.bullet import Bullet


class Boss(pygame.sprite.Sprite):
    frame_index = 0                         # Frame de animação
    update_time = pygame.time.get_ticks()   # Tempo de atualização
    boss_ready = False                      #

    class Boss_wing(pygame.sprite.Sprite):
        def __init__(self, wing_animation_list, direction, shoot_group):
            pygame.sprite.Sprite.__init__(self)

            self.direction = direction
            self.wing_animatin_list = wing_animation_list
            self.shoot_group = shoot_group

            # Imagem
            self.image = wing_animation_list[Boss.frame_index]
            self.rect = self.image.get_rect()
            pygame.Surface.set_colorkey(self.image, Const.BLACK)

            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, False, False)

            if self.direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)

            self.shield = Const.WING_BOSS_SHIELD
            self.damage = Const.BOSS_SMALL_SHOOT_DAMAGE

            self.last_big_shoot = pygame.time.get_ticks()
            self.last_small_shoot = pygame.time.get_ticks()
            self.small_shoot_temp = pygame.time.get_ticks()
            self.small_shoot_event = False
            self.small_shoot_event_index = 0

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
            self.image = Boss.update_animation(self.wing_animatin_list, self.direction)

        def big_shoot(self):
            if self.rect.x < Const.SCREEN_X / 2:
                pos_x_add = -3
            if self.rect.x > Const.SCREEN_X / 2:
                pos_x_add = 3

            if pygame.time.get_ticks() - self.last_big_shoot > Const.BOSS_BIG_SHOOT_DELAY:
                self.last_big_shoot = pygame.time.get_ticks()
                big_shoot = Bullet(self.rect.centerx + pos_x_add, self.rect.bottom - 20, Const.BULLET_BOSS_BLUE_IMAGE,
                                   Const.BOSS_BIG_SHOOT_DAMAGE, Const.SHOOT_SOUND_2, Const.BOSS_BIG_SHOOT_SPEED_Y,
                                   scale_x=28, scale_y=28)
                self.shoot_group.add(big_shoot)

        def small_shoot(self):
            if self.rect.x < Const.SCREEN_X / 2:
                pos_x1_add = -38
                pos_x2_add = 69
            if self.rect.x > Const.SCREEN_X / 2:
                pos_x1_add = 38
                pos_x2_add = -69

            if pygame.time.get_ticks() - self.last_small_shoot > Const.BOSS_SMALL_SHOOT_DELAY or self.small_shoot_event:
                self.last_small_shoot = pygame.time.get_ticks()
                self.small_shoot_event = True
                if pygame.time.get_ticks() - self.small_shoot_temp > Const.BOSS_SMALL_SHOOT_TEMP_DELAY:
                    self.small_shoot_temp = pygame.time.get_ticks()
                    small_shoot_1 = Bullet(self.rect.centerx + pos_x1_add, self.rect.bottom - 20, Const.BULLET_BOSS_BLUE_IMAGE,
                                           Const.BOSS_SMALL_SHOOT_DAMAGE, Const.SHOOT_SOUND_2, Const.BOSS_SMALL_SHOOT_SPEED_Y,
                                           scale_x=16, scale_y=16)
                    small_shoot_2 = Bullet(self.rect.centerx + pos_x2_add, self.rect.bottom - 30, Const.BULLET_BOSS_BLUE_IMAGE,
                                           Const.BOSS_SMALL_SHOOT_DAMAGE, Const.SHOOT_SOUND_2, Const.BOSS_SMALL_SHOOT_SPEED_Y,
                                           scale_x=16, scale_y=16)

                    self.shoot_group.add(small_shoot_1, small_shoot_2)

                    self.small_shoot_event_index += 1

                    if self.small_shoot_event_index >= 3:
                        self.small_shoot_event_index = 0
                        self.small_shoot_event = False
                        self.last_small_shoot = pygame.time.get_ticks()

        def update(self):
            self.movement()
            self.update_animation()

            if Boss.boss_ready:
                self.big_shoot()
                self.small_shoot()

    # Update de animação
    @staticmethod
    def update_animation(animation_list, direction="left"):
        image = animation_list[Boss.frame_index]
        if direction == "right":
            image = pygame.transform.flip(image, True, False)
        if pygame.time.get_ticks() - Boss.update_time > Const.ENEMIES_ANIMATION_COOLDOWN:
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

        self.rect.center = (Const.SCREEN_X / 2, -110)

        self.left_wing = Boss.Boss_wing(self.wing_animation_list, "left", self.shoot_group)
        self.right_wing = Boss.Boss_wing(self.wing_animation_list, "right", self.shoot_group)

        self.shield = Const.BODY_BOSS_SHIELD

    def movement(self):
        if self.rect.y < 50:
            self.rect.y += 1
        if self.rect.y >= 50:
            Boss.boss_ready = True

        self.left_wing.get_body_rect(self.rect)
        self.right_wing.get_body_rect(self.rect)

    def update(self):
        self.movement()

        self.image = Boss.update_animation(self.body_animation_list)
