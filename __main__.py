import pygame

from os import listdir
from random import randint
from sys import exit

from scripts.constantes import *
from scripts.asteroid import Asteroid
from scripts.background import Background
from scripts.enemy import Enemy
from scripts.explosion import Explosion
from scripts.player import Player
from scripts.score import Score
from scripts.powerup import Powerup
from scripts.enemy_shield_bar import Shield_bar


class Menu:
    def __init__(self):
        super().__init__()
        # Click do mouse
        self.click = False

        # Controle dos laços de repetição
        self.show_menu = False

        # Background
        self.menu_background_sprite = pygame.sprite.Sprite()
        self.menu_background_sprite.image = pygame.image.load(path.join(getcwd() + "/assets/images/menu_background.png"))
        self.menu_background_sprite.image = pygame.transform.scale(self.menu_background_sprite.image, (SCREEN_X, SCREEN_Y))
        self.menu_background_sprite.rect = self.menu_background_sprite.image.get_rect()
        self.menu_background = pygame.sprite.GroupSingle(self.menu_background_sprite)

    def menu(self):
        self.show_menu = True
        while self.show_menu:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = False
                    pygame.quit()
                    exit()

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

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if jogar_button.collidepoint((mx, my)):
                if self.click:
                    self.show_menu = False
                    game.new_game()

            if loja_button.collidepoint((mx, my)):
                if self.click:
                    pass
            if opcoes_button.collidepoint((mx, my)):
                if self.click:
                    pass
            if creditos_button.collidepoint((mx, my)):
                if self.click:
                    pass
            if sair_button.collidepoint((mx, my)):
                if self.click:
                    self.show_menu = False
                    pygame.quit()
                    exit()


            # Depois de checar os inputs o click volta a ser falso
            self.click = False

            # Update na tela
            pygame.display.flip()
            pygame.display.update()
            screen.fill(BLACK)


class Game:
    def __init__(self):
        super().__init__()
        # Controle dos laços de repetição
        self.game_over = False
        self.show_pause = False
        self.show_game_over_screen = False

        # Click do mouse
        self.click = False

        # Background do jogo - A SPRITE COM MOVIMENTO PRECISA TER 580x2722 !!!!
        self.game_background_rect = Background("game_background_azul_cinza.png")

    # Cria um novo jogo
    def new_game(self):
        # Sprite groups
        self.sprite_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.enemy_shoot_group = pygame.sprite.Group()

        # Background
        self.sprite_group.add(self.game_background_rect)

        # Player
        self.player = Player("spaceship_1.png", 100, 250, self.sprite_group, self.bullet_group)
        self.sprite_group.add(self.player)
        # Imagem do player que serve como contador de vidas
        self.player_mini_image = pygame.transform.scale(self.player.image, (30, 30))

        # Asteroid
        self.asteroid_sprite_sheet = self.create_sprite_sheet("asteroid", ASTEROID_SIZE_X, ASTEROID_SIZE_Y, "rotate")
        self.asteroid_sprite_sheet = self.asteroid_sprite_sheet[0]
        for i in range(0):
            self.new_asteroid()

        # Explosion
        self.explosion_sprite_sheet = self.create_sprite_sheet("explosion", 50, 50, "explosion-1")
        self.explosion_sprite_sheet = self.explosion_sprite_sheet[0]

        # Bullet explosion
        # self.bullet_explosion_sprite_sheet = self.create_sprite_sheet("explosion", 30, 30, "explosion-2")
        # self.bullet_explosion_sprite_sheet = self.bullet_explosion_sprite_sheet[0]

        # Enemy
        self.enemy_1_sprite_sheet = self.create_sprite_sheet("enemy_1", ENEMY_SIZE_X, ENEMY_SIZE_Y, "move")
        self.create_enemy_delay = 2500
        self.last_enemy = pygame.time.get_ticks()
        self.enemy_shield_bar = Shield_bar(screen)

        # Score
        self.score = Score()

        # Controladores de tempo
        self.ready_time = pygame.time.get_ticks()

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

            # Gera novos inimigos
            now = pygame.time.get_ticks()
            if now - self.last_enemy > self.create_enemy_delay:
                self.last_enemy = now
                self.new_tripe_enemy()

            self.collision_checks()

            # Verifica se o player ainda tem vidas
            if self.player.lives == 0 and not self.death_explosion.alive():
                self.game_over = True
                self.show_game_over_screen = True
                self.game_over_screen()

            # Update/Draw
            self.sprite_group.update()
            pygame.display.update()
            self.draw_sprites()

    # Desenha as sprites no jogo
    def draw_sprites(self):
        screen.fill(BLACK)
        self.sprite_group.draw(screen)

        # Texto/Draw
        draw_text(f"Score: {self.score.score}", 18, WHITE, SCREEN_X / 2, 16)  # Texto do score
        self.draw_shield_bar(screen, 5, 10) # Shield do Player
        self.draw_lives(screen, 480, 10, self.player_mini_image) # Vidas do Player

        self.draw_ready()

        # Shield do player
        for enemy in self.enemy_group:
            self.enemy_shield_bar.draw_shield_bar(enemy.shield, enemy.rect.x, enemy.rect.y)

        pygame.display.flip()

    # Checa as colisões do jogo
    def collision_checks(self):

        # Colissão dos tiros do Player com o Asteroid
        bullet_asteroid_collide = pygame.sprite.groupcollide(self.asteroid_group, self.bullet_group, True, True, pygame.sprite.collide_circle)
        for hit in bullet_asteroid_collide:
            self.score += 1
            explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
            self.sprite_group.add(explosion)
            self.new_asteroid()

        # Colisão com o tiro do Player
        player_shot_collide = pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, False, True, pygame.sprite.collide_mask)
        for hit in player_shot_collide:
            hit.shield -= 1
            if hit.shield <= 0:

                # Powerups
                if randint(0, 10) >= 5:
                    powerup = Powerup(hit.rect.center)
                    self.sprite_group.add(powerup)
                    self.powerup_group.add(powerup)

                self.score.add_score()
                hit.kill()
                explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(explosion)

        # Colisão d Player com o Asteroid
        player_asteroid_collide = pygame.sprite.spritecollide(self.player, self.asteroid_group, True, pygame.sprite.collide_mask)
        for hit in player_asteroid_collide:
            self.player.shield -= 20  # Tira o shield do player
            self.new_asteroid()  # Cria um novo asteroide
            if self.player.shield <= 0:
                death_explosion = Explosion(self.player.rect.center, self.explosion_sprite_sheet)
                self.sprite_group.add(death_explosion)
                self.player.hide()  # Esconde o player temporariamete
                self.player.lives -= 1  # Tira uma vida do player
                self.player.shield = 100  # O shield do jogador volta a ser 100

        # Colisão entre o Enemy e o Asteroid
        enemy_asteroid_collide = pygame.sprite.groupcollide(self.enemy_group, self.asteroid_group, True, True, pygame.sprite.collide_mask)
        for hit in enemy_asteroid_collide:
            self.new_asteroid()
            explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
            self.sprite_group.add(explosion)

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

        # Explosão quando o tiro bate na nave
        '''self.explode_bullet = pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, False, False, pygame.sprite.collide_mask)
        for hit in self.explode_bullet:
            explosion = Explosion(hit.rect.center, self.explosion_sprite_sheet)
            self.sprite_group.add(explosion)'''

    # Tela de pause
    def pause_screen(self):
        self.show_pause = True
        while self.show_pause:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_pause = False
                    self.game_over = True
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            # Título
            self.draw_text("PAUSE", LARGE_FONT_SIZE, WHITE, SCREEN_X / 2, 100)

            # Botões
            voltar_ao_jogo_button = draw_button(SCREEN_X / 2 - 150, 250, SCREEN_X / 2 + 10, 50, "VOLTAR AO JOGO")
            voltar_ao_menu_button = draw_button(SCREEN_X / 2 - 150, 310, SCREEN_X / 2 + 10, 50, "VOLTAR AO MENU")
            sair_do_jogo_button = draw_button(SCREEN_X / 2 - 150, 370, SCREEN_X / 2 + 10, 50, "SAIR DO JOGO")

            # Posição do mouse
            mx, my = pygame.mouse.get_pos()

            # Inputs do mouse com os botões do menu
            if voltar_ao_jogo_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_pause = False
            if voltar_ao_menu_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_pause = False
                    self.game_over = True
                    menu.menu()
            if sair_do_jogo_button.collidepoint((mx, my)):
                if self.click:
                    self.click = False
                    self.show_pause = False
                    self.game_over = True
                    pygame.quit()
                    exit()

            # Depois de checar os inputs o click fica falso
            self.click = False

            pygame.display.flip()
            pygame.display.update()
            screen.fill(BLACK)

    # Tela de game over
    def game_over_screen(self):
        while self.mostrar_game_over_screen:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


            self.draw_text("GAME OVER", LARGE_FONT_SIZE, RED, SCREEN_X / 2, 60)
            self.draw_text(f"SCORE: {self.score}", MEDIUM_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y / 2 - 32)
            self.draw_text("PRESSIONE 'SPACE' PARA VOLTAR AO MENU", SMALL_FONT_SIZE, WHITE, SCREEN_X / 2, SCREEN_Y - 100)

            pygame.display.flip()
            pygame.display.update()
            screen.fill(BLACK)

    # Função para criar um novo asteroide
    def new_asteroid(self):
        m = Asteroid(self.asteroid_sprite_sheet)
        self.sprite_group.add(m)
        self.asteroid_group.add(m)

    # Função para criar inimigos
    def new_tripe_enemy(self):
        pos_x = randint(0 + ENEMY_SIZE_X / 2, SCREEN_X - (ENEMY_SIZE_X * 3) + ENEMY_SIZE_X / 2)
        pos_y = -20
        distance_x = ENEMY_SIZE_X
        distance_y = 20
        for i in range(3):
            if i == 0:
                enemy = Enemy(pos_x, pos_y, ENEMY_1_SHIELD, self.enemy_1_sprite_sheet, self.enemy_shoot_group, self.sprite_group, self.explosion_sprite_sheet, self.score)
            else:
                enemy = Enemy(pos_x + distance_x, pos_y - distance_y, ENEMY_1_SHIELD, self.enemy_1_sprite_sheet, self.enemy_shoot_group, self.sprite_group, self.explosion_sprite_sheet, self.score)
                distance_x += ENEMY_SIZE_X
                distance_y -= 20
            self.sprite_group.add(enemy)
            self.enemy_group.add(enemy)



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






def draw_text(text, tam, color, x, y, topleft=False):
    fonte = pygame.font.Font(FONTE, tam)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    if topleft:
        text_rect.topleft(x, y)
    else:
        text_rect.center = (x, y)
    screen.blit(text_obj, text_rect)

def draw_button(left, top, width, height, text, font_size=20, color=(0, 0, 0)):
    button_border = pygame.Rect(left - 2, top - 2, width + 4, height + 4)
    button = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, (255, 255 ,255), button_border)
    pygame.draw.rect(screen, color, button)
    draw_text(text, font_size, (255, 255, 255), left + (width / 2), top + (height / 2))
    return button




if __name__ == '__main__':
    pygame.init()  # Inicializa o pygame
    pygame.mixer.init()  # Inicializa o modulo de mixer

    menu = Menu()
    game = Game()

    # Tela do jogo
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption("Space Battle")

    # Ajuda a controlar a taxa de atualização do jogo - FPS
    clock = pygame.time.Clock()

    menu.menu()
