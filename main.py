import pygame

from os import listdir
from random import randint
from sys import exit
from math import sin

from scripts.constants import *
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

from scripts.data.util import Util

from scripts.utils.music_engine import Music_framework


class Menu:
    def __init__(self):
        super().__init__()
        # Click do mouse
        self.click = False

        # Controle dos laços de repetição
        self.show_menu = False
        self.show_difficulty_menu = False
        self.show_loja_menu = False
        self.show_opcoes_menu = False
        self.show_creditos_menu = False

        # Background
        self.menu_background_sprite = pygame.sprite.Sprite()
        self.menu_background_sprite.image = pygame.image.load(MENU_IMAGE_BACKGROUND)
        self.menu_background_sprite.image = pygame.transform.scale(self.menu_background_sprite.image,
                                                                   (SCREEN_X, SCREEN_Y))
        self.menu_background_sprite.rect = self.menu_background_sprite.image.get_rect()
        self.menu_background = pygame.sprite.GroupSingle(self.menu_background_sprite)

    def menu(self):
        button_list = []
        cursor_point = None
        self.show_menu = True

        while self.show_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        cursor_point = self.cursor_event(button_list, cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.click = True

                    if event.key == pygame.K_F1:
                        music_framework = Music_framework(screen, clock)
                        music_framework.run()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Background
            self.menu_background.draw(screen)

            # Título do jogo
            draw_text("SPACE", LOGO_FONT, YELLOW, SCREEN_X / 2, 100)
            draw_text("BATTLE", LOGO_FONT, YELLOW, SCREEN_X / 2, 160)

            # Botões do menu
            jogar_button = draw_button(SCREEN_X / 2 - 120, 250, SCREEN_X / 2 - 50, 50, "JOGAR")
            loja_button = draw_button(SCREEN_X / 2 - 120, 310, SCREEN_X / 2 - 50, 50, "LOJA")
            opcoes_button = draw_button(SCREEN_X / 2 - 120, 370, SCREEN_X / 2 - 50, 50, "OPÇÕES")
            creditos_button = draw_button(SCREEN_X / 2 - 120, 430, SCREEN_X / 2 - 50, 50, "CRÉDITOS")
            sair_button = draw_button(SCREEN_X / 2 - 120, 490, SCREEN_X / 2 - 50, 50, "SAIR")

            button_list = [jogar_button, loja_button, opcoes_button, creditos_button, sair_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if jogar_button.collidepoint((mx, my)) or cursor_point == jogar_button:
                if cursor_point != jogar_button:
                    pygame.mixer.Sound.play(SELECT_SOUND)
                cursor_point = jogar_button
                if self.click:
                    self.click = False
                    self.show_menu = False
                    self.difficulty_menu()

            if loja_button.collidepoint((mx, my)) or cursor_point == loja_button:
                if cursor_point != loja_button:
                    pygame.mixer.Sound.play(SELECT_SOUND)
                cursor_point = loja_button
                if self.click:
                    self.click = False
                    self.loja_menu()

            if opcoes_button.collidepoint((mx, my)) or cursor_point == opcoes_button:
                if cursor_point != opcoes_button:
                    pygame.mixer.Sound.play(SELECT_SOUND)
                cursor_point = opcoes_button
                if self.click:
                    self.click = False
                    self.opcoes_menu()

            if creditos_button.collidepoint((mx, my)) or cursor_point == creditos_button:
                if cursor_point != creditos_button:
                    pygame.mixer.Sound.play(SELECT_SOUND)
                cursor_point = creditos_button
                if self.click:
                    self.click = False
                    self.credios_menu()

            if sair_button.collidepoint((mx, my)) or cursor_point == sair_button:
                if cursor_point != sair_button:
                    pygame.mixer.Sound.play(SELECT_SOUND)
                cursor_point = sair_button
                if self.click:
                    self.show_menu = False
                    pygame.quit()
                    exit()

            # Depois de checar os inputs o click volta a ser falso
            self.click = False

            try:
                draw_cursor(cursor_point)
            except:
                cursor_point = jogar_button

            screen_update()

    def difficulty_menu(self):
        button_list = []
        cursor_point = None
        self.show_difficulty_menu = True

        while self.show_difficulty_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        cursor_point = self.cursor_event(button_list, cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Título
            draw_text("Dificuldade", TITLE_FONT, WHITE, SCREEN_X / 2, 80)

            # Botões
            normal_button = draw_button(SCREEN_X / 2 - 120, 250, SCREEN_X / 2 - 50, 50, "Normal")
            dificil_button = draw_button(SCREEN_X / 2 - 120, 310, SCREEN_X / 2 - 50, 50, "Difícil")
            insano_button = draw_button(SCREEN_X / 2 - 120, 370, SCREEN_X / 2 - 50, 50, "Insano")

            button_list = [normal_button, dificil_button, insano_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if normal_button.collidepoint((mx, my)) or cursor_point == normal_button:
                cursor_point = normal_button
                if self.click:
                    self.click = False

                    self.show_difficulty_menu = False
                    game.new_game(1)

            if dificil_button.collidepoint((mx, my)) or cursor_point == dificil_button:
                cursor_point = dificil_button
                if self.click:
                    self.click = False

                    self.show_difficulty_menu = False
                    game.new_game(2)

            if insano_button.collidepoint((mx, my)) or cursor_point == insano_button:
                cursor_point = insano_button
                if self.click:
                    self.click = False

                    self.show_difficulty_menu = False
                    game.new_game(3)

            # Depois de checar os inputs o click volta a ser falso
            self.click = False

            try:
                draw_cursor(cursor_point)
            except:
                cursor_point = normal_button

            screen_update()

    def loja_menu(self):
        self.show_loja_menu = True
        while self.show_loja_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_loja_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_loja_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("LOJA", TITLE_FONT, WHITE, SCREEN_X / 2, 80)
            draw_text(f"Coins: {util.get_coins()}", 14, WHITE, 70, 150, topleft=True)

            spaceship_1_attributes = util.get_spaceships("spaceship-1")
            spaceship_2_attributes = util.get_spaceships("spaceship-2")
            spaceship_3_attributes = util.get_spaceships("spaceship-3")

            ship_1_button = draw_loja_button("spaceship-1.png", 70, 180, 440, 120, "Violet Rocket",
                                             spaceship_1_attributes["price"],
                                             spaceship_1_attributes["lives"],
                                             spaceship_1_attributes["shield"],
                                             spaceship_1_attributes["damage"],
                                             spaceship_1_attributes["velocity"],
                                             spaceship_1_attributes["shoot_delay"])

            ship_2_button = draw_loja_button("spaceship-2.png", 70, 330, 440, 120, "Nave teste",
                                             spaceship_2_attributes["price"],
                                             spaceship_2_attributes["lives"],
                                             spaceship_2_attributes["shield"],
                                             spaceship_2_attributes["damage"],
                                             spaceship_2_attributes["velocity"],
                                             spaceship_2_attributes["shoot_delay"])

            ship_3_button = draw_loja_button("nave_teste.png", 70, 480, 440, 120, "Nave teste",
                                             spaceship_3_attributes["price"],
                                             spaceship_3_attributes["lives"],
                                             spaceship_3_attributes["shield"],
                                             spaceship_3_attributes["damage"],
                                             spaceship_3_attributes["velocity"],
                                             spaceship_3_attributes["shoot_delay"])

            back_to_menu_button = draw_button(30, 670, 100, 30, "Voltar", font_size=14)

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_loja_menu = False

            if ship_1_button.collidepoint((mx, my)):
                if self.click:
                    if "spaceship-1" in util.get_purchased_ships():
                        util.set_spaceship("spaceship-1")

            if ship_2_button.collidepoint((mx, my)):
                if self.click:
                    if "spaceship-2" in util.get_purchased_ships():
                        util.set_spaceship("spaceship-2")
                    elif util.get_coins() >= spaceship_2_attributes["price"]:
                        util.set_coins(util.get_coins() - spaceship_2_attributes["price"])
                        util.set_purchased_ships("spaceship-2")

            if ship_3_button.collidepoint((mx, my)):
                if self.click:
                    if "spaceship-3" in util.get_purchased_ships():
                        util.set_spaceship("spaceship-3")

            self.click = False

            screen_update()

    def opcoes_menu(self):
        self.show_opcoes_menu = True
        while self.show_opcoes_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_opcoes_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_opcoes_menu = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("OPÇÕES", TITLE_FONT, WHITE, SCREEN_X / 2, 80)

            sons_button = draw_button(SCREEN_X / 2 - 150, 250, SCREEN_X / 2 + 10, 50, "SONS")
            acessibilidade_button = draw_button(SCREEN_X / 2 - 150, 320, SCREEN_X / 2 + 10, 50,
                                                "ACESSIBILIDADE PARA DALTÔNICOS", font_size=9)

            back_to_menu_button = draw_button(30, 670, 100, 30, "Voltar", font_size=14)

            mx, my = pygame.mouse.get_pos()

            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_opcoes_menu = False
            if sons_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.sons_options()

            self.click = False

            screen_update()

    def credios_menu(self):
        self.show_creditos_menu = True
        while self.show_creditos_menu:
            clock.tick(FPS)
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
                        self.click = True

            draw_text("CRÉDITOS", TITLE_FONT, WHITE, SCREEN_X / 2, 80)

            draw_text("DESENVOLVEDORES:", SUB_TITLE_FONT, WHITE, 40, 170, topleft=True)
            draw_text("LUCAS EDUARDO KREUCH", SMALL_FONT, WHITE, 100, 220, topleft=True)
            draw_text("MARIA CLARA DE SOUZA", SMALL_FONT, WHITE, 100, 240, topleft=True)
            draw_text("ALINE AMARAL DE SOUZA", SMALL_FONT, WHITE, 100, 260, topleft=True)
            draw_text("HAIDY JANDRE", SMALL_FONT, WHITE, 100, 280, topleft=True)

            draw_text("PROFESSORES:", SUB_TITLE_FONT, WHITE, 40, 370, topleft=True)
            draw_text("RICARDO DE LA ROCHA LADEIRA", SMALL_FONT, WHITE, 100, 420, topleft=True)
            draw_text("LUIZ RICARDO URIARTE", SMALL_FONT, WHITE, 100, 440, topleft=True)

            back_to_menu_button = draw_button(30, 670, 100, 30, "Voltar", font_size=14)

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_creditos_menu = False

            self.click = False

            screen_update()

    def sons_options(self):
        self.show_options_sons_menu = True
        while self.show_options_sons_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_options_sons_menu = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_options_sons_menu = False

            min_line_sound = (SCREEN_X - 425, 300)
            max_line_sound = (SCREEN_X - 150, 300)

            draw_text("SONS", TITLE_FONT, WHITE, SCREEN_X / 2, 80)

            pygame.draw.line(screen, WHITE, min_line_sound, max_line_sound, 2)

            pygame.draw.line(screen, RED, (SCREEN_X / 2, 0), (SCREEN_X / 2, SCREEN_Y), 1)
            pygame.draw.line(screen, GREEN, (SCREEN_X - 425, 315), (SCREEN_X / 2, 315), 1)
            pygame.draw.line(screen, GREEN, (SCREEN_X / 2, 315), (SCREEN_X - 150, 315), 1)

            screen_update()

    @staticmethod
    def cursor_event(button_list, cursor_point, button):
        pygame.mixer.Sound.play(SELECT_SOUND)
        if button == pygame.K_UP:
            if button_list.index(cursor_point) >= 0:
                return button_list[button_list.index(cursor_point) - 1]
        if button == pygame.K_DOWN:
            if button_list.index(cursor_point) < len(button_list) - 1:
                return button_list[button_list.index(cursor_point) + 1]


class Game:
    def __init__(self):
        super().__init__()
        # Controle dos laços de repetição
        self.game_over = False
        self.show_pause = False
        self.show_game_over_screen = False
        self.draw_dev_options = False
        self.ready = False

        # Click do mouse
        self.click = False

    # Cria um novo jogo
    def new_game(self, difficulty):
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
        pygame.mixer.music.load(path.join(getcwd() + f"/assets/music/{util.get_music()}"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        # Background do jogo - A SPRITE COM MOVIMENTO PRECISA TER 580x2722 !!!!
        self.game_background_rect = Background(GAME_IMAGE_BACKGROUND)
        self.background = pygame.sprite.GroupSingle(self.game_background_rect)

        # Player
        self.player = Player(util.get_spaceship(), util.spaceship_attributes(), self.bullet_group)
        self.player_group_single = pygame.sprite.GroupSingle(self.player)
        # Imagem do player que serve como contador de vidas
        self.player_mini_image = pygame.transform.scale(self.player.image, (MINI_PLAYER_IMG, MINI_PLAYER_IMG))

        # Asteroid
        self.asteroid_sprite_sheet = self.create_sprite_sheet(ASTEROID_IMAGE_DIR, ASTEROID_SIZE_X, ASTEROID_SIZE_Y)

        # Explosion
        self.explosion_sprite_sheet = self.create_sprite_sheet(EXPLOSION_IMAGE_DIR, EXPLOSION_WIDTH, EXPLOSION_HEIGHT)

        # Enemy
        self.enemy_1_sprite_sheet = self.create_sprite_sheet(ENEMY_IMAGE_DIR, ENEMY_SIZE_X, ENEMY_SIZE_Y)
        self.create_enemy_delay = 2500
        self.last_enemy = pygame.time.get_ticks()

        # Kamikaze
        self.kamikaze_sprite_sheet = self.create_sprite_sheet(KAMIKADE_IMAGE_DIR, ENEMY_SIZE_X, ENEMY_SIZE_Y)
        self.create_kamikaze_delay = 7000
        self.last_kemikaze = pygame.time.get_ticks()

        # Shield bar
        self.player_shield_bar = Player_shield_bar(screen)
        self.enemy_shield_bar = Enemy_shield_bar(screen)
        self.kamikaze_shield_bar = Enemy_shield_bar(screen)
        self.boss_wings_shield_bar = Enemy_shield_bar(screen)
        self.boss_body_shield_bar = Enemy_shield_bar(screen)

        # Boss
        self.boss_body_sprite_sheet = self.create_sprite_sheet(BOSS_BODY_IMAGE_DIR, BODY_BOSS_SIZE_X, BODY_BOSS_SIZE_Y)
        self.boss_wing_sprite_sheet = self.create_sprite_sheet(BOSS_WING_IMAGE_DIR, WING_BOSS_SIZE_X, WING_BOSS_SIZE_Y)
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
        self.difficulty = difficulty
        if self.difficulty == 1:
            self.create_enemy_delay_multiplier = 0
            self.enemy_shoot_delay_multiplier = 0

        if self.difficulty == 2:
            self.create_enemy_delay_multiplier = self.create_enemy_delay / 2
            self.enemy_shoot_delay_multiplier = ENEMY_SHOOT_DELAY / 8

        if self.difficulty == 3:
            self.create_enemy_delay_multiplier = self.create_enemy_delay / 1.8
            self.enemy_shoot_delay_multiplier = ENEMY_SHOOT_DELAY / 6

            self.player.lives = 1

        # Roda o jogo
        self.game_over = False
        self.running()

    # Loop principal do jogo
    def running(self):
        #  Loop principal do jogo
        while not self.game_over:
            clock.tick(FPS)
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
                self.dev_options()

            self.update_sprites()
            self.draw()

    # Função principal de renderização
    def draw(self):
        screen.fill(BLACK)

        self.draw_groups()

        draw_text(f"Score: {self.score.get_score()}", 18, WHITE, SCREEN_X / 2, 16)  # Texto do score

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
            for wing in self.boss_wings_group:
                if wing.rect.x < SCREEN_X / 2:
                    margin = -40
                    pos_x_add = 25
                if wing.rect.x > SCREEN_X / 2:
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

                if event.key == pygame.K_F3:
                    if not self.draw_dev_options:
                        self.draw_dev_options = True
                    else:
                        self.draw_dev_options = False

    # Checa as colisões do jogo
    def collision_checks(self):
        # Colissão do tiro do Player com o Asteroide
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
                self.player.shield -= ASTEROID_DAMAGE
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
            collision = pygame.sprite.groupcollide(self.enemy_group, self.asteroid_group, True, True, pygame.sprite.collide_mask)
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
            collision = pygame.sprite.groupcollide(self.kamikaze_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
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
                self.player.shield -= PLAYER_COLLIDE_DAMAGE
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.explosion_group.add(explosion)
                hit.kill()

        # ---------- Colisões com o Boss ---------- #

        # Colisão do tiro do Player com a Asa do Boss
        def player_bullet_collision_with_boss_wing():
            collision = pygame.sprite.groupcollide(self.boss_wings_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
            for wing_hit in collision:
                wing_hit.shield -= self.player.damage * 1
                if wing_hit.shield <= 0:
                    self.score.add_score(20)
                    self.wing_explosion = True
                    wing_hit.kill()

        # Colisão do tiro do Player com o corpo do Boss
        def collision_of_the_player_bullet_with_the_boss_body():
            collision = pygame.sprite.groupcollide(self.boss_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
            if self.draw_body_boss_shield_bar:
                for body_hit in collision:
                    body_hit.shield -= self.player.damage * 1
                    if body_hit.shield <= 0:
                        self.score.add_score(50)
                        self.body_explosion = True
                        body_hit.kill()

        # Colisão do Player com o Boss
        def player_collision_with_boss():
            player_collision_boss = pygame.sprite.spritecollide(self.player, self.boss_group, False, pygame.sprite.collide_mask)
            if player_collision_boss:
                self.player.shield = 0

        # Colisão do Player com as asas do Boss
        def player_collision_with_Boss_wings():
            collision = pygame.sprite.spritecollide(self.player, self.boss_wings_group, False, pygame.sprite.collide_mask)
            if collision:
                self.player.shield = 0

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

            # Boss
            player_bullet_collision_with_boss_wing()
            collision_of_the_player_bullet_with_the_boss_body()
            player_collision_with_boss()
            player_collision_with_Boss_wings()


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

    # Tela de pause
    def pause_screen(self):
        button_list = []
        cursor_point = None
        self.show_pause = True

        while self.show_pause:
            clock.tick(FPS)
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
                            cursor_point = menu.cursor_event(button_list, cursor_point, event.key)

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Título
            draw_text("PAUSE", TITLE_FONT, WHITE, SCREEN_X / 2, 100)

            # Botões
            voltar_ao_jogo_button = draw_button(SCREEN_X / 2 - 150, 250, SCREEN_X / 2 + 10, 50, "VOLTAR AO JOGO")
            voltar_ao_menu_button = draw_button(SCREEN_X / 2 - 150, 310, SCREEN_X / 2 + 10, 50, "VOLTAR AO MENU")
            sair_do_jogo_button = draw_button(SCREEN_X / 2 - 150, 370, SCREEN_X / 2 + 10, 50, "SAIR DO JOGO")

            button_list = [voltar_ao_jogo_button, voltar_ao_menu_button, sair_do_jogo_button]
            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if voltar_ao_jogo_button.collidepoint((mx, my)) or cursor_point == voltar_ao_jogo_button:
                cursor_point = voltar_ao_jogo_button
                if self.click:
                    self.click = False

                    self.show_pause = False
                    pygame.mixer.music.unpause()

            if voltar_ao_menu_button.collidepoint((mx, my)) or cursor_point == voltar_ao_menu_button:
                cursor_point = voltar_ao_menu_button
                if self.click:
                    self.click = False

                    self.show_pause = False
                    self.game_over = True
                    pygame.mixer.music.stop()
                    menu.menu()

            if sair_do_jogo_button.collidepoint((mx, my)) or cursor_point == sair_do_jogo_button:
                cursor_point = sair_do_jogo_button
                if self.click:
                    self.click = False

                    self.show_pause = False
                    self.game_over = True
                    pygame.quit()
                    exit()

            try:
                draw_cursor(cursor_point)
            except:
                cursor_point = voltar_ao_jogo_button

            # Depois de checar os inputs o click fica falso
            self.click = False

            screen_update()

    # Tela de game over
    def game_over_screen(self):
        self.show_game_over_screen = True
        button_list = []
        cursor_point = None

        while self.show_game_over_screen:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        cursor_point = menu.cursor_event(button_list, cursor_point, "UP")

                    if event.key == pygame.K_DOWN:
                        cursor_point = menu.cursor_event(button_list, cursor_point, "DOWN")

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            draw_text("GAME OVER", 42, RED, SCREEN_X / 2, 60)
            draw_text(f"SCORE: {self.score.get_score()}", 42, WHITE, SCREEN_X / 2, SCREEN_Y / 2 - 124)

            voltar_ao_menu_buttom = draw_button(SCREEN_X / 2 - 150, 300, SCREEN_X / 2 + 10, 50, "Voltar ao menu")
            jogar_novamente_button = draw_button(SCREEN_X / 2 - 150, 360, SCREEN_X / 2 + 10, 50, "Jogar novamente",
                                                 font_size=19)

            button_list = [voltar_ao_menu_buttom, jogar_novamente_button]

            mx, my = pygame.mouse.get_pos()

            if voltar_ao_menu_buttom.collidepoint((mx, my)) or cursor_point == voltar_ao_menu_buttom:
                cursor_point = voltar_ao_menu_buttom
                if self.click:
                    self.click = False

                    self.show_game_over_screen = False
                    menu.menu()

            if jogar_novamente_button.collidepoint((mx, my)) or cursor_point == jogar_novamente_button:
                cursor_point = jogar_novamente_button
                if self.click:
                    self.click = False

                    self.show_game_over_screen = False
                    self.new_game(self.difficulty)

            self.click = False

            try:
                draw_cursor(cursor_point)
            except:
                cursor_point = voltar_ao_menu_buttom

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
        if pygame.time.get_ticks() - self.asteroid_shower_time > ASTEROID_SHOWER_COOLDOWN_TIME or self.asteroid_shower_event:
            self.asteroid_shower_time = pygame.time.get_ticks()

            if randint(0, 100) >= 80 and not self.asteroid_shower_event:
                self.asteroid_cooldown = pygame.time.get_ticks()
                self.asteroid_event_cooldown = pygame.time.get_ticks()

                self.asteroid_shower_event = True

            if self.asteroid_shower_event:
                if pygame.time.get_ticks() - self.asteroid_cooldown > ASTEROID_COOLDOWN:
                    self.asteroid_cooldown = pygame.time.get_ticks()
                    self.new_asteroid()

                if pygame.time.get_ticks() - self.asteroid_event_cooldown > ASTEROID_EVENT_COOLDOWN:
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
        pos_x = randint(0 + ENEMY_SIZE_X / 2, SCREEN_X - (ENEMY_SIZE_X * 3) + ENEMY_SIZE_X / 2)
        pos_y = -20
        distance_x = ENEMY_SIZE_X
        distance_y = 20
        for i in range(3):
            if i == 0:
                enemy = self.create_enemy(pos_x, pos_y)
            else:
                enemy = self.create_enemy(pos_x + distance_x, pos_y - distance_y)
                distance_x += ENEMY_SIZE_X
                distance_y -= 20
            self.enemy_group.add(enemy)

    # Novo inimigo solo
    def new_solo_enemy(self):
        pos_x = randint(ENEMY_SIZE_X / 2, SCREEN_X - (ENEMY_SIZE_X / 2))
        pos_y = -20
        enemy = self.create_enemy(pos_x, pos_y)
        self.enemy_group.add(enemy)

    # Novo kamikaze
    def new_kamikaze(self):
        kamikaze_1 = self.create_kemikaze(KAMIKAZE_X_POS_1, KAMIKAZE_SHIELD)
        kamikaze_2 = self.create_kemikaze(KAMIKAZE_X_POS_2, KAMIKAZE_SHIELD)
        self.kamikaze_group.add(kamikaze_1, kamikaze_2)

    # Gera o kamikaze
    def generate_kamikaze(self):
        if pygame.time.get_ticks() - self.last_kemikaze > self.create_kamikaze_delay:
            self.last_kemikaze = pygame.time.get_ticks()
            self.new_kamikaze()

    # Cria o inimigo
    def create_enemy(self, x, y):
        enemy = Enemy(x, y, ENEMY_SHIELD, ENEMY_DAMGE, self.enemy_1_sprite_sheet, self.enemy_shoot_group,
                      self.enemy_shoot_delay_multiplier)
        return enemy

    # Cria o kamikaze
    def create_kemikaze(self, x, shield):
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

            if self.body_explosion:
                self.body_explosion_event()
                self.boss_event = False

            if self.left_wing_destroyed and self.right_wing_destroyed:
                self.draw_body_boss_shield_bar = True

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
            image_rect.x = (SCREEN_X - 50) + (MINI_PLAYER_IMG + 10) * -i
            image_rect.y = 10
            screen.blit(image, image_rect)

    # Denha o texto de READY no início do jogo
    def draw_ready(self):
        if READY_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            draw_text("READY?", 42, YELLOW, SCREEN_X / 2, 100)
        if GO_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            draw_text("GO", 42, YELLOW, SCREEN_X / 2, 150)
        if pygame.time.get_ticks() - self.ready_time > 3000:
            self.ready = True

    # Opções de desenvolvedor
    @staticmethod
    def dev_options():
        draw_text(f"FPS: {clock.get_fps():.2f}", 12, RED, 20, 100, topleft=True)

    # Cria as sprite sheets de naves
    @staticmethod
    def create_sprite_sheet(sprite_directory, sprite_size_x, sprite_size_y):
        animation_list = []
        num_of_frames = len(listdir(sprite_directory))
        for i in range(1, num_of_frames):
            image = pygame.image.load(f"{sprite_directory}/sprite-{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(sprite_size_x), int(sprite_size_y)))
            animation_list.append(image)
        return animation_list


# -------------------------------------------------------- // -------------------------------------------------------- #


def screen_update():
    pygame.display.update()
    screen.fill(BLACK)


def draw_text(text, tam, color, x, y, topleft=False):
    fonte = pygame.font.Font(FONT_STYLE, tam)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    if topleft:
        text_rect.topleft = (x, y)
    else:
        text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def draw_button(left, top, width, height, text, font_size=20, color=(0, 0, 0)):
    button_border = pygame.Rect(int(left - 2), int(top - 2), int(width + 4), int(height + 4))
    button = pygame.Rect(int(left), int(top), int(width), int(height))
    pygame.draw.rect(screen, WHITE, button_border)
    pygame.draw.rect(screen, color, button)
    draw_text(text, font_size, WHITE, left + (width / 2), top + (height / 2))
    return button


def draw_loja_button(sprite, left, top, width, height, nome, price, lives, shield, damage, velocity, shoot_dedaly):
    button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
    button = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, WHITE, button_border)
    pygame.draw.rect(screen, BLACK, button)

    image = pygame.image.load(path.join(f"{IMAGE_DIR}/sprites/spaceships/{sprite}"))
    image = pygame.transform.scale(image, (75, 75))
    image_rect = image.get_rect()
    image_rect.center = (left + 60, top + (height / 2))
    screen.blit(image, image_rect)

    draw_text(nome, 16, YELLOW, left + 130, top + 10, topleft=True)  # Nome
    draw_text(f"Vidas: {lives}", 10, WHITE, left + 130, top + 35, topleft=True)  # Vidas
    draw_text(f"Escudo: {shield}", 10, WHITE, left + 130, top + 55, topleft=True)  # Escudo
    draw_text(f"Dano: {damage}", 10, WHITE, left + 270, top + 35, topleft=True)  # Dano
    draw_text(f"Velocidade: {velocity}", 10, WHITE, left + 270, top + 55, topleft=True)  # Velocidade
    draw_text(f"Shoot delay: {shoot_dedaly}", 10, WHITE, left + 270, top + 75, topleft=True)  # Shoot delay

    if util.get_spaceship() == sprite[:11]:
        draw_text("Equipado", 16, WHITE, left + 110, top + 100, topleft=True)
    else:
        if sprite[:11] in util.get_purchased_ships():
            draw_text("Disponível", 16, WHITE, left + 110, top + 100, topleft=True)
        else:
            draw_text(f"{price} Coins", 16, WHITE, left + 110, top + 100, topleft=True)

    return button


def draw_cursor(button, color=WHITE):
    draw_text("->", 16, color, button.left - 30, button.centery)
    draw_text("<-", 16, color, button.right + 30, button.centery)


# -------------------------------------------------------- // -------------------------------------------------------- #


if __name__ == '__main__':
    pygame.init()  # Inicializa o pygame
    pygame.mixer.init()  # Inicializa o modulo de mixer

    util = Util()
    menu = Menu()
    game = Game()

    # Tela do jogo
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Battle")

    # Ajuda a controlar a taxa de atualização do jogo — FPS
    clock = pygame.time.Clock()

    menu.menu()
