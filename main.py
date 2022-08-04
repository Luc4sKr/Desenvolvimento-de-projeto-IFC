import pygame

from os import listdir
from random import randint
from sys import exit

from scripts.constantes import *
from scripts.asteroid import Asteroid
from scripts.background import Background
from scripts.enemies import Enemy
from scripts.enemies import Kamikaze
from scripts.boss import Boss
from scripts.explosion import Explosion
from scripts.player import Player
from scripts.score import Score
from scripts.powerup import Powerup
from scripts.enemy_shield_bar import Shield_bar

from scripts.data.util import Util


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
        self.menu_background_sprite.image = pygame.image.load(path.join(getcwd() + "/assets/images/backgrounds/menu_background.png"))
        self.menu_background_sprite.image = pygame.transform.scale(self.menu_background_sprite.image, (SCREEN_X, SCREEN_Y))
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
                    if event.key == pygame.K_UP:
                        cursor_point = self.cursor_event(button_list, cursor_point, "UP")

                    if event.key == pygame.K_DOWN:
                        cursor_point = self.cursor_event(button_list, cursor_point, "DOWN")

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Background
            self.menu_background.draw(screen)

            # Título do jogo
            draw_text("SPACE", 60, YELLOW, SCREEN_X / 2, 100)
            draw_text("BATTLE", 60, YELLOW, SCREEN_X / 2, 160)

            # Botões do menu
            jogar_button = draw_button(SCREEN_X/2 - 120, 250, SCREEN_X/2 - 50, 50, "JOGAR")
            loja_button = draw_button(SCREEN_X/2 - 120, 310, SCREEN_X/2 - 50, 50, "LOJA")
            opcoes_button = draw_button(SCREEN_X/2 - 120, 370, SCREEN_X/2 - 50, 50, "OPÇÕES")
            creditos_button = draw_button(SCREEN_X/2 - 120, 430, SCREEN_X/2 - 50, 50, "CRÉDITOS")
            sair_button = draw_button(SCREEN_X/2 - 120, 490, SCREEN_X/2 - 50, 50, "SAIR")

            button_list = [jogar_button, loja_button, opcoes_button, creditos_button, sair_button]

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if jogar_button.collidepoint((mx, my)) or cursor_point == jogar_button:
                cursor_point = jogar_button
                if self.click:
                    self.click = False

                    self.show_menu = False
                    self.difficulty_menu()

            if loja_button.collidepoint((mx, my)) or cursor_point == loja_button:
                cursor_point = loja_button
                if self.click:
                    self.click = False

                    self.loja_menu()

            if opcoes_button.collidepoint((mx, my)) or cursor_point == opcoes_button:
                cursor_point = opcoes_button
                if self.click:
                    self.click = False

            if creditos_button.collidepoint((mx, my)) or cursor_point == creditos_button:
                cursor_point = creditos_button
                if self.click:
                    self.click = False

                    self.credios_menu()

            if sair_button.collidepoint((mx, my)) or cursor_point == sair_button:
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

            # Update na tela
            pygame.display.update()
            screen.fill(BLACK)


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
                    if event.key == pygame.K_UP:
                        cursor_point = self.cursor_event(button_list, cursor_point, "UP")

                    if event.key == pygame.K_DOWN:
                        cursor_point = self.cursor_event(button_list, cursor_point, "DOWN")

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Título
            draw_text("Dificuldade", 44, WHITE, SCREEN_X/2, 80)

            # Botões
            normal_button = draw_button(SCREEN_X/2 - 120, 250, SCREEN_X/2 - 50, 50, "Normal")
            dificil_button = draw_button(SCREEN_X/2 - 120, 310, SCREEN_X/2 - 50, 50, "Difícil")
            insano_button = draw_button(SCREEN_X/2 - 120, 370, SCREEN_X/2 - 50, 50, "Insano")

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

            # Update na tela
            pygame.display.update()
            screen.fill(BLACK)


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

            draw_text("LOJA", 44, WHITE, SCREEN_X / 2, 80)
            draw_text(f"Coins: {util.get_coins()}", 14, WHITE, 70, 150, topleft=True)

            nave_1_button = draw_loja_button("nave_teste.png", 70, 180, 440, 120, "Nave teste", 3, 100)
            nave_2_button = draw_loja_button("nave_teste.png", 70, 330, 440, 120, "Nave teste", 3, 100)
            nave_3_button = draw_loja_button("nave_teste.png", 70, 480, 440, 120, "Nave teste", 3, 100)

            back_to_menu_button = draw_button(30, 670, 100, 30, "Voltar", font_size=14)

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_loja_menu = False

            self.click = False

            pygame.display.update()
            screen.fill(BLACK)


    def opcoes_menu(self):
        self.show_opcoes_menu = True
        while self.show_opcoes_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_opcoes_menu = False
                    pygame.quit()
                    exit()


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

            draw_text("CRÉDITOS", 44, WHITE, SCREEN_X/2, 80)

            draw_text("DESENVOLVEDORES:", 22, WHITE, 40, 170, topleft=True)
            draw_text("LUCAS EDUARDO KREUCH", 14, WHITE, 100, 220, topleft=True)
            draw_text("MARIA CLARA DE SOUZA", 14, WHITE, 100, 240, topleft=True)
            draw_text("ALINE AMARAL DE SOUZA", 14, WHITE, 100, 260, topleft=True)
            draw_text("HAIDY JANDRE", 14, WHITE, 100, 280, topleft=True)

            draw_text("PROFESSORES:", 22, WHITE, 40, 370, topleft=True)
            draw_text("RICARDO DE LA ROCHA LADEIRA", 14, WHITE, 100, 420, topleft=True)
            draw_text("LUIZ RICARDO URIARTE", 14, WHITE, 100, 440, topleft=True)

            back_to_menu_button = draw_button(30, 670, 100, 30, "Voltar", font_size=14)

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Colisão com os botões
            if back_to_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_creditos_menu = False

            self.click = False

            # Update na tela
            pygame.display.update()
            screen.fill(BLACK)


    @staticmethod
    def cursor_event(button_list, cursor_point, type):
                if type == "UP":
                    if button_list.index(cursor_point) >= 0:
                        return button_list[button_list.index(cursor_point)-1]

                if type == "DOWN":
                    if button_list.index(cursor_point) < len(button_list)-1:
                       return button_list[button_list.index(cursor_point)+1]




class Game:
    def __init__(self):
        super().__init__()
        # Controle dos laços de repetição
        self.game_over = False
        self.show_pause = False
        self.show_game_over_screen = False
        self.draw_dev_options = False

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
        self.kamikaze_group = pygame.sprite.Group()

        # Background do jogo - A SPRITE COM MOVIMENTO PRECISA TER 580x2722 !!!!
        self.game_background_rect = Background("game_background_azul_cinza.png")
        self.background = pygame.sprite.GroupSingle(self.game_background_rect)

        # Player
        self.player = Player(util.get_spaceship(), util.spaceship_attributes(), self.bullet_group)
        self.player_group_single = pygame.sprite.GroupSingle(self.player)
        # Imagem do player que serve como contador de vidas
        self.player_mini_image = pygame.transform.scale(self.player.image, (35, 35))

        # Asteroid
        self.asteroid_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/asteroid", ASTEROID_SIZE_X, ASTEROID_SIZE_Y)

        # Explosion
        self.explosion_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/explosion/explosion-1", 50, 50)
        self.explosion_sprite_sheet = self.explosion_sprite_sheet

        # Enemy
        self.enemy_1_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/enemy-1", ENEMY_SIZE_X, ENEMY_SIZE_Y)
        self.create_enemy_delay = 2500
        self.last_enemy = pygame.time.get_ticks()

        # Kamikaze
        self.kamikaze_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/enemy-2", ENEMY_SIZE_X, ENEMY_SIZE_Y)
        self.create_kamikaze_delay = 7000
        self.last_kemikaze = pygame.time.get_ticks()

        # Shield bar
        self.enemy_shield_bar = Shield_bar(screen)
        self.kamikaze_shield_bar = Shield_bar(screen)
        self.boss_wings_shield_bar = Shield_bar(screen)

        # Boss
        self.boss_body_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/boss/body", BODY_BOSS_SIZE_X, BODY_BOSS_SIZE_Y)
        self.boss_wing_sprite_sheet = self.create_sprite_sheet("assets/images/sprites/boss/wings", WING_BOSS_SIZE_X, WING_BOSS_SIZE_Y)
        self.boss_event = False

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

    # Roda o jogo
    def running(self):
        #  Loop principal do jogo
        while not self.game_over:
            clock.tick(FPS)
            # Eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.show_pause = True
                        self.pause_screen()

                    if event.key == pygame.K_p:
                        self.asteroid_shower_event = True
                    
                    if event.key == pygame.K_i:
                        self.score.add_score(100)

                    if event.key == pygame.K_q:
                        self.boss = Boss(self.boss_body_sprite_sheet, self.boss_wing_sprite_sheet)
                        self.boss_group.add(self.boss)
                        self.boss_wings_group.add(self.boss.left_wing)
                        self.boss_wings_group.add(self.boss.right_wing)

                        self.draw_boss = True

                    if event.key == pygame.K_e:
                        kamikaze1 = Kamikaze(KAMIKAZE_XPOS_1, 4, self.kamikaze_sprite_sheet)
                        kamikaze2 = Kamikaze(KAMIKAZE_XPOS_2, 4, self.kamikaze_sprite_sheet)

                        self.kamikaze_group.add(kamikaze1)
                        self.kamikaze_group.add(kamikaze2)


                    if event.key == pygame.K_F3:
                        if not self.draw_dev_options:
                            self.draw_dev_options = True
                        else:
                            self.draw_dev_options = False

            self.collision_checks()

            
            if self.ready:
                self.asteroid_shower()

                if not self.asteroid_shower_event and not self.boss_event:
                    self.generate_enemy()
                    self.generate_kamikaze()

            self.fBoss_event()

            self.check_lives()
            self.check_shield()


            if self.draw_dev_options:
                self.dev_options()

            self.update_sprites()
            self.draw()

    # Desenha as sprites no jogo
    def draw(self):
        screen.fill(BLACK)

        self.draw_groups()

        draw_text(f"Score: {self.score.get_score()}", 18, WHITE, SCREEN_X / 2, 16)  # Texto do score

        self.draw_shield_bar(5, 10) # Shield do Player
        self.draw_lives(480, 10, self.player_mini_image) # Vidas do Player

        self.draw_ready()

        # Shield bar do enemy
        for enemy in self.enemy_group:
            self.enemy_shield_bar.draw_shield_bar(enemy.shield, enemy.rect)
        
        # Shield bar do kamikaze
        for kamikaze in self.kamikaze_group:
            self.kamikaze_shield_bar.draw_shield_bar(kamikaze.shield, kamikaze.rect)

        if self.boss_event:
            for wing in self.boss_wings_group:
                self.boss_wings_shield_bar.draw_shield_bar(wing.shield, wing.rect)


    def update_sprites(self):
        self.background.update()
        self.player_group_single.update()
        self.explosion_group.update()
        self.enemy_group.update()
        self.asteroid_group.update()
        self.bullet_group.update()
        self.enemy_shoot_group.update()
        self.powerup_group.update()
        self.kamikaze_group.update()

        if self.draw_boss:
            self.boss_group.update()
            self.boss_wings_group.update()

        pygame.display.update()


    def draw_groups(self):
        self.background.draw(screen)
        self.explosion_group.draw(screen)
        self.enemy_group.draw(screen)
        self.asteroid_group.draw(screen)
        self.bullet_group.draw(screen)
        self.enemy_shoot_group.draw(screen)
        self.powerup_group.draw(screen)
        self.player_group_single.draw(screen)
        self.kamikaze_group.draw(screen)

        if self.draw_boss:
            self.boss_group.draw(screen)
            self.boss_wings_group.draw(screen)

    # Checa as colisões do jogo
    def collision_checks(self):
        # Colissão dos tiros do Player com o Asteroid
        bullet_asteroid_collide = pygame.sprite.groupcollide(self.asteroid_group, self.bullet_group, True, True, pygame.sprite.collide_mask)
        for hit in bullet_asteroid_collide:
            self.score.add_score()
            explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
            self.explosion_group.add(explosion)

        # Colisão do Player com o Asteroid
        player_asteroid_collide = pygame.sprite.spritecollide(self.player, self.asteroid_group, True, pygame.sprite.collide_mask)
        for hit in player_asteroid_collide:
            self.player.shield -= ASTEROID_DAMAGE  # Tira o shield do player

        # Colisão do Enemy com o tiro do Player
        player_shot_collide = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
        for hit in player_shot_collide:
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

        # Colisão entre o Enemy e o Asteroid
        enemy_asteroid_collide = pygame.sprite.groupcollide(self.enemy_group, self.asteroid_group, True, True, pygame.sprite.collide_mask)
        for hit in enemy_asteroid_collide:
            explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
            self.explosion_group.add(explosion)

        # Colissão do Player com os Powerups
        powerup_collide = pygame.sprite.spritecollide(self.player, self.powerup_group, True)
        for hit in powerup_collide:
            if hit.type == "shield":
                self.player.shield += 20
                if self.player.shield >= 100:
                    self.player.shield = 100

            if hit.type == "gun":
                self.player.powerup()

        # Colisão dos tiros inimigos com o Player
        enemy_shoot_collision = pygame.sprite.spritecollide(self.player, self.enemy_shoot_group, True)
        for hit in enemy_shoot_collision:
            self.player.shield -= hit.damage

        
        # Colisão entre os tiros do Player com a Asa do Boss
        shoot_collision_wing = pygame.sprite.groupcollide(self.boss_wings_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
        for hit in shoot_collision_wing:
            hit.shield -= self.player.damage


    def check_lives(self):
        # Verifica se o player ainda tem vidas
        if self.player.lives == 0 and not self.death_explosion.alive(): # -- Teste -- and not self.death_explosion.alive() 
            self.game_over = True
            self.game_over_screen()


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

                    if event.key == pygame.K_UP:
                        cursor_point = menu.cursor_event(button_list, cursor_point, "UP")

                    if event.key == pygame.K_DOWN:
                        cursor_point = menu.cursor_event(button_list, cursor_point, "DOWN")

                    if event.key == pygame.K_RETURN:
                        self.click = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Título
            draw_text("PAUSE", 42, WHITE, SCREEN_X / 2, 100)

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

            if voltar_ao_menu_button.collidepoint((mx, my)) or cursor_point == voltar_ao_menu_button:
                cursor_point = voltar_ao_menu_button
                if self.click:
                    self.click = False

                    self.show_pause = False
                    self.game_over = True
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

            pygame.display.update()
            screen.fill(BLACK)

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

            voltar_ao_menu_buttom = draw_button(SCREEN_X/2 - 150, 300, SCREEN_X/2 + 10, 50, "Voltar ao menu")
            jogar_novamente_button = draw_button(SCREEN_X / 2 - 150, 360, SCREEN_X / 2 + 10, 50, "Jogar novamente", font_size=19)

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

            pygame.display.update()
            screen.fill(BLACK)

    # Função para criar um novo asteroide
    def new_asteroid(self):
        asteroid = Asteroid(self.asteroid_sprite_sheet)
        self.asteroid_group.add(asteroid)


    def asteroid_shower(self):
        if pygame.time.get_ticks() - self.asteroid_shower_time > ASTEROID_TIME or self.asteroid_shower_event:
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
        if pygame.time.get_ticks() - self.last_enemy > self.create_enemy_delay - self.create_enemy_delay_multiplier :
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


    def new_solo_enemy(self):
        pos_x = randint(ENEMY_SIZE_X / 2, SCREEN_X - (ENEMY_SIZE_X / 2))
        pos_y = -20
        enemy = self.create_enemy(pos_x, pos_y)
        self.enemy_group.add(enemy)


    def new_kamikaze(self):
        kamikaze_1 = self.create_kemikaze(KAMIKAZE_XPOS_1, KAMIKAZE_SHIELD)
        kamikaze_2 = self.create_kemikaze(KAMIKAZE_XPOS_2, KAMIKAZE_SHIELD)
        self.kamikaze_group.add(kamikaze_1, kamikaze_2)

    
    def generate_kamikaze(self):
        if pygame.time.get_ticks() - self.last_kemikaze > self.create_kamikaze_delay:
            self.last_kemikaze = pygame.time.get_ticks()
            self.new_kamikaze()


    def create_enemy(self, x, y):
        enemy = Enemy(x, y, ENEMY_1_SHIELD, self.enemy_1_sprite_sheet, self.enemy_shoot_group, self.enemy_shoot_delay_multiplier)
        return enemy

    
    def create_kemikaze(self, x, shield):
        kamikaze = Kamikaze(x, shield, self.kamikaze_sprite_sheet)
        return kamikaze


    def fBoss_event(self):
        if self.score.get_score() >= 100 and not self.boss_event:
            self.boss_event = True
            boss = Boss(self.boss_body_sprite_sheet, self.boss_wing_sprite_sheet)
            self.boss_group.add(boss)
            self.boss_wings_group.add(boss.left_wing)
            self.boss_wings_group.add(boss.right_wing)
            self.draw_boss = True      


    def dev_options(self):
        draw_text(f"FPS: {clock.get_fps():.2f}", 12, RED, 20, 100, topleft=True)
        


    
    @staticmethod # Cria as sprite sheets de naves
    def create_sprite_sheet(sprite_directory, sprite_size_x, sprite_size_y):
        animation_list = []

        num_of_frames = len(listdir(sprite_directory))
        for i in range(1, num_of_frames):
            image = pygame.image.load(path.join(getcwd() + f"/{sprite_directory}/sprite-{i}.png")).convert_alpha()
            image = pygame.transform.scale(image, (sprite_size_x, sprite_size_y))
            animation_list.append(image)
        return animation_list

    # Desenha a quantidade de vidas do jogador
    def draw_lives(self, x, y, image):
        for i in range(self.player.lives):
            image_rect = image.get_rect()
            image_rect.x = x + 30 * i
            image_rect.y = y
            screen.blit(image, image_rect)

    # Denha o texto de READY no inicio do jogo
    def draw_ready(self):
        READY_DELAY = 1000
        GO_DELAY = 2000
        if READY_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            draw_text("READY?", 42, YELLOW, SCREEN_X / 2, 100)
        if GO_DELAY < pygame.time.get_ticks() - self.ready_time < 3000:
            draw_text("GO", 42, YELLOW, SCREEN_X / 2, 150)
        if pygame.time.get_ticks() - self.ready_time > 3000:
            self.ready = True

    # Desenha a barra do escudo do player
    def draw_shield_bar(self, x, y):
        if self.player.shield < 0:
            self.player.shield = 0
        fill = (self.player.shield / 100) * BAR_WIDTH
        outline_rect = pygame.Rect(x, y, BAR_WIDTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, outline_rect, 2)





def draw_text(text, tam, color, x, y, topleft=False):
    fonte = pygame.font.Font(FONTE, tam)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    if topleft:
        text_rect.topleft = (x, y)
    else:
        text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)


def draw_button(left, top, width, height, text, font_size=20, color=(0, 0, 0)):
    button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
    button = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, WHITE, button_border)
    pygame.draw.rect(screen, color, button)
    draw_text(text, font_size, WHITE, left + (width / 2), top + (height / 2))
    return button


def draw_loja_button(sprite, left, top, width, height, nome, vidas, shield):
    button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
    button = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, WHITE, button_border)
    pygame.draw.rect(screen, BLACK, button)

    image = pygame.image.load(path.join(getcwd() + f"/assets/images/{sprite}"))
    image = pygame.transform.scale(image, (75, 75))
    image_rect = image.get_rect()
    image_rect.center = (left + 60, top + (height / 2))
    screen.blit(image, image_rect)

    draw_text(nome, 16, YELLOW, left + 130, top + 10, topleft=True)               # Nome
    draw_text(f"Vidas: {vidas}", 10, WHITE, left + 130, top + 35, topleft=True)   # Vidas
    draw_text(f"Escudo: {shield}", 10, WHITE, left + 130, top + 55, topleft=True) # Escudo
    return  button


def draw_cursor(button, color=WHITE):
    draw_text("->", 16, color, button.left - 30, button.centery)
    draw_text("<-", 16, color, button.right + 30, button.centery)






if __name__ == '__main__':
    pygame.init()  # Inicializa o pygame
    pygame.mixer.init()  # Inicializa o modulo de mixer

    util = Util()
    menu = Menu()
    game = Game()

    # Tela do jogo
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Battle")

    # Ajuda a controlar a taxa de atualização do jogo - FPS
    clock = pygame.time.Clock()

    menu.menu()
