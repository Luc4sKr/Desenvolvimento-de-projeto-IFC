import pygame

from sys import exit
from os import listdir, getcwd, path

from scripts.constantes import *


class Music_framework:
    def __init__(self, screen, clock):
        self.running = True
        self.click = False
        self.clock = clock
        self.screen = screen

        self.list_directory = listdir(path.join(getcwd() + '/assets/music'))
        self.directory = (path.join(getcwd() + '/assets/music'))
        self.music_index = 0

        self.run()
    
    # Roda o framework
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.input_events()

            self.draw_text("Music", 44, WHITE, SCREEN_X / 2, 80)

            self.draw_text(f"{self.list_directory[self.music_index]}", 8, WHITE, SCREEN_X / 2, 200)

            play_button = self.draw_button(SCREEN_X / 2 - 55, 250, 45, 25, "play", font_size=8)
            pause_button = self.draw_button(SCREEN_X / 2 + 5, 250, 45, 25, "pause", font_size=8)
            next_button = self.draw_button(SCREEN_X / 2 + 60, 250, 45, 25, ">", font_size=8)
            back_button = self.draw_button(SCREEN_X / 2 - 110, 250, 45, 25, "<", font_size=8)

            mx, my = pygame.mouse.get_pos()

            if play_button.collidepoint((mx, my)):
                if self.click:
                    pygame.mixer.music.load(path.join(self.directory + f"/{self.list_directory[self.music_index]}"))
                    pygame.mixer.music.play(loops=-1)

            if pause_button.collidepoint((mx, my)):
                if self.click:
                    pass

            if next_button.collidepoint((mx, my)):
                if self.click:
                    if len(self.list_directory)-1 == self.music_index:
                        self.music_index = 0
                    else:
                        self.music_index += 1

            if back_button.collidepoint((mx, my)):
                if self.click:
                    if 0 == self.music_index:
                        self.music_index = len(self.list_directory) - 1
                    else:
                        self.music_index -= 1

            self.click = False

            # Update na tela
            pygame.display.update()
            self.screen.fill(BLACK)
            
    # Eventos de input
    def input_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    # Desenha o texto
    def draw_text(self, text, tam, color, x, y, topleft=False):
        fonte = pygame.font.Font(FONTE, tam)
        text_obj = fonte.render(text, False, color)
        text_rect = text_obj.get_rect()
        if topleft:
            text_rect.topleft = (x, y)
        else:
            text_rect.center = (x, y)
        self.screen.blit(text_obj, text_rect)
    
    # Desenha o botão
    def draw_button(self, left, top, width, height, text, font_size=20, color=(0, 0, 0)):
        button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
        button = pygame.Rect(left, top, width, height)
        pygame.draw.rect(self.screen, WHITE, button_border)
        pygame.draw.rect(self.screen, color, button)
        self.draw_text(text, font_size, WHITE, left + (width / 2), top + (height / 2))
        return button


# -------------------------------------------------------- // -------------------------------------------------------- #


