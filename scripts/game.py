import pygame

from os import path, getcwd, listdir
from sys import exit

from scripts.constantes import *
from scripts.explosion import Explosion
from scripts.player import Player
from scripts.enemy import Enemy
from scripts.asteroid import Asteroid


class Game:
    def __init__(self):
        pygame.init() # Inicializa o pygame
        pygame.mixer.init() # Inicializa o modulo de mixer

        # -- Tela do jogo -----------------------------------------
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption("Space Battle")

        # -- Cria um objeto para ajudar a controlar o tempo -------
        self.clock = pygame.time.Clock()

        # -- Controle dos laços de repetição ----------------------
        self.rodando = True
        self.game_over = False
        self.mostrar_menu = True

        # -- Variáveis do menu -----------------------------------
        self.cursor_rect = pygame.Rect(100, 300, 100, 100)
        self.cursor_point = "Jogar"

        # -- Função para carregar os arquivos --------------------
        self.carregar_arquivos()

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
        # -- Sprite groups -------------------
        self.sprite_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()

        # -- Background
        self.sprite_group.add(self.game_background)

        # -- Player ---------------------------------
        self.player = Player(self.sprite_group, self.bullet_group)
        self.sprite_group.add(self.player)
        self.player_mini_image = pygame.transform.scale(self.player.image, (25, 25))

        # -- Asteroid -------------------------------
        self.asteroid_sprite_sheet = self.create_sprite_sheet("asteroid", ASTEROID_SIZE_X, ASTEROID_SIZE_Y, "rotate")
        self.asteroid_sprite_sheet = self.asteroid_sprite_sheet[0]
        for i in range(8):
            self.newasteroid()

        # -- Explosion ------------------------------
        self.explosion_sprite_sheet = self.create_sprite_sheet("explosion", 50, 50, "explosion-1")
        self.explosion_sprite_sheet = self.explosion_sprite_sheet[0]

        # -- Enemy ----------------------------------
        self.enemy_group = pygame.sprite.Group()
        self.enemy_1_sprite_sheet = self.create_sprite_sheet("enemy_1", ENEMY_SIZE_X, ENEMY_SIZE_Y, "move")

        # -- Score ----------------------------------
        self.score = 0

        # -- Roda o jogo ----------------------------
        self.game_over = False
        self.running()

    # Rodando ---------------------------------------------------------------------------------------------
    def running(self):
        #  -- Loop do jogo --------------------------
        while not self.game_over:
            self.clock.tick(FPS)

            self.eventos()
            self.update_sprites()
            self.draw_sprites()

            # Colissão dos tiros com os asteroides
            self.bullet_collide = pygame.sprite.groupcollide(self.asteroid_group, self.bullet_group, True, True, pygame.sprite.collide_circle)
            for hit in self.bullet_collide:
                self.score += 1
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(explosion)
                self.newasteroid()

            # Colisão da nave com os asteroides
            self.player_collide = pygame.sprite.spritecollide(self.player, self.asteroid_group, True, pygame.sprite.collide_mask)
            for hit in self.player_collide:
                self.player.shield -= 20
                self.newasteroid() # Cria um novo asteroide
                if self.player.shield <= 0:
                    self.death_explosion = Explosion(self.player.rect.center, self.explosion_sprite_sheet)
                    self.sprite_group.add(self.death_explosion)
                    self.player.hide() # Esconde o player temporariamete
                    self.player.lives -= 1 # Tira uma vida do player
                    self.player.shield = 100 # O shield do jogador volta a ser 100

            # Verifica se o player ainda tem vidas
            if self.player.lives == 0 and not self.death_explosion.alive():
                self.game_over = True
                self.mostrar_menu = True
                self.menu()

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

        # Texto/Draw
        self.draw_text(f"Score: {self.score}", 18, WHITE, SCREEN_X/2, 16) # Texto do score
        self.draw_shield_bar(self.screen, 5, 10, self.player.shield)
        self.draw_lives(self.screen, 480, 10, self.player_mini_image)

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

    def newasteroid(self):
        m = Asteroid(self.asteroid_sprite_sheet)
        self.sprite_group.add(m)
        self.asteroid_group.add(m)

    # Cria as sprite sheets de naves -----------------------------------------------------------------------
    def create_sprite_sheet(self, sprite, sprite_size_x, sprite_size_y, *animation_type):
        self.animation_list = []
        self.animation_types = animation_type

        for animation in self.animation_types:
            self.temp_list = []
            self.num_of_frames = len(listdir(f"assets/images/sprites/{sprite}/{animation}"))
            for i in range(1, self.num_of_frames):
                self.image = pygame.image.load(path.join(getcwd() + f"/assets/images/sprites/{sprite}/{animation}/sprite-{i}.png"))
                self.image = pygame.transform.scale(self.image, (sprite_size_x, sprite_size_y))
                self.temp_list.append(self.image)
            self.animation_list.append(self.temp_list)
        return self.animation_list

    # Desenha o escudo do player
    def draw_shield_bar(self, surface, x, y, shield):
        if self.player.shield < 0:
            self.player.shield = 0
        fill = (self.player.shield / 100) * BAR_WIDTH
        outline_rect = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surface, GREEN, fill_rect)
        pygame.draw.rect(surface, WHITE, outline_rect, 2)

    # Desenha a quantidade de vidas do jogador
    def draw_lives(self, surface, x, y, image):
        for i in range(self.player.lives):
            image_rect = image.get_rect()
            image_rect.x = x + 30 * i
            image_rect.y = y
            surface.blit(image, image_rect)

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

            
            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)




        

        

