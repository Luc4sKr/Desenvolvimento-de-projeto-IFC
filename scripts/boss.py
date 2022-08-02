import pygame

from scripts.constantes import *

class Boss(pygame.sprite.Sprite):

    frame_index = 0  # Frame de animação
    update_time = pygame.time.get_ticks()  # Tempo de atualização

    class Boss_wing(pygame.sprite.Sprite):
        def __init__(self, wing_animation_list, direction):
            pygame.sprite.Sprite.__init__(self)

            self.direction = direction

            # Imagem
            self.image = wing_animation_list[Boss.frame_index]
            self.rect = self.image.get_rect()

            pygame.Surface.set_colorkey(self.image, BLACK)

            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, False, False)

            if self.direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)

        def get_body_rect(self, body_rect):
            self.body_rect = body_rect


        def update(self, *args, **kwargs):
            if self.direction == "left":
                self.rect.y = self.body_rect.y
                self.rect.right = self.body_rect.left + 10

            if self.direction == "right":
                self.rect.y = self.body_rect.y
                self.rect.left = self.body_rect.right - 10


    def __init__(self, body_animation_list, wing_animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.body_animation_list = body_animation_list
        self.wing_animation_list = wing_animation_list

        self.image = self.body_animation_list[self.frame_index]
        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_X / 2, 100)

        self.left_wing = Boss.Boss_wing(self.wing_animation_list, "left")
        self.right_wing = Boss.Boss_wing(self.wing_animation_list, "right")


    def update(self):
        self.rect.y += 1

        self.left_wing.get_body_rect(self.rect)
        self.right_wing.get_body_rect(self.rect)













