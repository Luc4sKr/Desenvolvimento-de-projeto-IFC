import pygame
from os import path, getcwd

# Screen
SCREEN_X = 580
SCREEN_Y = 720

# Background
BACKGROUND_MOVEMENT_SPEED_Y = 4

# Delays
READY_DELAY = 1000
GO_DELAY = 2000

# Player
PLAYER_SIZE_X = 32 * 2.5         # Largura do PLayer
PLAYER_SIZE_Y = 32 * 2.5         # Altura do Player
MINI_PLAYER_IMG = 35             # Imagem utilizada para a contagem das vidas do Player
PLAYER_SHIELD_BAR_HEIGHT = 15    # Altura da barra de shield do Player
PLAYER_SHIELD_BAR_WIDTH = 170    # Largura da barra de shield do Player
PLAYER_BULLET = "player-bullet"  # Nome do arquivo da sprite do tiro
PLAYER_SHOOT_SPEED = -10         # Velocidade do tiro do Player


COLLIDE_DAMAGE = 50  # Dano de colisão com naves inimigas

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
BODY_BOSS_SIZE_X = 128 * 1.6
BODY_BOSS_SIZE_Y = 128 * 1.5

WING_BOSS_SIZE_X = 128 * 1.6
WING_BOSS_SIZE_Y = 128 * 1.5

WING_BOSS_SHIELD = 50
BODY_BOSS_SHIELD = 100

BOSS_BIG_SHOOT_DELAY = 2000
BOSS_BIG_SHOOT_VELY = 5

BOSS_SMALL_SHOOT_DELAY = 1800
BOSS_SMALL_SHOOT_TEMP_DELAY = 200
BOSS_SMALL_SHOOT_VELY = 6

# FPS
FPS = 60

# Cooldown de animação do Asteroid
ASTEROID_ANIMATION_COOLDOWN = 100

EXPLOSION_ANIMATION_COOLDOWN = 100

ENEMIES_ANIMATION_COOLDOWN = 100

# Tempo de powerup
POWERUP_TIME = 5000

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Sons
pygame.mixer.init()

SHOOT_SOUND_1 = pygame.mixer.Sound(path.join(getcwd() + "/assets/sounds/shoot-1.wav"))
SHOOT_SOUND_2 = pygame.mixer.Sound(path.join(getcwd() + "/assets/sounds/shoot-2.wav"))
EXPLOSION_SOUND = pygame.mixer.Sound(path.join(getcwd() + "/assets/sounds/explosion-1.wav"))
SELECT_SOUND = pygame.mixer.Sound(path.join(getcwd() + "/assets/sounds/select-3.wav"))

SHOOT_SOUND_1.set_volume(0.5)
SHOOT_SOUND_2.set_volume(0.1)
EXPLOSION_SOUND.set_volume(0.9)
SELECT_SOUND.set_volume(0.1)

# Fonte
FONTE = path.join(getcwd() + "/assets/font/8-bit_font.ttf")
