from os import listdir
from random import randint
from sys import exit

import pygame

from scripts.constantes import *
from scripts.asteroid import Asteroid
from scripts.background import Background
from scripts.enemy import Enemy
from scripts.explosion import Explosion
from scripts.player import Player
from scripts.score import Score


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
        self.mostrar_menu = True
        self.game_over = False
        self.mostrar_creditos = False
        self.mostrar_pause = False
        self.mostrar_game_over_screen = False
        self.mostrar_loja = False
        self.mostrar_opcoes = False

        # -- Cursores ---------------------------------------------
        self.cursor_rect = pygame.Rect(0, 0, 100, 100)
        self.cursor_point = "Jogar"
        self.pause_cursor_point = "Voltar ao jogo"
        self.loja_cusror_point = "Naves"

        # -- Background do menu -----------------------------------
        self.menu_background = pygame.sprite.Sprite()
        self.menu_background.image = pygame.image.load(path.join(getcwd() + "/assets/images/menu_background.png"))
        self.menu_background.image = pygame.transform.scale(self.menu_background.image, (SCREEN_X, SCREEN_Y))
        self.menu_background.rect = self.menu_background.image.get_rect()

        # -- Background do jogo -----------------------------------
        # !!!! A SPRITE COM MOVIMENTO PRECISA TER 580x2722
        self.game_background_rect = Background("game_background_preto.png")

    # Menu do jogo ----------------------------------------------------------------------------------------
    def menu(self):
        self.menu_background_group = pygame.sprite.Group()
        self.menu_background_group.add(self.menu_background)

        # Posição do cursor
        self.cursor_rect.x = 100
        self.cursor_rect.y = 300

        while self.mostrar_menu:
            self.clock.tick(FPS)

            self.menu_background_group.update()
            self.menu_background_group.draw(self.screen)

            self.draw_text("SPACE", 60, YELLOW, SCREEN_X / 2, 100)
            self.draw_text("BATTLE", 60, YELLOW, SCREEN_X / 2, 160)

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
                self.mostrar_menu = False
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if self.cursor_point == "Jogar":
                        self.new_game()
                        self.mostrar_menu = False
                    if self.cursor_point == "Loja":
                        self.mostrar_loja = True
                        self.loja()
                    if self.cursor_point == "Opções":
                        self.mostrar_opcoes = True
                        self.opcoes()
                    if self.cursor_point == "Créditos":
                        self.mostrar_creditos = True
                        self.credit_screen()
                    if self.cursor_point == "Sair":
                        self.mostrar_menu = False

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

        self.draw_cursor()

    # Desenha o cursor
    def draw_cursor(self):
        self.draw_text("->", 25, WHITE, self.cursor_rect.x, self.cursor_rect.y)

    # Novo jogo -------------------------------------------------------------------------------------------
    def new_game(self):
        # -- Sprite groups -------------------
        self.sprite_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        # -- Background
        self.sprite_group.add(self.game_background_rect)

        # -- Player -----------------------------------------------
        self.player = Player(self.sprite_group, self.bullet_group)
        self.sprite_group.add(self.player)
        # Imagem do player que serve como contador de vidas
        self.player_mini_image = pygame.transform.scale(self.player.image, (30, 30))

        # -- Asteroid ---------------------------------------------
        self.asteroid_sprite_sheet = self.create_sprite_sheet("asteroid", ASTEROID_SIZE_X, ASTEROID_SIZE_Y, "rotate")
        self.asteroid_sprite_sheet = self.asteroid_sprite_sheet[0]
        for i in range(0):
            self.new_asteroid()

        # -- Explosion --------------------------------------------
        self.explosion_sprite_sheet = self.create_sprite_sheet("explosion", 50, 50, "explosion-1")
        self.explosion_sprite_sheet = self.explosion_sprite_sheet[0]

        # -- Enemy ------------------------------------------------
        self.enemy_1_sprite_sheet = self.create_sprite_sheet("enemy_1", ENEMY_SIZE_X, ENEMY_SIZE_Y, "move")
        self.create_enemy_delay = 2500
        self.last_enemy = pygame.time.get_ticks()

        # -- Score ------------------------------------------------
        self.score = Score()

        # -- Controladores de tempo -------------------------------
        self.ready_time = pygame.time.get_ticks()

        # -- Roda o jogo -----------------------------------------
        self.game_over = False
        self.running()

    # Rodando ---------------------------------------------------------------------------------------------
    def running(self):
        #  Loop principal do jogo
        while not self.game_over:
            self.clock.tick(FPS)
            self.eventos()

            # Gera novos inimigos
            now = pygame.time.get_ticks()
            if now - self.last_enemy > self.create_enemy_delay:
                self.last_enemy = now
                self.new_tripe_enemy()

            # Colissão dos tiros com os asteroides
            self.bullet_asteroid_collide = pygame.sprite.groupcollide(self.asteroid_group, self.bullet_group, True, True, pygame.sprite.collide_circle)
            for hit in self.bullet_asteroid_collide:
                self.score += 1
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(explosion)
                self.new_asteroid()

            # Colisão da nave com os asteroides
            self.player_asteroid_collide = pygame.sprite.spritecollide(self.player, self.asteroid_group, True, pygame.sprite.collide_mask)
            for hit in self.player_asteroid_collide:
                self.player.shield -= 20 # Tira o shield do player
                self.new_asteroid() # Cria um novo asteroide
                if self.player.shield <= 0:
                    self.death_explosion = Explosion(self.player.rect.center, self.explosion_sprite_sheet)
                    self.sprite_group.add(self.death_explosion)
                    self.player.hide() # Esconde o player temporariamete
                    self.player.lives -= 1 # Tira uma vida do player
                    self.player.shield = 100 # O shield do jogador volta a ser 100

            # Colisão entre a nave inimiga e o asteroide
            self.enemy_asteroid_collide = pygame.sprite.groupcollide(self.enemy_group, self.asteroid_group, True, True, pygame.sprite.collide_mask)
            for hit in self.enemy_asteroid_collide:
                self.new_asteroid()
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(explosion)

            # Colissão entre o tiro e o inimigo
            #self.bullet_enemy_collide = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
            '''for hit in self.bullet_enemy_collide:
                self.score += 1
                #explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                #self.sprite_group.add(explosion)'''

            # Verifica se o player ainda tem vidas
            if self.player.lives == 0 and not self.death_explosion.alive():
                self.game_over = True
                self.mostrar_game_over_screen = True
                self.game_over_screen()


            self.update_sprites()
            self.draw_sprites()

    # Eventos do jogo -------------------------------------------------------------------------------------
    def eventos(self):
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.mostrar_pause = True
                    self.pause_screen()

    # Atualiza as sprites ---------------------------------------------------------------------------------
    def update_sprites(self):
        self.sprite_group.update()
        pygame.display.update()

    # Tela de game over
    def game_over_screen(self):
        while self.mostrar_game_over_screen:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mostrar_game_over_screen = False
                        self.mostrar_menu = True
                        self.menu()
            
            self.draw_text("GAME OVER", LARGE_FONT_SIZE, RED, SCREEN_X / 2, 60)
            self.draw_text(f"SCORE: {self.score}", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y / 2 - 32)
            self.draw_text("PRESSIONE 'SPACE' PARA VOLTAR AO MENU", SMALL_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y - 100)

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)
    
    # Loja do jogo
    def loja(self):
        self.cursor_rect.x = 150
        self.cursor_rect.y = SCREEN_Y / 2

        while self.mostrar_loja:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        # O cursor volta a ter a posição do cursor do menu
                        self.cursor_rect.x = 100
                        self.cursor_rect.y = 350
                        self.mostrar_loja = False
                    
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        if self.loja_cusror_point == "Naves":
                            pass
                        if self.loja_cusror_point == "Skins":
                            pass
                    
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.loja_cusror_point == "Skins":
                            self.loja_cusror_point = "Naves"
                            self.cursor_rect.y = SCREEN_Y / 2

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.loja_cusror_point == "Naves":
                            self.loja_cusror_point = "Skins"
                            self.cursor_rect.y = SCREEN_Y / 2 + 32

            self.draw_text("LOJA", LARGE_FONT_SIZE, WHITE, SCREEN_X / 2, 60)
            self.draw_text("NAVES", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y / 2)
            self.draw_text("SKINS", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y / 2 + 32)

            self.draw_cursor()

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)

    # Opções
    def opcoes(self):
        while self.mostrar_opcoes:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                        self.mostrar_opcoes = False

            self.draw_text("OPÇÕES", LARGE_FONT_SIZE, WHITE, SCREEN_X / 2, 60)

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)

    # Função para criar um novo asteroide
    def new_asteroid(self):
        m = Asteroid(self.asteroid_sprite_sheet)
        self.sprite_group.add(m)
        self.asteroid_group.add(m)
    
    # Função para criar inimigos
    def new_tripe_enemy(self):
        pos_x = randint(0 + ENEMY_SIZE_X / 2, SCREEN_X - (ENEMY_SIZE_X*3) + ENEMY_SIZE_X / 2)
        pos_y = -20
        distance_x = ENEMY_SIZE_X
        distance_y = 20
        for i in range(3):
            if i == 0:
                enemy = Enemy(pos_x, pos_y, ENEMY_1_SHIELD, self.enemy_1_sprite_sheet, self.bullet_group, self.sprite_group, self.explosion_sprite_sheet, self.score)
            else:
                enemy = Enemy(pos_x + distance_x, pos_y - distance_y, ENEMY_1_SHIELD, self.enemy_1_sprite_sheet, self.bullet_group, self.sprite_group, self.explosion_sprite_sheet, self.score)
                distance_x += ENEMY_SIZE_X
                distance_y -= 20
            self.sprite_group.add(enemy)
            self.enemy_group.add(enemy)
            #self.draw_enemy_shield_bar(self.screen, enemy.rect.x, enemy.rect.y, enemy.shield, enemy.vel_y)

    
    '''
    # Desenha a barra do escudo do enemy
    def draw_enemy_shield_bar(self, surface, x, y, enemy_shield, vel_y):
        if enemy_shield < 0:
            enemy_shield = 0
        fill = (enemy_shield / 100) * ENEMY_BAR_WIDTH
        fill_rect = pygame.Rect(x, y, fill, ENEMY_BAR_HEIGHT)
        pygame.draw.rect(surface, GREEN, fill_rect)
    '''

    # Tela de créditos do menu ------------------------------------------------------------------------------
    def credit_screen(self):
        while self.mostrar_creditos:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mostrar_creditos = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE or pygame.K_ESCAPE:
                        self.mostrar_creditos = False

            self.draw_text("CRÉDITOS", 42, WHITE, SCREEN_X/2, 60)
            self.draw_text("LUCAS EDUARDO KREUCH", 28, WHITE, SCREEN_X/2, 150)
            self.draw_text("MARIA CLARA DE SOUZA", 28, WHITE, SCREEN_X/2, 180)
            self.draw_text("HAIDY JANDRE", 28, WHITE, SCREEN_X/2, 210)

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)

    # Tela de pause
    def pause_screen(self):
        # Posição do cursor
        self.cursor_rect.x = 60
        self.cursor_rect.y = VOLTAR_AO_JOGO_Y

        while self.mostrar_pause:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mostrar_pause = False
                    self.game_over = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if self.pause_cursor_point == "Voltar ao jogo":
                            self.mostrar_pause = False
                        if self.pause_cursor_point == "Voltar ao menu":
                            self.pause_cursor_point = "Voltar ao jogo"
                            self.mostrar_pause = False
                            self.game_over = True
                            self.mostrar_menu = True
                            self.menu()
                        if self.pause_cursor_point == "Sair do jogo":
                            exit()
                        if self.pause_cursor_point == "Opções":
                            pass

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.pause_cursor_point == "Voltar ao menu":
                            self.pause_cursor_point = "Voltar ao jogo"
                            self.cursor_rect.y = VOLTAR_AO_JOGO_Y
                        if self.pause_cursor_point == "Sair do jogo":
                            self.pause_cursor_point = "Voltar ao menu"
                            self.cursor_rect.y = VOLTAR_AO_MENU_Y
                        if self.pause_cursor_point == "Opções":
                            self.pause_cursor_point = "Sair do jogo"
                            self.cursor_rect.y = SAIR_DO_JOGO_Y

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.pause_cursor_point == "Sair do jogo":
                            self.pause_cursor_point = "Opções"
                            self.cursor_rect.y = OPCOES_Y
                        if self.pause_cursor_point == "Voltar ao menu":
                            self.pause_cursor_point = "Sair do jogo"
                            self.cursor_rect.y = SAIR_DO_JOGO_Y
                        if self.pause_cursor_point == "Voltar ao jogo":
                            self.pause_cursor_point = "Voltar ao menu"
                            self.cursor_rect.y = VOLTAR_AO_MENU_Y
            
            self.draw_text("PAUSE", LARGE_FONT_SIZE, WHITE, SCREEN_X / 2, 200)        
            
            self.draw_text("VOLTAR AO JOGO", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, VOLTAR_AO_JOGO_Y)
            self.draw_text("VOLTAR AO MENU", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, VOLTAR_AO_MENU_Y)
            self.draw_text("SAIR DO JOGO", MEDIUM_FONT_SIZE, WHITE, SCREEN_X/2, SAIR_DO_JOGO_Y)
            self.draw_text("OPÇÕES", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, OPCOES_Y)

            self.draw_cursor()

            pygame.display.flip()
            pygame.display.update()
            self.screen.fill(BLACK)


    # Cria as sprite sheets de naves -----------------------------------------------------------------------
    @staticmethod
    def create_sprite_sheet(sprite, sprite_size_x, sprite_size_y, *animation_type):
        animation_list = []
        animation_types = animation_type

        for animation in animation_types:
            temp_list = []
            num_of_frames = len(listdir(f"assets/images/sprites/{sprite}/{animation}"))
            for i in range(1, num_of_frames):
                image = pygame.image.load(
                    path.join(getcwd() + f"/assets/images/sprites/{sprite}/{animation}/sprite-{i}.png"))
                image = pygame.transform.scale(image, (sprite_size_x, sprite_size_y))
                temp_list.append(image)
            animation_list.append(temp_list)
        return animation_list


    # !! ------------------------ DRAW ------------------------ !! #
    # Desenha a quantidade de vidas do jogador
    def draw_lives(self, surface, x, y, image):
        for i in range(self.player.lives):
            image_rect = image.get_rect()
            image_rect.x = x + 30 * i
            image_rect.y = y
            surface.blit(image, image_rect)

    # Denha o texto de READY no inicio do jogo
    def draw_ready(self):
        READY_DELAY = 1000
        GO_DELAY = 2000
        if READY_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            self.draw_text("READY?", LARGE_FONT_SIZE, YELLOW, SCREEN_X / 2, 100)
        if GO_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            self.draw_text("GO", LARGE_FONT_SIZE, YELLOW, SCREEN_X / 2, 150)

    # Desenha a barra do escudo do player
    def draw_shield_bar(self, surface, x, y):
        if self.player.shield < 0:
            self.player.shield = 0
        fill = (self.player.shield / 100) * BAR_WIDTH
        outline_rect = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surface, GREEN, fill_rect)
        pygame.draw.rect(surface, WHITE, outline_rect, 2)

    # Desenha o texto na tela
    def draw_text(self, text, tam, color, x, y):
        self.fonte = pygame.font.Font(FONTE, tam)
        self.text_obj = self.fonte.render(text, False, color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (x, y)
        self.screen.blit(self.text_obj, self.text_rect)

    # Desenha as sprites no jogo
    def draw_sprites(self):
        self.screen.fill(WHITE)
        self.sprite_group.draw(self.screen)

        # Texto/Draw
        self.draw_text(f"Score: {self.score.score}", 18, WHITE, SCREEN_X/2, 16) # Texto do score
        self.draw_shield_bar(self.screen, 5, 10)
        self.draw_lives(self.screen, 480, 10, self.player_mini_image)

        self.draw_ready()

        pygame.display.flip()