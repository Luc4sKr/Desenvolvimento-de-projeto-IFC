from os import path, getcwd

# Screen
SCREEN_X = 580
SCREEN_Y = 720


# Player
PLAYER_SIZE_X = 80
PLAYER_SIZE_Y = 80
# Barra de shield do Player
PLAYER_BAR_HEIGHT = 15
PLAYER_BAR_WIDTH = 150


# Enemy
ENEMY_SIZE_X = 70
ENEMY_SIZE_Y = 70

ENEMY_1_SHIELD = 4

ENEMY_SHOOT_VELY = 7

# Barra de shield do Enemy
SHIELD_BAR_HEIGHT = 5

ENEMY_SHOOT_DELAY = 1700


# Kamikaze
KAMIKAZE_XPOS_1 = -10
KAMIKAZE_XPOS_2 = SCREEN_X - 10
KAMIKAZE_SHIELD = 4
KAMIKAZE_DAMAGE = 50


# Asteroid
ASTEROID_SIZE_X = 60
ASTEROID_SIZE_Y = 60
ASTEROID_TIME = 20000 # Tempo para ter a chance de começar o evento
ASTEROID_EVENT_COOLDOWN = 10000 # COOLDOWND do tempo de evento
ASTEROID_COOLDOWN = 100 # COOLDOWN que os asteroids tem para aparecer
ASTEROID_DAMAGE = 20


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
YELLOW  = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Fonte
FONTE = path.join(getcwd() + "/assets/font/8-bit_font.ttf")



