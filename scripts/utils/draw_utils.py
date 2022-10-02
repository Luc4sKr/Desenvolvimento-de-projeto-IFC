import pygame

from os import path

from scripts.constants import Constants as Const
from scripts.data.data_utils import Data_util
from scripts.utils.images import Images


class Draw_util:

    @staticmethod
    def draw_text(screen, text, tam, color, x, y, topleft=False):
        fonte = pygame.font.Font(Const.FONT_STYLE, tam)
        text_obj = fonte.render(text, False, color)
        text_rect = text_obj.get_rect()
        if topleft:
            text_rect.topleft = (x, y)
        else:
            text_rect.center = (x, y)
        screen.blit(text_obj, text_rect)

    @staticmethod
    def draw_button(screen, left, top, width, height, text, font_size=20, button_color=(0, 0, 0), font_color=Const.WHITE, border_color=Const.WHITE):
        button_border = pygame.Rect(int(left - 2), int(top - 2), int(width + 4), int(height + 4))
        button = pygame.Rect(int(left), int(top), int(width), int(height))
        pygame.draw.rect(screen, border_color, button_border)
        pygame.draw.rect(screen, button_color, button)
        Draw_util.draw_text(screen, text, font_size, font_color, left + (width / 2), top + (height / 2))
        return button

    @staticmethod
    def voltar_button(screen):
        return Draw_util.draw_button(screen, 30, 670, 100, 30, "Voltar", font_size=14)

    @staticmethod
    def draw_loja_button(screen, sprite, left, top, width, height, nome, price, lives, shield, damage, velocity, shoot_dedaly):
        button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
        button = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, Const.WHITE, button_border)
        pygame.draw.rect(screen, Const.BLACK, button)

        if Data_util.get_player_spaceship() == sprite[:11]:
            pygame.draw.rect(screen, Const.GREEN, button_border)
            pygame.draw.rect(screen, Const.BLACK, button)
            Draw_util.draw_text(screen, "Equipado", 16, Const.GREEN, left + 110, top + 100, topleft=True)
        else:
            if sprite[:11] in Data_util.get_purchased_ships():
                Draw_util.draw_text(screen, "Disponível", 16, Const.WHITE, left + 110, top + 100, topleft=True)
            else:
                Draw_util.draw_text(screen, f"{price} Coins", 16, Const.WHITE, left + 110, top + 100, topleft=True)

        image = pygame.image.load(path.join(f"{Images.image_dir}/sprites/spaceships/{sprite}"))
        image = pygame.transform.scale(image, (75, 75))
        image_rect = image.get_rect()
        image_rect.center = (left + 60, top + (height / 2))
        screen.blit(image, image_rect)

        Draw_util.draw_text(screen, nome, 16, Const.YELLOW, left + 130, top + 10, topleft=True)  # Nome
        Draw_util.draw_text(screen, f"Vidas: {lives}", 10, Const.WHITE, left + 130, top + 35, topleft=True)  # Vidas
        Draw_util.draw_text(screen, f"Escudo: {shield}", 10, Const.WHITE, left + 130, top + 55, topleft=True)  # Escudo
        Draw_util.draw_text(screen, f"Dano: {damage}", 10, Const.WHITE, left + 270, top + 35, topleft=True)  # Dano
        Draw_util.draw_text(screen, f"Velocidade: {velocity}", 10, Const.WHITE, left + 270, top + 55, topleft=True)  # Velocidade
        Draw_util.draw_text(screen, f"Shoot delay: {shoot_dedaly}", 10, Const.WHITE, left + 270, top + 75, topleft=True)  # Shoot delay
        return button

    @staticmethod
    def cursor(screen, button, color=Const.WHITE):
        Draw_util.draw_text(screen, "->", 16, color, button.left - 30, button.centery)
        Draw_util.draw_text(screen, "<-", 16, color, button.right + 30, button.centery)
