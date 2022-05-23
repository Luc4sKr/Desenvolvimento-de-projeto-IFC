from os import path, getcwd

# Screen
SCREEN_X = 580
SCREEN_Y = 720

# Player
PLAYER_SIZE_X = 80
PLAYER_SIZE_Y = 80
PLAYER_VEL = 5

# Barra de vida do player
BAR_HEIGHT = 15
BAR_WIDTH = 150

# Enemy
ENEMY_SIZE_X = 80
ENEMY_SIZE_Y = 80

# Asteroid
ASTEROID_SIZE_X = 60
ASTEROID_SIZE_Y = 60
ASTEROID_VEL = 1

# FPS
FPS = 60

# Cooldown de animação dos sprite sheets
ANIMATION_COOLDOWN = 100

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

# Menu de pause
VOLTAR_AO_JOGO_Y = SCREEN_Y / 2 - 32
VOLTAR_AO_MENU_Y = SCREEN_Y / 2
SAIR_DO_JOGO_Y = SCREEN_Y / 2 + 32
OPCOES_Y =SCREEN_Y / 2 + 64
