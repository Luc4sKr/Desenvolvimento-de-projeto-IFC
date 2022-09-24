import pygame
from os import path, getcwd

# Diretórios
IMAGE_DIR = path.join(getcwd() + f"/assets/images/default")
SOUND_DIR = path.join(getcwd() + f"/assets/sounds")

ASTEROID_IMAGE_DIR = f"{IMAGE_DIR}/sprites/asteroid"
EXPLOSION_IMAGE_DIR = f"{IMAGE_DIR}/sprites/explosion"
ENEMY_IMAGE_DIR = f"{IMAGE_DIR}/sprites/enemy"
KAMIKADE_IMAGE_DIR = f"{IMAGE_DIR}/sprites/kamikaze"
BOSS_BODY_IMAGE_DIR = f"{IMAGE_DIR}/sprites/boss/body"
BOSS_WING_IMAGE_DIR = f"{IMAGE_DIR}/sprites/boss/wings"

# Imagens
MENU_IMAGE_BACKGROUND = f"{IMAGE_DIR}/backgrounds/menu-background.png"
GAME_IMAGE_BACKGROUND = f"{IMAGE_DIR}/backgrounds/game-background.png"
PLAYER_IMAGE = f"{IMAGE_DIR}/sprites/spaceships/"
SHIELD_POWERUP_IMAGE = f"{IMAGE_DIR}/powerups/shield.png"
GUN_POWERUP_IMAGE = f"{IMAGE_DIR}/powerups/gun.png"
BULLET_PLAYER_IMAGE = f"{IMAGE_DIR}/bullet/player-bullet.png"
BULLET_ENEMY_IMAGE = f"{IMAGE_DIR}/bullet/enemy-bullet.png"
BULLET_BOSS_BLUE_IMAGE = f"{IMAGE_DIR}/bullet/boss-bullet-blue.png"
COIN_IMAGE = f"{IMAGE_DIR}/coins/coin-1.png"

# Screen
SCREEN_X = 580
SCREEN_Y = 720

# Background
BACKGROUND_MOVEMENT_SPEED_Y = 4

# Delays
READY_DELAY = 1000
GO_DELAY = 2000

# Player
PLAYER_SIZE_X = int(32 * 2.5)     # Largura do PLayer
PLAYER_SIZE_Y = int(32 * 2.5)    # Altura do Player
MINI_PLAYER_IMG = 35             # Imagem utilizada para a contagem das vidas do Player
PLAYER_SHIELD_BAR_HEIGHT = 15    # Altura da barra de shield do Player
PLAYER_SHIELD_BAR_WIDTH = 170    # Largura da barra de shield do Player
PLAYER_BULLET = "player-bullet"  # Nome do arquivo da sprite do tiro
PLAYER_SHOOT_SPEED = -10         # Velocidade do tiro do Player

# Player shield bar
PLAYER_SHIELD_BAR_POS_X = 10  # Posição X da barra de shield do Player
PLAYER_SHIELD_BAR_POS_Y = 10  # Posição Y da barra de shield do Player
PLAYER_COLLIDE_DAMAGE = 50  # Dano de colisão com naves inimigas

# Coin
COIN_WIDTH = int(32 * 0.4)
COIN_HEIGHT = int(32 * 0.4)

# Enemy
ENEMY_SIZE_X = 70              # Largura do inimigo
ENEMY_SIZE_Y = 70              # Altura do inimigo
ENEMY_SHIELD = 4               # Shield do inimigo
ENEMY_DAMGE = 30               # Dano do inimigo
ENEMY_SHOOT_SPEED_Y = 7        # Velocidade do tiro
ENEMY_SPEED_Y = 1              # Velocidade do inimigo
ENEMY_SHIELD_BAR_HEIGHT = 5    # Barra de shield do inimigo
ENEMY_SHOOT_DELAY = 1700       # Delay do tiro
ENEMY_BULLET = "enemy-bullet"  # Nome do arquivo da sprite do tiro

# Kamikaze
KAMIKAZE_X_POS_1 = -10             # Posição X do kamikaze quando spawna no lado esquerdo da tela
KAMIKAZE_X_POS_2 = SCREEN_X - 10   # Posição X do kamikaze quando spawna no lado direito da tela
KAMIKAZE_SHIELD = 4                # Shield
KAMIKAZE_DAMAGE = 50               # Dano

# Asteroid
ASTEROID_SIZE_X = 60                   # Largura do asteroide
ASTEROID_SIZE_Y = 60                   # Altura do asteroide
ASTEROID_SHOWER_COOLDOWN_TIME = 20000  # Tempo para ter a chance de começar o evento
ASTEROID_EVENT_COOLDOWN = 10000        # COOLDOWND do tempo de evento
ASTEROID_COOLDOWN = 100                # COOLDOWN para gerar um novo asteroide
ASTEROID_DAMAGE = 20                   # Dano do asteroide

# Boss
BODY_BOSS_SIZE_X = 128 * 1.6        # Largura do corpo do Boss
BODY_BOSS_SIZE_Y = 128 * 1.5        # Altura do corpo do Boss
WING_BOSS_SIZE_X = 128 * 1.6        # Largura da asa do Boss
WING_BOSS_SIZE_Y = 128 * 1.5        # Altura da asa do Boss
WING_BOSS_SHIELD = 50               # Shield da asa do Boss
BODY_BOSS_SHIELD = 100              # Shield do corpo do Boss
BOSS_BIG_SHOOT_DELAY = 2000         # Delay do tiro grande do Boss
BOSS_SMALL_SHOOT_DELAY = 1800       # Delay do tiro pequeno do Boss
BOSS_SMALL_SHOOT_TEMP_DELAY = 200   # Tempo de dalay do tiro pequeno
BOSS_SMALL_SHOOT_SPEED_Y = 6        # Velocidade do tiro pequeno
BOSS_BIG_SHOOT_SPEED_Y = 5          # Velocidade do tiro grade
BOSS_SMALL_SHOOT_DAMAGE = 10        # Dano do tiro pequeno
BOSS_BIG_SHOOT_DAMAGE = 30          # Dano do tiro grande

# Explosion
EXPLOSION_WIDTH = 50
EXPLOSION_HEIGHT = 50

# FPS
FPS = 60

# Cooldown de animação
ASTEROID_ANIMATION_COOLDOWN = 100
EXPLOSION_ANIMATION_COOLDOWN = 100
ENEMIES_ANIMATION_COOLDOWN = 100

# Powerup
POWERUP_TIME = 5000
POWERUP_SPEED_Y = 3
POWERUP_WIDTH = int(32 * 1.3)
POWERUP_HEIGHT = int(32 * 1.3)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Sons
pygame.mixer.init()

SHOOT_SOUND_1 = pygame.mixer.Sound(f"{SOUND_DIR}/shoot-1.wav")
SHOOT_SOUND_2 = pygame.mixer.Sound(f"{SOUND_DIR}/shoot-2.wav")
EXPLOSION_SOUND = pygame.mixer.Sound(f"{SOUND_DIR}/explosion-1.wav")
SELECT_SOUND = pygame.mixer.Sound(f"{SOUND_DIR}/select-3.wav")
COIN_SOUND = pygame.mixer.Sound(f"{SOUND_DIR}/coin-1.wav")

SHOOT_SOUND_1.set_volume(0.15)
SHOOT_SOUND_2.set_volume(0.1)
EXPLOSION_SOUND.set_volume(0.4)
SELECT_SOUND.set_volume(0.1)
COIN_SOUND.set_volume(0.4)

# Fonte
FONT_STYLE = path.join(getcwd() + "/assets/font/8-bit_font.ttf")
LOGO_FONT = 60          # Fonte da logo principal
TITLE_FONT = 44         # Fonte do título dos menus
SUB_TITLE_FONT = 22     # Fonte do sub-título
SMALL_FONT = 14         # Fonte pequena
