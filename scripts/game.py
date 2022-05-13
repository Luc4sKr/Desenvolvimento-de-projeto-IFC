import pygame

from os import path, getcwd, listdir
from sys import exit

from scripts.constantes import *
from scripts.player import Player
from scripts.enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()

        # -- Tela do jogo -----------------------------------------
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption("Space Battle")
        # ---------------------------------------------------------

        # -- Cria um objeto para ajudar a controlar o tempo -------
        self.clock = pygame.time.Clock()
        # ---------------------------------------------------------

        # -- Controle dos laços de repetição ----------------------
        self.rodando = True
        self.game_over = False
        self.mostrar_menu = True
        # --------------------------------------------------------

        # -- Variáveis do menu -----------------------------------
        self.cursor_rect = pygame.Rect(100, 300, 100, 100)
        self.cursor_point = "Jogar"
        # --------------------------------------------------------

        # -- Função para carregar os arquivos --------------------
        self.carregar_arquivos()
        # --------------------------------------------------------

    # Menu do jogo ----------------------------------------------------------------------------------------
    def menu(self):
        self.menu_background_group = pygame.sprite.Group()
        #self.menu_background_group.add(self.menu_background)

        while self.mostrar_menu:
            self.clock.tick(FPS)

            self.menu_background_group.update()
            self.menu_background_group.draw(self.screen)

            self.draw_text("SPACE", 50, YELLOW, SCREEN_X / 2, 100)
            self.draw_text("BATTLE", 50, YELLOW, SCREEN_X / 2, 160)

            self.draw_text("Jogar", 40, WHITE, SCREEN_X / 2, 300)
            self.draw_text("Loja", 40, WHITE, SCREEN_X / 2, 350)
            self.draw_text("Opções", 40, WHITE, SCREEN_X / 2, 400)
            self.draw_text("Créditos", 40, WHITE, SCREEN_X / 2, 450)
            self.draw_text("Sair", 40, WHITE, SCREEN_X / 2, 500)

            self.menu_events()

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)

    # Eventos do menu -------------------------------------------------------------------------------------
    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
                self.mostrar_menu = False
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if self.cursor_point == "Jogar":
                        self.new_game()
                        self.mostrar_menu = False
                    if self.cursor_point == "Loja":
                        pass
                    if self.cursor_point == "Opções":
                        pass
                    if self.cursor_point == "Créditos":
                        self.mostrar_creditos = True
                        self.mostrar_menu = False
                        self.creditos()
                    if self.cursor_point == "Sair":
                        self.rodando = False
                        exit()

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.cursor_point == "Loja":
                        self.cursor_point = "Jogar"
                        self.cursor_rect.y = 300
                    if self.cursor_point == "Opções":
                        self.cursor_point = "Loja"
                        self.cursor_rect.y = 350
                    if self.cursor_point == "Créditos":
                        self.cursor_point = "Opções"
                        self.cursor_rect.y = 400
                    if self.cursor_point == "Sair":
                        self.cursor_point = "Créditos"
                        self.cursor_rect.y = 450

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.cursor_point == "Créditos":
                        self.cursor_point = "Sair"
                        self.cursor_rect.y = 500
                    if self.cursor_point == "Opções":
                        self.cursor_point = "Créditos"
                        self.cursor_rect.y = 450
                    if self.cursor_point == "Loja":
                        self.cursor_point = "Opções"
                        self.cursor_rect.y = 400
                    if self.cursor_point == "Jogar":
                        self.cursor_point = "Loja"
                        self.cursor_rect.y = 350

                #print(self.cursor)

        self.draw_cursor()


    def draw_cursor(self):
        self.draw_text("->", 25, WHITE, self.cursor_rect.x, self.cursor_rect.y)

    # Novo jogo -------------------------------------------------------------------------------------------
    def new_game(self):
        # -- Instancia as sprites -------------------
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.game_background)

        # Player
        self.player = Player()
        self.sprite_group.add(self.player)

        # Enemy
        self.enemy_group = pygame.sprite.Group()
        self.enemy_1_sprite_sheet = self.create_spaceship_sprite_sheet("enemy_1", 100, 100)
        # -------------------------------------------

        # -- Roda o jogo ----------------------------
        self.running()
        # -------------------------------------------

    # Rodando ---------------------------------------------------------------------------------------------
    def running(self):
        #  -- Loop do jogo --------------------------
        while not self.game_over:
            self.clock.tick(FPS)

            self.eventos()
            self.update_sprites()
            self.draw_sprites()

            #self.draw_text(f"{self.player.vel}", 20, WHITE, 100, 100)

    # Eventos do jogo -------------------------------------------------------------------------------------
    def eventos(self):
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                self.rodando = False
                exit()

    # Atualiza as sprites ---------------------------------------------------------------------------------
    def update_sprites(self):
        self.sprite_group.update()
        pygame.display.update()

    # Desenha as sprites ----------------------------------------------------------------------------------
    def draw_sprites(self):
        #self.sprite_group.add(self.enemy_1)

        self.screen.fill(WHITE)
        self.sprite_group.draw(self.screen)
        pygame.display.flip()

    # Texto -----------------------------------------------------------------------------------------------
    def draw_text(self, text, tam, color, x, y):
        self.fonte = pygame.font.Font(FONTE, tam)
        self.text_obj = self.fonte.render(text, False, color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (x, y)
        self.screen.blit(self.text_obj, self.text_rect)

    # Carrega os arquivos do jogo -------------------------------------------------------------------------
    def carregar_arquivos(self):
        self.menu_background = pygame.sprite.Sprite()
        self.menu_background.image = pygame.image.load(path.join(getcwd() + "/assets/images/background.png"))
        self.menu_background.image = pygame.transform.scale(self.menu_background.image, (SCREEN_X, SCREEN_Y))
        self.menu_background.rect = self.menu_background.image.get_rect()

        self.game_background = pygame.sprite.Sprite()
        self.game_background.image = pygame.image.load(path.join(getcwd() + "/assets/images/game_background.jpg"))
        self.game_background.image = pygame.transform.scale(self.game_background.image, (SCREEN_X, SCREEN_Y))
        self.game_background.rect = self.game_background.image.get_rect()
        


    def tela_game_over(self):
        pass

    # Cria as sprite sheets de naves -----------------------------------------------------------------------
    def create_spaceship_sprite_sheet(self, sprite, sprite_size_x, sprite_size_y):
        self.animation_list = []
        self.animation_types = ["move"]

        for animation in self.animation_types:
            self.temp_list = []
            self.num_of_frames = len(listdir(f"assets/images/sprites/{sprite}/{animation}"))
            for i in range(0, self.num_of_frames):
                self.image = pygame.image.load(path.join(getcwd() + f"/assets/images/sprites/{sprite}/{animation}/sprite_{i}.png"))
                self.image = pygame.transform.scale(self.image, (sprite_size_x, sprite_size_y))
                self.temp_list.append(self.image)
            self.animation_list.append(self.temp_list)
        return self.animation_list

    # Tela de créditos do menu ------------------------------------------------------------------------------
    def creditos(self):
        while self.mostrar_creditos:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mostrar_creditos = False
                    self.self.rodando = False
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE or pygame.K_ESCAPE:
                        self.mostrar_creditos = False
                        self.mostrar_menu = True
                        self.menu()

            self.draw_text("CRÉDITOS", 42, WHITE, SCREEN_X/2, 60)
            self.draw_text("LUCAS EDUARDO KREUCH", 28, WHITE, SCREEN_X/2, 150)
            self.draw_text("MARIA CLARA DE SOUZA", 28, WHITE, SCREEN_X/2, 180)
            self.draw_text("HAIDY JANDRE", 28, WHITE, SCREEN_X/2, 210)
            self.draw_text("DAVI GABRIEL KRUEGER", 28, WHITE, SCREEN_X/2, 240)

            
            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)




        

        

