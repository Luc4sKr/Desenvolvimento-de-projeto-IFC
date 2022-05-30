import pygame

from scripts.constantes import ANIMATION_COOLDOWN

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, animation_list):
        pygame.sprite.Sprite.__init__(self)

        self.center = center
        self.animation_list = animation_list

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animation_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update_animation(self):
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index == len(self.animation_list):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.animation_list[self.frame_index]
                self.rect.center = center

    def update(self):
        self.update_animation()

