import pygame

from random import choice
from os import path, getcwd

from scripts.constantes import *


class Powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        powerup_images = {}
        powerup_images["shield"] = pygame.image.load(path.join(getcwd() + "/assets/images/powerups/shield2.png"))
        #powerup_images["gun"] = pygame.image.load(path.join(getcwd() + "/assets/images/powerups/shield.png"))

         # Imagem
        self.type = choice(["shield"]) # Escolhe aleatoriamente o tipo
        self.image = powerup_images[self.type]
        if self.type == "shield":
            self.image = pygame.transform.scale(self.image, (30, 38))
        else:
            self.image = pygame.transform.scale(self.image, (40, 40))
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.center = center

        # Velocidade y
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > SCREEN_Y:
            self.kill()
        