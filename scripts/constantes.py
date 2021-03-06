from os import path, getcwd

# Screen
import pygame.time

SCREEN_X = 580
SCREEN_Y = 720


# Player
PLAYER_SIZE_X = 80
PLAYER_SIZE_Y = 80
# Barra de shield do Player
BAR_HEIGHT = 15
BAR_WIDTH = 150


# Enemy
ENEMY_SIZE_X = 70
ENEMY_SIZE_Y = 70
# Shield
ENEMY_1_SHIELD = 4
# Barra de shield do Enemy
ENEMY_BAR_HEIGHT = 5
ENEMY_BAR_WIDTH = 18


# Asteroid
ASTEROID_SIZE_X = 60
ASTEROID_SIZE_Y = 60
ASTEROID_TIME = 20000 # Tempo para ter a chance de começar o evento
ASTEROID_EVENT_COOLDOWN = 10000 # COOLDOWND do tempo de evento
ASTEROID_COOLDOWN = 100 # COOLDOWN que os asteroids tem para aparecer


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
YELLOW  = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Fonte
FONTE = path.join(getcwd() + "/assets/font/8-bit_font.ttf")
LARGE_FONT_SIZE = 42
MEDIUM_FONT_SIZE = 28
SMALL_FONT_SIZE = 14


