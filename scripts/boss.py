import pygame

from scripts.constantes import *

class Boss(pygame.sprite.Sprite):

    frame_index = 0
    update_time = pygame.time.get_ticks()

    def __init__(self, body_animation_list, wing_animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.frame_index = 0 # Frame de animação
        self.update_time = pygame.time.get_ticks() # Tempo de atualização

        self.sprite_group = pygame.sprite.Group()

        self.body_animation_list = body_animation_list
        self.wing_animation_list = wing_animation_list
        

        class Boss_body(pygame.sprite.Sprite):
            def __init__(self, body_animation_list):
                pygame.sprite.Sprite.__init__(self)

                # Imagem
                self.image = body_animation_list[Boss.frame_index]
                self.rect = self.image.get_rect()

                self.rect.center = (SCREEN_X / 2, SCREEN_Y / 2)

        
        class Boss_wing(pygame.sprite.Sprite):
            def __init__(self, wing_animation_list, direction, body_rect):
                pygame.sprite.Sprite.__init__(self)

                # Imagem
                self.image = wing_animation_list[Boss.frame_index]
                self.rect = self.image.get_rect()

                pygame.Surface.set_colorkey(self.image, BLACK)

                if direction == "left":
                    self.image = pygame.transform.rotate(self.image, 0)
                    self.rect.right = body_rect.left
                    self.rect.y = body_rect.centerx

                if direction == "right":
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rect.left = body_rect.right
                    self.rect.y = body_rect.centerx



        body = Boss_body(self.body_animation_list)
        left_wing = Boss_wing(self.wing_animation_list, "left", body.rect)
        right_wing = Boss_wing(self.wing_animation_list, "right", body.rect)

        self.sprite_group.add(body)
        self.sprite_group.add(left_wing)
        self.sprite_group.add(right_wing)










