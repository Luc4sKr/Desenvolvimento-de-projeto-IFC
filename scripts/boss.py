import pygame

from scripts.constantes import *

class Boss(pygame.sprite.Sprite):

    frame_index = 0  # Frame de animação
    update_time = pygame.time.get_ticks()  # Tempo de atualização

    class Boss_wing(pygame.sprite.Sprite):
        def __init__(self, wing_animation_list, direction):
            pygame.sprite.Sprite.__init__(self)

            self.direction = direction
            self.wing_animatin_list = wing_animation_list

            # Imagem
            self.image = wing_animation_list[Boss.frame_index]
            self.rect = self.image.get_rect()

            pygame.Surface.set_colorkey(self.image, BLACK)

            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, False, False)

            if self.direction == "right":
                self.image = pygame.transform.flip(self.image, True, False)


            self.shield = WING_BOSS_SHIELD


        def get_body_rect(self, body_rect):
            self.body_rect = body_rect

        
        def check_shield(self):
            if self.shield <= 0:
                self.kill()


        def update(self):
            self.check_shield()

            self.image = Boss.update_animation(self.image, self.wing_animatin_list, self.direction)

            if self.direction == "left":
                self.rect.y = self.body_rect.y - 15
                self.rect.right = self.body_rect.left + 15

            if self.direction == "right":
                self.rect.y = self.body_rect.y - 15
                self.rect.left = self.body_rect.right - 15


    def __init__(self, body_animation_list, wing_animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.body_animation_list = body_animation_list
        self.wing_animation_list = wing_animation_list

        self.image = self.body_animation_list[Boss.frame_index]
        self.rect = self.image.get_rect()

        self.rect.center = (SCREEN_X / 2, -30)

        self.left_wing = Boss.Boss_wing(self.wing_animation_list, "left")
        self.right_wing = Boss.Boss_wing(self.wing_animation_list, "right")

    # Update de animação
    @staticmethod
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

    
    def movement(self):
        if self.rect.y <= 50:
            self.rect.y += 1

        self.left_wing.get_body_rect(self.rect)
        self.right_wing.get_body_rect(self.rect)


    def update(self):
        self.movement()

        self.image = self.update_animation(self.image, self.body_animation_list)

        

