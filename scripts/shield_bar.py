from scripts.constants import *


class Player_shield_bar(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.__surface = surface
        self.__image = None
        self.__rect = None
        self.__temp = 0

    def draw_shield_bar(self, shield):
        if shield > self.__temp:
            self.__temp = shield

        self.__image = pygame.Surface(((shield * PLAYER_SHIELD_BAR_WIDTH) / self.__temp, PLAYER_SHIELD_BAR_HEIGHT))
        self.__image.fill(GREEN)
        self.__rect = self.__image.get_rect()
        self.__rect.x = PLAYER_SHIELD_BAR_POS_X
        self.__rect.y = PLAYER_SHIELD_BAR_POS_Y
        self.outline_rect()
        self.__surface.blit(self.__image, self.__rect)

    def outline_rect(self):
        rect = pygame.Rect(PLAYER_SHIELD_BAR_POS_X - 2, PLAYER_SHIELD_BAR_POS_X - 2, PLAYER_SHIELD_BAR_WIDTH + 4, PLAYER_SHIELD_BAR_HEIGHT + 4)
        pygame.draw.rect(self.__surface, WHITE, rect)


class Enemy_shield_bar(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.__surface = surface
        self.__image = None
        self.__rect = None
        self.__temp = 0

    def draw_shield_bar(self, shield, enemy_rect, additional_x_position=0, additional_y_position=0, margin=0):
        
        if shield > self.__temp:
            self.__temp = shield

        self.__image = pygame.Surface(((shield * (enemy_rect.width + margin)) / self.__temp, ENEMY_SHIELD_BAR_HEIGHT))
        self.__image.fill(GREEN)
        self.__rect = self.__image.get_rect()
        self.__rect.x = enemy_rect.x + additional_x_position
        self.__rect.y = enemy_rect.y + additional_y_position
        self.__surface.blit(self.__image, self.__rect)
