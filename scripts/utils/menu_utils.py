import pygame
from sys import exit

from scripts.constants import Constants as Const
from scripts.utils.draw_utils import Draw_util


class Menu_util:

    @staticmethod
    def cursor_event(button_list, cursor_point, button):
        pygame.mixer.Sound.play(Const.SELECT_SOUND)
        if button == pygame.K_UP:
            if button_list.index(cursor_point) >= 0:
                return button_list[button_list.index(cursor_point) - 1]
        if button == pygame.K_DOWN:
            if button_list.index(cursor_point) < len(button_list) - 1:
                return button_list[button_list.index(cursor_point) + 1]

    @staticmethod
    def back_button(click, link):
        click = False   # Deixa o click falso para evitar bugs
        link = False    # O link é o laço de repetição que será interrompido
        return click, link

    @staticmethod
    def quit_game():
        pygame.quit()
        exit()
