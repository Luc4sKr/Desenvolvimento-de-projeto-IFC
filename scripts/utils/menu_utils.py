import pygame
from sys import exit

from scripts.constants import Constants as Const


class Menu_util:

    @staticmethod
    def back_button(click, link):
        click = False   # Deixa o click falso para evitar bugs
        link = False    # O link é o laço de repetição que será interrompido
        return click, link

    @staticmethod
    def quit_game():
        pygame.quit()
        exit()
