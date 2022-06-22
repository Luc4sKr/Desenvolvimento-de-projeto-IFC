from os import path, getcwd

# Screen
SCREEN_X = 580
SCREEN_Y = 720


# Player
PLAYER_SIZE_X = 80
PLAYER_SIZE_Y = 80
PLAYER_VEL = 5
# Barra de shield do Player
BAR_HEIGHT = 15
BAR_WIDTH = 150


# Enemy
ENEMY_SIZE_X = 80
ENEMY_SIZE_Y = 80
# Shield
ENEMY_1_SHIELD = 4
# Barra de shield do Enemy
ENEMY_BAR_HEIGHT = 5
ENEMY_BAR_WIDTH = 18


# Asteroid
ASTEROID_SIZE_X = 60
ASTEROID_SIZE_Y = 60
ASTEROID_VEL = 1


# FPS
FPS = 60


# Cooldown de animação dos sprite sheets
ANIMATION_COOLDOWN = 100

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


# Tamanho da imagem da loja
IMAGE_LOJA_SIZE = 60


