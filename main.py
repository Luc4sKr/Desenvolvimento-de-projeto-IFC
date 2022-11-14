import pygame

from os import path, getcwd
from random import randint
from sys import exit
from math import sin

from scripts.constants import Constants as Const
from scripts.asteroid import Asteroid
from scripts.background import Background
from scripts.enemy import Enemy
from scripts.kamikaze import Kamikaze
from scripts.boss import Boss
from scripts.explosion import Explosion
from scripts.player import Player
from scripts.score import Score
from scripts.coin import Coin
from scripts.powerup import Powerup
from scripts.shield_bar import Enemy_shield_bar, Player_shield_bar

from scripts.data.data_utils import Data_util
from scripts.utils.game_utils import Game_utils
from scripts.utils.loja_utils import Loja_util
from scripts.utils.menu_utils import Menu_util
from scripts.utils.draw_utils import Draw_util
from scripts.utils.images import Images
from scripts.utils.sprite_sheet import Sprite_sheet as Sprite

from scripts.utils.music_player import Music_player


class Menu:
    def __init__(self):
        super().__init__()
        self.enter = False  # Click no enter
        self.mouse_click = False  # Click do mouse

        self.cursor_point = None

        # Controle dos laços de repetição
        self.show_menu = False
        self.show_difficulty_menu = False
        self.show_loja_menu = False
        self.show_opcoes_menu = False
        self.show_creditos_menu = False

        self.show_options_sons_menu = False
        self.show_options_acessibilidade_menu = False

        # Background
        self.menu_background_sprite = pygame.sprite.Sprite()
        self.menu_background_sprite.image = pygame.image.load(Images.manu_image_background)
        self.menu_background_sprite.image = pygame.transform.scale(self.menu_background_sprite.image,
                                                                   (Const.SCREEN_X, Const.SCREEN_Y))
        self.menu_background_sprite.rect = self.menu_background_sprite.image.get_rect()
        self.menu_background = pygame.sprite.GroupSingle(self.menu_background_sprite)

    def menu(self):
        button_list = []
        self.show_menu = True

        while self.show_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.enter = True

                    if event.key == pygame.K_F1:
                        music_framework = Music_player(screen, clock)
                        music_framework.run()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            # Background
            self.menu_background_sprite.image = pygame.image.load(Images.manu_image_background)
            self.menu_background_sprite.image = pygame.transform.scale(self.menu_background_sprite.image,
                                                                       (Const.SCREEN_X, Const.SCREEN_Y))
            self.menu_background.draw(screen)

            # Título do jogo
            Draw_util.draw_text(screen, "SPACE", Const.LOGO_FONT, Const.YELLOW, Const.SCREEN_X / 2, 100)
            Draw_util.draw_text(screen, "BATTLE", Const.LOGO_FONT, Const.YELLOW, Const.SCREEN_X / 2, 160)

            # Botões do menu
            jogar_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 250, Const.SCREEN_X / 2 - 50, 50,
                                                 "JOGAR")
            loja_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 310, Const.SCREEN_X / 2 - 50, 50,
                                                "LOJA")
            opcoes_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 370, Const.SCREEN_X / 2 - 50, 50,
                                                  "OPÇÕES")
            creditos_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 430, Const.SCREEN_X / 2 - 50, 50,
                                                    "CRÉDITOS")
            sair_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 490, Const.SCREEN_X / 2 - 50, 50,
                                                "SAIR")

            Draw_util.draw_text(screen, "(EM DESENVOLVIMENTO)", 8, Const.WHITE, Const.SCREEN_X / 2, 355)
            Draw_util.draw_text(screen, "(EM DESENVOLVIMENTO)", 8, Const.WHITE, Const.SCREEN_X / 2, 415)

            button_list = [jogar_button, loja_button, opcoes_button, creditos_button, sair_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if jogar_button.collidepoint((mx, my)) or self.cursor_point == jogar_button:
                self.cursor_point = self.cursor_event(jogar_button, self.difficulty_menu, mx, my)

            if loja_button.collidepoint((mx, my)) or self.cursor_point == loja_button:
                self.cursor_point = self.cursor_event(loja_button, self.loja_menu, mx, my)

            if opcoes_button.collidepoint((mx, my)) or self.cursor_point == opcoes_button:
                self.cursor_point = self.cursor_event(opcoes_button, self.opcoes_menu, mx, my)

            if creditos_button.collidepoint((mx, my)) or self.cursor_point == creditos_button:
                self.cursor_point = self.cursor_event(creditos_button, self.credios_menu, mx, my)

            if sair_button.collidepoint((mx, my)) or self.cursor_point == sair_button:
                self.cursor_point = self.cursor_event(sair_button, Menu_util.quit_game, mx, my)

            self.click_to_false()  # Depois de checar os inputs o click volta a ser falso
            self.draw_cursor(jogar_button)

            screen_update()

    def difficulty_menu(self):
        button_list = []
        self.show_difficulty_menu = True

        while self.show_difficulty_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.enter = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            # Título
            Draw_util.draw_text(screen, "Dificuldade", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 80)

            # Botões
            normal_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 250, Const.SCREEN_X / 2 - 50, 50,
                                                  "Normal")
            dificil_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 310, Const.SCREEN_X / 2 - 50, 50,
                                                   "Difícil")
            insano_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 120, 370, Const.SCREEN_X / 2 - 50, 50,
                                                  "Insano")

            button_list = [normal_button, dificil_button, insano_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if normal_button.collidepoint((mx, my)) or self.cursor_point == normal_button:
                game.difficulty = 1
                self.cursor_point = self.cursor_event(normal_button, game.new_game, mx, my)

            if dificil_button.collidepoint((mx, my)) or self.cursor_point == dificil_button:
                game.difficulty = 2
                self.cursor_point = self.cursor_event(dificil_button, game.new_game, mx, my)

            if insano_button.collidepoint((mx, my)) or self.cursor_point == insano_button:
                game.difficulty = 3
                self.cursor_point = self.cursor_event(insano_button, game.new_game, mx, my)

            self.click_to_false()  # Depois de checar os inputs o click volta a ser falso
            self.draw_cursor(normal_button)

            screen_update()

    def loja_menu(self):
        button_list = []
        self.show_loja_menu = True
        self.cursor_point = None

        while self.show_loja_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_loja_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.enter = True

                    if event.key == pygame.K_ESCAPE:
                        self.show_loja_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            Draw_util.draw_text(screen, "LOJA", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 80)
            Draw_util.draw_text(screen, f"Coins: {Data_util.get_coins()}", 14, Const.WHITE, 70, 150, topleft=True)

            spaceship_1_attributes = Data_util.get_spaceships("spaceship-1")
            spaceship_2_attributes = Data_util.get_spaceships("spaceship-2")
            spaceship_3_attributes = Data_util.get_spaceships("spaceship-3")

            ship_1_button = Draw_util.draw_loja_button(screen, "spaceship-1.png", 70, 180, 440, 120, "Violet Rocket",
                                                       spaceship_1_attributes["price"],
                                                       spaceship_1_attributes["lives"],
                                                       spaceship_1_attributes["shield"],
                                                       spaceship_1_attributes["damage"],
                                                       spaceship_1_attributes["velocity"],
                                                       spaceship_1_attributes["shoot_delay"])

            ship_2_button = Draw_util.draw_loja_button(screen, "spaceship-2.png", 70, 330, 440, 120, "Black Eagle",
                                                       spaceship_2_attributes["price"],
                                                       spaceship_2_attributes["lives"],
                                                       spaceship_2_attributes["shield"],
                                                       spaceship_2_attributes["damage"],
                                                       spaceship_2_attributes["velocity"],
                                                       spaceship_2_attributes["shoot_delay"])

            ship_3_button = Draw_util.draw_loja_button(screen, "spaceship-3.png", 70, 480, 440, 120, "Bat Spaceship",
                                                       spaceship_3_attributes["price"],
                                                       spaceship_3_attributes["lives"],
                                                       spaceship_3_attributes["shield"],
                                                       spaceship_3_attributes["damage"],
                                                       spaceship_3_attributes["velocity"],
                                                       spaceship_3_attributes["shoot_delay"])

            back_to_menu_button = Draw_util.draw_button(screen, 30, 670, 100, 30, "Voltar", font_size=14)

            button_list = [ship_1_button, ship_2_button, ship_3_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.mouse_click:
                    self.mouse_click, self.show_loja_menu = Menu_util.back_button(self.enter, self.show_loja_menu)

            if ship_1_button.collidepoint((mx, my)):
                def event():
                    Loja_util.equip_spaceship(Data_util, "spaceship-1")

                self.cursor_point = self.cursor_event(ship_1_button, event, mx, my)

            if ship_2_button.collidepoint((mx, my)):
                def event():
                    if "spaceship-2" not in Data_util.get_purchased_ships():
                        Loja_util.buy_spaceship(Data_util, "spaceship-2")
                    Loja_util.equip_spaceship(Data_util, "spaceship-2")

                self.cursor_point = self.cursor_event(ship_2_button, event, mx, my)

            if ship_3_button.collidepoint((mx, my)):
                def event():
                    if "spaceship-3" not in Data_util.get_purchased_ships():
                        Loja_util.buy_spaceship(Data_util, "spaceship-3")
                    Loja_util.equip_spaceship(Data_util, "spaceship-3")

                self.cursor_point = self.cursor_event(ship_3_button, event, mx, my)

            self.click_to_false()
            self.draw_cursor(ship_1_button)

            screen_update()

    def opcoes_menu(self):
        button_list = []
        self.cursor_point = None
        self.show_opcoes_menu = True

        while self.show_opcoes_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_opcoes_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        menu.enter = True

                    if event.key == pygame.K_ESCAPE:
                        self.show_opcoes_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu.mouse_click = True

            Draw_util.draw_text(screen, "OPÇÕES", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 80)

            sons_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 250, Const.SCREEN_X / 2 + 10, 50,
                                                "SONS")
            acessibilidade_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 320,
                                                          Const.SCREEN_X / 2 + 10, 50,
                                                          "ACESSIBILIDADE PARA DALTÔNICOS", font_size=9)

            voltar_button = Draw_util.voltar_button(screen)

            button_list = [sons_button, acessibilidade_button]

            mx, my = pygame.mouse.get_pos()

            if voltar_button.collidepoint((mx, my)):
                if self.mouse_click:
                    self.mouse_click = False
                    self.show_opcoes_menu = False

            if sons_button.collidepoint((mx, my)):
                self.cursor_point = self.cursor_event(sons_button, self.sons_options, mx, my)

            if acessibilidade_button.collidepoint((mx, my)):
                self.cursor_point = self.cursor_event(acessibilidade_button, self.acessibilidade_options, mx, my)

            self.click_to_false()
            self.draw_cursor(sons_button)

            screen_update()

    def credios_menu(self):
        self.show_creditos_menu = True
        while self.show_creditos_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_creditos_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_creditos_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            Draw_util.draw_text(screen, "CRÉDITOS", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 80)

            Draw_util.draw_text(screen, "DESENVOLVEDORES:", Const.SUB_TITLE_FONT, Const.WHITE, 40, 170, topleft=True)
            Draw_util.draw_text(screen, "LUCAS EDUARDO KREUCH", Const.SMALL_FONT, Const.WHITE, 100, 220, topleft=True)
            Draw_util.draw_text(screen, "MARIA CLARA DE SOUZA", Const.SMALL_FONT, Const.WHITE, 100, 240, topleft=True)
            Draw_util.draw_text(screen, "ALINE AMARAL DE SOUZA", Const.SMALL_FONT, Const.WHITE, 100, 260, topleft=True)
            Draw_util.draw_text(screen, "HAIDY JANDRE", Const.SMALL_FONT, Const.WHITE, 100, 280, topleft=True)

            Draw_util.draw_text(screen, "PROFESSORES:", Const.SUB_TITLE_FONT, Const.WHITE, 40, 370, topleft=True)
            Draw_util.draw_text(screen, "RICARDO DE LA ROCHA LADEIRA", Const.SMALL_FONT, Const.WHITE, 100, 420,
                                topleft=True)
            Draw_util.draw_text(screen, "LUIZ RICARDO URIARTE", Const.SMALL_FONT, Const.WHITE, 100, 440, topleft=True)

            back_to_menu_button = Draw_util.draw_button(screen, 30, 670, 100, 30, "Voltar", font_size=14)

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.mouse_click:
                    self.mouse_click = False
                    self.show_creditos_menu = False

            self.click_to_false()

            screen_update()

    def sons_options(self):
        button_list = []
        self.cursor_point = None
        self.show_options_sons_menu = True
        while self.show_options_sons_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_options_sons_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_options_sons_menu = False

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.enter = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            Draw_util.draw_text(screen, "SONS", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 80)

            music_button = Draw_util.draw_music_button(screen, Const.SCREEN_X / 2 - 150, 250, Const.SCREEN_X / 2 + 10,
                                                       70, "MÚSICA")
            som_button = Draw_util.draw_som_button(screen, Const.SCREEN_X / 2 - 150, 350, Const.SCREEN_X / 2 + 10,
                                                   70, "SOM")
            voltar_button = Draw_util.voltar_button(screen)

            button_list = [music_button, som_button]
            mx, my = pygame.mouse.get_pos()

            if voltar_button.collidepoint((mx, my)):
                if self.mouse_click:
                    self.mouse_click = False
                    self.show_options_sons_menu = False

            if music_button.collidepoint((mx, my)) or self.cursor_point == music_button:
                def change_music():
                    if Data_util.get_music_activated():
                        Data_util.set_music_activated(False)
                        pygame.mixer.music.pause()
                        pygame.mixer.music.set_volume(0)
                    else:
                        Data_util.set_music_activated(True)
                        pygame.mixer.music.set_volume(0.3)

                self.cursor_point = self.cursor_event(music_button, change_music, mx, my)

            if som_button.collidepoint((mx, my)) or self.cursor_point == som_button:
                def change_sound():
                    if Data_util.get_sound_activated():
                        Data_util.set_sound_activated(False)
                        for sound in Const.LIST_OF_SOUNDS:
                            sound.set_volume(0)
                    else:
                        Data_util.set_sound_activated(True)
                        for i, sound in enumerate(Const.LIST_OF_SOUNDS):
                            sound.set_volume(Const.LIST_OF_VOL[i])


                self.cursor_point = self.cursor_event(som_button, change_sound, mx, my)

            self.click_to_false()
            self.draw_cursor(music_button)

            screen_update()

    def acessibilidade_options(self):
        button_list = []
        self.cursor_point = None
        self.show_options_acessibilidade_menu = True

        while self.show_options_acessibilidade_menu:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_options_acessibilidade_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.cursor_point = Menu_util.cursor_event(button_list, self.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.enter = True

                    if event.key == pygame.K_ESCAPE:
                        self.show_options_acessibilidade_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_click = True

            Draw_util.draw_text(screen, "ACESSIBILIDADE", Const.TITLE_FONT - 10, Const.WHITE, Const.SCREEN_X / 2, 80)
            Draw_util.draw_text(screen, "PARA DALTÔNICOS", Const.TITLE_FONT - 10, Const.WHITE, Const.SCREEN_X / 2, 120)

            padrao_buton = Draw_util.draw_acessibilidade_button(screen, Const.SCREEN_X / 2 - 150, 250,
                                                                Const.SCREEN_X / 2 + 10, 50,
                                                                "PADRÃO", "default")
            deutranopia_buton = Draw_util.draw_acessibilidade_button(screen, Const.SCREEN_X / 2 - 150, 320,
                                                                     Const.SCREEN_X / 2 + 10,
                                                                     50, "DEUTERANOPIA", "deuteranopia")
            protanopia_buton = Draw_util.draw_acessibilidade_button(screen, Const.SCREEN_X / 2 - 150, 390,
                                                                    Const.SCREEN_X / 2 + 10, 50,
                                                                    "PROTANOPIA", "protanopia")
            tritanopia_buton = Draw_util.draw_acessibilidade_button(screen, Const.SCREEN_X / 2 - 150, 460,
                                                                    Const.SCREEN_X / 2 + 10, 50,
                                                                    "TRITANOPIA", "tritanopia")

            voltar_button = Draw_util.voltar_button(screen)

            button_list = [padrao_buton, deutranopia_buton, protanopia_buton, tritanopia_buton]
            mx, my = pygame.mouse.get_pos()

            if voltar_button.collidepoint((mx, my)):
                if self.mouse_click:
                    self.mouse_click = False
                    self.show_options_acessibilidade_menu = False

            if padrao_buton.collidepoint((mx, my)) or self.cursor_point == padrao_buton:
                def change_image():
                    Data_util.set_image("default")
                    Images.update()

                self.cursor_point = self.cursor_event(padrao_buton, change_image, mx, my)

            if deutranopia_buton.collidepoint((mx, my)) or self.cursor_point == deutranopia_buton:
                def change_image():
                    Data_util.set_image("deuteranopia")
                    Images.update()

                self.cursor_point = self.cursor_event(deutranopia_buton, change_image, mx, my)

            if protanopia_buton.collidepoint((mx, my)) or self.cursor_point == protanopia_buton:
                def change_image():
                    Data_util.set_image("protanopia")
                    Images.update()

                self.cursor_point = self.cursor_event(protanopia_buton, change_image, mx, my)

            if tritanopia_buton.collidepoint((mx, my)) or self.cursor_point == tritanopia_buton:
                def change_image():
                    Data_util.set_image("tritanopia")
                    Images.update()

                self.cursor_point = self.cursor_event(tritanopia_buton, change_image, mx, my)

            self.click_to_false()
            self.draw_cursor(padrao_buton)

            screen_update()

    def cursor_event(self, button, event, mx, my):
        if self.cursor_point != button:
            pygame.mixer.Sound.play(Const.SELECT_SOUND)
        if button.collidepoint((mx, my)):
            if self.mouse_click:
                self.mouse_click = False
                event()
        if self.enter:
            self.enter = False
            event()
        return button

    def draw_cursor(self, first_button):
        try:
            Draw_util.cursor(screen, self.cursor_point)
        except:
            self.cursor_point = first_button

    def click_to_false(self):
        self.enter = False
        self.mouse_click = False


class Game:
    def __init__(self):
        super().__init__()
        # Controle dos laços de repetição
        self.game_over = False
        self.show_pause = False
        self.show_game_over_screen = False
        self.draw_dev_options = False
        self.ready = False

        self.difficulty = None

    # Cria um novo jogo
    def new_game(self):
        menu.show_difficulty_menu = False
        # Sprite groups
        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.enemy_shoot_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.Group()
        self.boss_wings_group = pygame.sprite.Group()
        self.boss_shoot_group = pygame.sprite.Group()
        self.kamikaze_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()

        # Música tema do jogo
        pygame.mixer.music.load(path.join(getcwd() + f"/assets/music/{Data_util.get_music()}"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # Verifica se a música está desativada
        if not Data_util.get_music_activated():
            pygame.mixer.music.pause()
            pygame.mixer.music.set_volume(0)

        # Background do jogo
        self.game_background_rect = Background(Images.game_image_background)
        self.background = pygame.sprite.GroupSingle(self.game_background_rect)

        # Player
        self.player = Player(Data_util.get_player_spaceship(), Data_util.spaceship_attributes(), self.bullet_group)
        self.player_group_single = pygame.sprite.GroupSingle(self.player)
        # Imagem do player que serve como contador de vidas
        self.player_mini_image = pygame.transform.scale(self.player.image,
                                                        (Const.MINI_PLAYER_IMG, Const.MINI_PLAYER_IMG))

        # Asteroid
        self.asteroid_sprite_sheet = Sprite.create_sprite_sheet(Images.asteroid_image_dir, Const.ASTEROID_SIZE_X,
                                                                Const.ASTEROID_SIZE_Y)

        # Explosion
        self.explosion_sprite_sheet = Sprite.create_sprite_sheet(Images.explosion_image_dir, Const.EXPLOSION_WIDTH,
                                                                 Const.EXPLOSION_HEIGHT)

        # Enemy
        self.enemy_1_sprite_sheet = Sprite.create_sprite_sheet(Images.enemy_image_dir, Const.ENEMY_SIZE_X,
                                                               Const.ENEMY_SIZE_Y)
        self.create_enemy_delay = 2500
        self.last_enemy = pygame.time.get_ticks()

        # Kamikaze
        self.kamikaze_sprite_sheet = Sprite.create_sprite_sheet(Images.kamikaze_image_dir, Const.ENEMY_SIZE_X,
                                                                Const.ENEMY_SIZE_Y)
        self.create_kamikaze_delay = 7000
        self.last_kemikaze = pygame.time.get_ticks()

        # Shield bar
        self.player_shield_bar = Player_shield_bar(screen)
        self.enemy_shield_bar = Enemy_shield_bar(screen)
        self.kamikaze_shield_bar = Enemy_shield_bar(screen)
        self.boss_wings_shield_bar = Enemy_shield_bar(screen)
        self.boss_body_shield_bar = Enemy_shield_bar(screen)

        # Boss
        self.boss_body_sprite_sheet = Sprite.create_sprite_sheet(Images.boss_body_image_dir, Const.BODY_BOSS_SIZE_X,
                                                                 Const.BODY_BOSS_SIZE_Y)
        self.boss_wing_sprite_sheet = Sprite.create_sprite_sheet(Images.boss_wing_image_dir, Const.WING_BOSS_SIZE_X,
                                                                 Const.WING_BOSS_SIZE_Y)
        self.boss_event = False
        self.boss_created = False
        self.wing_explosion = False
        self.body_explosion = False
        self.left_wing_destroyed = False
        self.right_wing_destroyed = False
        self.boss_destroyed = False
        self.draw_body_boss_shield_bar = False
        self.boss_body_last_explosion = pygame.time.get_ticks()
        self.boss_wing_last_explosion = pygame.time.get_ticks()
        self.boss_last_explosion_index = 1

        # Controle de aparição dos asteroides
        self.asteroid_event_cooldown = pygame.time.get_ticks()
        self.asteroid_cooldown = pygame.time.get_ticks()
        self.asteroid_shower_time = pygame.time.get_ticks()
        self.asteroid_shower_event = False

        # Score
        self.score = Score()

        # Controladores de tempo
        self.ready_time = pygame.time.get_ticks()

        # Controle de aparecimento do Enemy
        self.ready = False

        self.draw_boss = False

        # Dificuldade do jogo
        if self.difficulty == 1:
            self.create_enemy_delay_multiplier = 0
            self.enemy_shoot_delay_multiplier = 0

        if self.difficulty == 2:
            self.create_enemy_delay_multiplier = self.create_enemy_delay / 2
            self.enemy_shoot_delay_multiplier = Const.ENEMY_SHOOT_DELAY / 8

        if self.difficulty == 3:
            self.create_enemy_delay_multiplier = self.create_enemy_delay / 1.8
            self.enemy_shoot_delay_multiplier = Const.ENEMY_SHOOT_DELAY / 6

            self.player.lives = 1

        # Roda o jogo
        self.game_over = False
        self.running()

    # Loop principal do jogo
    def running(self):
        #  Loop principal do jogo
        while not self.game_over:
            clock.tick(Const.FPS)
            self.events()  # Eventos do jogo
            self.collision_checks()  # Verificação das colisões do jogo
            self.powerups_collision_checks()  # Verifica a colissão com os powerups

            if self.ready:
                self.asteroid_shower()

                if not self.asteroid_shower_event and not self.boss_event:
                    self.generate_enemy()
                    self.generate_kamikaze()

            if self.score.get_score() >= 100 and not self.boss_destroyed:
                self.fBoss_event()

            self.check_lives()
            self.check_shield()

            if self.draw_dev_options:
                Game_utils.dev_options(clock)

            self.update_sprites()
            self.draw()

    # Função principal de renderização
    def draw(self):
        screen.fill(Const.BLACK)

        self.draw_groups()

        Draw_util.draw_text(screen, f"Score: {self.score.get_score()}", 18, Const.WHITE, Const.SCREEN_X / 2,
                            16)  # Texto do score

        self.draw_lives(self.player_mini_image)  # Vidas do Player
        self.player_shield_bar.draw_shield_bar(self.player.shield)  # Shield do Player

        self.draw_ready()

        # Shield bar do enemy
        for enemy in self.enemy_group:
            self.enemy_shield_bar.draw_shield_bar(enemy.shield, enemy.rect)

        # Shield bar do kamikaze
        for kamikaze in self.kamikaze_group:
            self.kamikaze_shield_bar.draw_shield_bar(kamikaze.shield, kamikaze.rect)

        if self.boss_event:
            margin = 0
            pos_x_add = 0

            for wing in self.boss_wings_group:
                if wing.rect.x < Const.SCREEN_X / 2:
                    margin = -40
                    pos_x_add = 25
                if wing.rect.x > Const.SCREEN_X / 2:
                    margin = -40
                    pos_x_add = -25 + (margin * -1)
                pos_y_add = 40

                self.boss_wings_shield_bar.draw_shield_bar(wing.shield, wing.rect, additional_x_position=pos_x_add,
                                                           additional_y_position=pos_y_add, margin=margin)

            if self.draw_body_boss_shield_bar:
                self.boss_body_shield_bar.draw_shield_bar(self.boss.shield, self.boss.rect)

    # Atualiza os grupos de sprites
    def update_sprites(self):
        self.background.update()
        self.coin_group.update()
        self.player_group_single.update()
        self.explosion_group.update()
        self.asteroid_group.update()
        self.bullet_group.update()
        self.enemy_shoot_group.update()
        self.powerup_group.update()
        self.kamikaze_group.update()

        if self.boss_event:
            self.boss_shoot_group.update()
            self.boss_group.update()
            self.boss_wings_group.update()

        self.enemy_group.update()
        pygame.display.update()

    # Desenha na tela os grupos de sprites
    def draw_groups(self):
        self.background.draw(screen)
        self.coin_group.draw(screen)
        self.enemy_group.draw(screen)
        self.asteroid_group.draw(screen)
        self.bullet_group.draw(screen)
        self.enemy_shoot_group.draw(screen)
        self.powerup_group.draw(screen)
        self.player_group_single.draw(screen)
        self.kamikaze_group.draw(screen)

        if self.boss_event:
            self.boss_shoot_group.draw(screen)
            self.boss_group.draw(screen)
            self.boss_wings_group.draw(screen)

        self.explosion_group.draw(screen)

    # Eventos de input
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_pause = True
                    pygame.mixer.music.pause()
                    self.pause_screen()

                if event.key == pygame.K_p:
                    self.asteroid_shower_event = True

                if event.key == pygame.K_i:
                    self.score.add_score(100)

                if event.key == pygame.K_l:
                    self.game_over_screen()

                if event.key == pygame.K_F3:
                    if not self.draw_dev_options:
                        self.draw_dev_options = True
                    else:
                        self.draw_dev_options = False

    # Checa as colisões do jogo
    def collision_checks(self):
        # Colisão do tiro do Player com o Asteroide
        def asteroid_collision_with_player_shots():
            collision = pygame.sprite.groupcollide(self.asteroid_group, self.bullet_group, True, True,
                                                   pygame.sprite.collide_mask)
            for hit in collision:
                self.score.add_score()
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

        # Colisão do Player com o Asteroide
        def player_collision_with_asteroid():
            collision = pygame.sprite.spritecollide(self.player, self.asteroid_group, True, pygame.sprite.collide_mask)
            for hit in collision:
                self.player.shield -= Const.ASTEROID_DAMAGE
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

        # Colisão do Inimigo com o tiro do Player
        def enemy_collision_with_player_shot():
            collision = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, False, True,
                                                   pygame.sprite.collide_mask)
            for hit in collision:
                hit.shield -= self.player.damage

                if hit.shield <= 0:
                    # Chance de dropar um powerup
                    if randint(0, 10) >= 5:
                        powerup = Powerup(hit.rect.center)
                        self.powerup_group.add(powerup)

                    self.score.add_score()
                    hit.kill()
                    explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                    self.explosion_group.add(explosion)

                    self.chance_to_drop_coins(hit.rect.centerx, hit.rect.centery)

        # Colisão entre o Asteroide e o Inimigo
        def collision_between_the_asteroid_and_the_enemy():
            collision = pygame.sprite.groupcollide(self.enemy_group, self.asteroid_group, True, True,
                                                   pygame.sprite.collide_mask)
            for hit in collision:
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

        # Colisão do tiro do Inimigo com o Player
        def enemy_shot_collision_with_player():
            collision = pygame.sprite.spritecollide(self.player, self.enemy_shoot_group, True)
            for hit in collision:
                self.player.shield -= hit.damage

        # Colisão do tiro do Player com o Kamikaze
        def player_shoot_collision_with_kamikaze():
            collision = pygame.sprite.groupcollide(self.kamikaze_group, self.bullet_group, False, True,
                                                   pygame.sprite.collide_mask)
            for kamikaze_hit in collision:
                kamikaze_hit.shield -= self.player.damage
                if kamikaze_hit.shield <= 0:
                    explosion = Explosion(kamikaze_hit.rect.center, self.explosion_sprite_sheet)
                    self.explosion_group.add(explosion)
                    self.score.add_score()
                    kamikaze_hit.kill()

        # Colisão do Kamikaze com o Player
        def kamikaze_collision_with_player():
            collision = pygame.sprite.spritecollide(self.player, self.kamikaze_group, False)
            for hit in collision:
                self.player.shield -= hit.damage
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)
                hit.kill()

        # Colisão entre o Player e o Inimigo
        def collision_between_the_player_and_the_enemy():
            collision = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
            for hit in collision:
                self.player.shield -= Const.PLAYER_COLLIDE_DAMAGE
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)
                hit.kill()

        # Colisão entre o Player e o Coin
        def collision_between_the_player_and_the_coin():
            collision = pygame.sprite.spritecollide(self.player, self.coin_group, True)
            if collision:
                Coin.collided_with_coin(1, Data_util)

        # ---------- Colisões com o Boss ---------- #

        # Colisão do tiro do Player com a Asa do Boss
        def player_bullet_collision_with_boss_wing():
            collision = pygame.sprite.groupcollide(self.boss_wings_group, self.bullet_group, False, True,
                                                   pygame.sprite.collide_mask)
            for wing_hit in collision:
                wing_hit.shield -= self.player.damage * 1
                if wing_hit.shield <= 0:
                    self.score.add_score(20)
                    self.wing_explosion = True
                    wing_hit.kill()

        # Colisão do tiro do Player com o corpo do Boss
        def collision_of_the_player_bullet_with_the_boss_body():
            collision = pygame.sprite.groupcollide(self.boss_group, self.bullet_group, False, True,
                                                   pygame.sprite.collide_mask)
            if self.draw_body_boss_shield_bar:
                for body_hit in collision:
                    body_hit.shield -= self.player.damage * 1
                    if body_hit.shield <= 0:
                        self.score.add_score(50)
                        self.body_explosion = True
                        body_hit.kill()

        # Colisão do Player com o Boss
        def player_collision_with_boss():
            player_collision_boss = pygame.sprite.spritecollide(self.player, self.boss_group, False,
                                                                pygame.sprite.collide_mask)
            if player_collision_boss:
                self.player.shield = 0

        # Colisão do Player com as asas do Boss
        def player_collision_with_Boss_wings():
            collision = pygame.sprite.spritecollide(self.player, self.boss_wings_group, False,
                                                    pygame.sprite.collide_mask)
            if collision:
                self.player.shield = 0

        # Colisão do tiro do Boss com o Player
        def boss_shooting_collision_with_player():
            collision = pygame.sprite.spritecollide(self.player, self.boss_shoot_group, True,
                                                    pygame.sprite.collide_mask)
            for hit in collision:
                self.player.shield -= hit.damage

        # ----------------------------------------- #

        def update():
            asteroid_collision_with_player_shots()
            player_collision_with_asteroid()
            enemy_collision_with_player_shot()
            collision_between_the_asteroid_and_the_enemy()
            enemy_shot_collision_with_player()
            player_shoot_collision_with_kamikaze()
            kamikaze_collision_with_player()
            collision_between_the_player_and_the_enemy()
            collision_between_the_player_and_the_coin()

            # Boss
            player_bullet_collision_with_boss_wing()
            collision_of_the_player_bullet_with_the_boss_body()
            player_collision_with_boss()
            player_collision_with_Boss_wings()
            boss_shooting_collision_with_player()

        update()

    # Colissão do Player com os Powerups
    def powerups_collision_checks(self):
        powerup_collide = pygame.sprite.spritecollide(self.player, self.powerup_group, True)
        for hit in powerup_collide:
            if hit.type == "shield":
                self.player.shield += 20
                if self.player.shield >= 100:
                    self.player.shield = 100

            if hit.type == "gun":
                self.player.powerup()

    # Checa se o Player tem vidas
    def check_lives(self):
        # Verifica se o player ainda tem vidas
        if self.player.lives == 0 and not self.death_explosion.alive():  # -- Teste -- and not self.death_explosion.alive()
            self.game_over = True
            self.game_over_screen()

    # Checa a quantidade de shield do Player
    def check_shield(self):
        if self.player.shield <= 0:
            self.death_explosion = Explosion(self.player.rect.center, self.explosion_sprite_sheet)
            self.explosion_group.add(self.death_explosion)
            self.player.hide()  # Esconde o player temporariamete
            self.player.lives -= 1  # Tira uma vida do player
            self.player.shield = 100  # O shield do jogador volta a ser 100

    # ------------ Screens ----------- #
    # Tela de pause
    def pause_screen(self):
        button_list = []
        menu.cursor_point = None

        self.show_pause = True
        while self.show_pause:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_pause = False
                    self.game_over = True
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_pause = False
                        pygame.mixer.music.unpause()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            menu.cursor_point = Menu_util.cursor_event(button_list, menu.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        menu.enter = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu.enter = True

            # Título
            Draw_util.draw_text(screen, "PAUSE", Const.TITLE_FONT, Const.WHITE, Const.SCREEN_X / 2, 100)

            # Botões
            voltar_ao_jogo_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 250,
                                                          Const.SCREEN_X / 2 + 10, 50, "VOLTAR AO JOGO")
            voltar_ao_menu_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 310,
                                                          Const.SCREEN_X / 2 + 10, 50, "VOLTAR AO MENU")
            sair_do_jogo_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 370, Const.SCREEN_X / 2 + 10,
                                                        50, "SAIR DO JOGO")

            button_list = [voltar_ao_jogo_button, voltar_ao_menu_button, sair_do_jogo_button]
            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if voltar_ao_jogo_button.collidepoint((mx, my)) or menu.cursor_point == voltar_ao_jogo_button:
                def event():
                    self.show_pause = False
                    pygame.mixer.music.unpause()

                menu.cursor_point = menu.cursor_event(voltar_ao_jogo_button, event, mx, my)

            if voltar_ao_menu_button.collidepoint((mx, my)) or menu.cursor_point == voltar_ao_menu_button:
                def event():
                    self.show_pause = False
                    self.game_over = True
                    pygame.mixer.music.stop()
                    menu.menu()

                menu.cursor_point = menu.cursor_event(voltar_ao_menu_button, event, mx, my)

            if sair_do_jogo_button.collidepoint((mx, my)) or menu.cursor_point == sair_do_jogo_button:
                def event():
                    self.show_pause = False
                    self.game_over = True
                    pygame.quit()
                    exit()

                menu.cursor_point = menu.cursor_event(sair_do_jogo_button, event, mx, my)

            menu.click_to_false()
            menu.draw_cursor(voltar_ao_jogo_button)
            screen_update()

    # Tela de game over
    def game_over_screen(self):
        button_list = []
        menu.cursor_point = None
        pygame.mixer.music.stop()

        self.show_game_over_screen = True
        while self.show_game_over_screen:
            clock.tick(Const.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        menu.cursor_point = Menu_util.cursor_event(button_list, menu.cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        menu.enter = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu.enter = True

            Draw_util.draw_text(screen, "GAME OVER", 42, Const.RED, Const.SCREEN_X / 2, 60)
            Draw_util.draw_text(screen, f"SCORE: {self.score.get_score()}", 42, Const.WHITE, Const.SCREEN_X / 2,
                                Const.SCREEN_Y / 2 - 124)

            voltar_ao_menu_buttom = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 300,
                                                          Const.SCREEN_X / 2 + 10, 50, "Voltar ao menu")
            jogar_novamente_button = Draw_util.draw_button(screen, Const.SCREEN_X / 2 - 150, 360,
                                                           Const.SCREEN_X / 2 + 10, 50, "Jogar novamente", font_size=19)

            button_list = [voltar_ao_menu_buttom, jogar_novamente_button]

            mx, my = pygame.mouse.get_pos()

            if voltar_ao_menu_buttom.collidepoint((mx, my)) or menu.cursor_point == voltar_ao_menu_buttom:
                def voltar_ao_menu():
                    self.show_game_over_screen = False
                    menu.menu()

                menu.cursor_point = menu.cursor_event(voltar_ao_menu_buttom, voltar_ao_menu, mx, my)

            if jogar_novamente_button.collidepoint((mx, my)) or menu.cursor_point == jogar_novamente_button:
                def jogar_novamente():
                    self.show_game_over_screen = False
                    self.new_game()

                menu.cursor_point = menu.cursor_event(jogar_novamente_button, jogar_novamente, mx, my)

            menu.click_to_false()
            menu.draw_cursor(voltar_ao_menu_buttom)
            screen_update()

    # Chance de dropar moedas
    def chance_to_drop_coins(self, pos_x, pos_y):
        if randint(1, 2) > 0:
            coin = Coin(pos_x, pos_y, self.coin_group)

    # Função para criar um novo asteroide
    def new_asteroid(self):
        asteroid = Asteroid(self.asteroid_sprite_sheet)
        self.asteroid_group.add(asteroid)

    # Evento de chuva de asteroides
    def asteroid_shower(self):
        if pygame.time.get_ticks() - self.asteroid_shower_time > Const.ASTEROID_SHOWER_COOLDOWN_TIME or self.asteroid_shower_event:
            self.asteroid_shower_time = pygame.time.get_ticks()

            if randint(0, 100) >= 80 and not self.asteroid_shower_event:
                self.asteroid_cooldown = pygame.time.get_ticks()
                self.asteroid_event_cooldown = pygame.time.get_ticks()

                self.asteroid_shower_event = True

            if self.asteroid_shower_event:
                if pygame.time.get_ticks() - self.asteroid_cooldown > Const.ASTEROID_COOLDOWN:
                    self.asteroid_cooldown = pygame.time.get_ticks()
                    self.new_asteroid()

                if pygame.time.get_ticks() - self.asteroid_event_cooldown > Const.ASTEROID_EVENT_COOLDOWN:
                    self.asteroid_event_cooldown = pygame.time.get_ticks()
                    self.asteroid_shower_event = False

    # Gera novos inimigos
    def generate_enemy(self):
        if pygame.time.get_ticks() - self.last_enemy > self.create_enemy_delay - self.create_enemy_delay_multiplier:
            self.last_enemy = pygame.time.get_ticks()
            enemy_type = randint(1, 3)
            if enemy_type <= 2:
                self.new_solo_enemy()
            if enemy_type == 3:
                self.new_tripe_enemy()

    # Função para criar inimigos
    def new_tripe_enemy(self):
        pos_x = randint(0 + Const.ENEMY_SIZE_X / 2, Const.SCREEN_X - (Const.ENEMY_SIZE_X * 3) + Const.ENEMY_SIZE_X / 2)
        pos_y = -20
        distance_x = Const.ENEMY_SIZE_X
        distance_y = 20
        for i in range(3):
            if i == 0:
                enemy = self.create_enemy(pos_x, pos_y)
            else:
                enemy = self.create_enemy(pos_x + distance_x, pos_y - distance_y)
                distance_x += Const.ENEMY_SIZE_X
                distance_y -= 20
            self.enemy_group.add(enemy)

    # Novo inimigo solo
    def new_solo_enemy(self):
        pos_x = randint(Const.ENEMY_SIZE_X / 2, Const.SCREEN_X - (Const.ENEMY_SIZE_X / 2))
        pos_y = -20
        enemy = self.create_enemy(pos_x, pos_y)
        self.enemy_group.add(enemy)

    # Novo kamikaze
    def new_kamikaze(self, x1=0, x2=0):
        kamikaze_1 = self.create_kamikaze(Const.KAMIKAZE_X_POS_1 + x1, Const.KAMIKAZE_SHIELD)
        kamikaze_2 = self.create_kamikaze(Const.KAMIKAZE_X_POS_2 - x2, Const.KAMIKAZE_SHIELD)
        self.kamikaze_group.add(kamikaze_1, kamikaze_2)

    # Gera o kamikaze
    def generate_kamikaze(self):
        if pygame.time.get_ticks() - self.last_kemikaze > self.create_kamikaze_delay:
            self.last_kemikaze = pygame.time.get_ticks()
            self.new_kamikaze()

    # Cria o inimigo
    def create_enemy(self, x, y):
        enemy = Enemy(x, y, Const.ENEMY_SHIELD, Const.ENEMY_DAMGE, self.enemy_1_sprite_sheet, self.enemy_shoot_group,
                      self.enemy_shoot_delay_multiplier)
        return enemy

    # Cria o kamikaze
    def create_kamikaze(self, x, shield):
        kamikaze = Kamikaze(x, shield, self.kamikaze_sprite_sheet)
        return kamikaze

    # Evento do Boss
    def fBoss_event(self):
        self.boss_event = True

        if not self.boss_created:
            self.create_boss()

        if self.boss_created:
            if self.wing_explosion:
                self.wing_explosion_event()

            if self.left_wing_destroyed and self.right_wing_destroyed:
                self.final_boss_event()

            if self.body_explosion:
                self.body_explosion_event()
                self.boss_event = False

            if self.left_wing_destroyed and self.right_wing_destroyed:
                self.draw_body_boss_shield_bar = True

    def final_boss_event(self):
        # Gera inimigos
        if pygame.time.get_ticks() - self.last_enemy > self.create_enemy_delay - self.create_enemy_delay_multiplier:
            self.last_enemy = pygame.time.get_ticks()
            self.new_kamikaze(100, 100)

    # Explosão do Boss
    def body_explosion_event(self):
        if not self.boss_destroyed:
            explosion_pos = [self.boss.rect.centerx, self.boss.rect.bottom]
            if pygame.time.get_ticks() - self.boss_wing_last_explosion > 1600:
                explosion_pos[0] += (sin(self.boss_last_explosion_index) * 60)
                explosion_pos[1] -= self.boss_last_explosion_index * 8

                explosion = Explosion(explosion_pos, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

                self.boss_last_explosion_index += 1

                if self.boss_last_explosion_index > 25:
                    self.boss_last_explosion_index = 1
                    self.body_explosion = False
                    self.boss_destroyed = True

    # Explosão da Asa do Boss
    def wing_explosion_event(self):
        if self.boss.left_wing.shield <= 0 and not self.left_wing_destroyed:
            explosion_pos = [self.boss.left_wing.rect.right - 10, self.boss.rect.top + 90]

            if pygame.time.get_ticks() - self.boss_wing_last_explosion > 2000:
                explosion_pos[0] -= self.boss_last_explosion_index * 8
                explosion_pos[1] += (sin(self.boss_last_explosion_index) * 50)

                explosion = Explosion(explosion_pos, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

                self.boss_last_explosion_index += 1

                if self.boss_last_explosion_index > 21:
                    self.boss_last_explosion_index = 1
                    self.wing_explosion = False
                    self.left_wing_destroyed = True

        if self.boss.right_wing.shield <= 0 and not self.right_wing_destroyed:
            explosion_pos = [self.boss.right_wing.rect.left + 10, self.boss.rect.top + 90]

            if pygame.time.get_ticks() - self.boss_wing_last_explosion > 2000:
                explosion_pos[0] = explosion_pos[0] + self.boss_last_explosion_index * 8
                explosion_pos[1] = explosion_pos[1] + (sin(self.boss_last_explosion_index) * 50)

                explosion = Explosion(explosion_pos, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)

                self.boss_last_explosion_index += 1

                if self.boss_last_explosion_index > 21:
                    self.boss_last_explosion_index = 1
                    self.wing_explosion = False
                    self.right_wing_destroyed = True

    # Cria o Boss
    def create_boss(self):
        self.boss_created = True
        self.boss = Boss(self.boss_body_sprite_sheet, self.boss_wing_sprite_sheet, self.boss_shoot_group)
        self.boss_group.add(self.boss)
        self.boss_wings_group.add(self.boss.left_wing)
        self.boss_wings_group.add(self.boss.right_wing)

    # Desenha a quantidade de vidas do jogador
    def draw_lives(self, image):
        for i in range(self.player.lives):
            image_rect = image.get_rect()
            image_rect.x = (Const.SCREEN_X - 50) + (Const.MINI_PLAYER_IMG + 10) * -i
            image_rect.y = 10
            screen.blit(image, image_rect)

    # Denha o texto de READY no início do jogo
    def draw_ready(self):
        if Const.READY_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            Draw_util.draw_text(screen, "READY?", 42, Const.YELLOW, Const.SCREEN_X / 2, 100)
        if Const.GO_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            Draw_util.draw_text(screen, "GO", 42, Const.YELLOW, Const.SCREEN_X / 2, 150)
        if pygame.time.get_ticks() - self.ready_time > 3000:
            self.ready = True


# -------------------------------------------------------- // -------------------------------------------------------- #


def screen_update():
    pygame.display.update()
    screen.fill(Const.BLACK)


# -------------------------------------------------------- // -------------------------------------------------------- #


if __name__ == '__main__':
    pygame.init()  # Inicializa o pygame
    pygame.mixer.init()  # Inicializa o modulo de mixer

    menu = Menu()
    game = Game()

    # Tela do jogo
    screen = pygame.display.set_mode((Const.SCREEN_X, Const.SCREEN_Y))
    pygame.display.set_caption("Space Battle")

    # Ajuda a controlar a taxa de atualização do jogo — FPS
    clock = pygame.time.Clock()

    menu.menu()
