import pygame

from scripts.constantes import *

class ShieldBar(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.surface = surface



    def draw_shield_bar(self, shield, x, y):
        self.image = pygame.Surface(((shield / 100) * ENEMY_BAR_WIDTH, ENEMY_BAR_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.surface.blit(self.image, self.rect)



        '''if shield < 0:
            shield = 0
        fill = (shield / 100) * ENEMY_BAR_WIDTH
        fill_rect = pygame.Rect(x, y, fill, ENEMY_BAR_HEIGHT)
        pygame.draw.rect(self.surface, GREEN, fill_rect)'''

