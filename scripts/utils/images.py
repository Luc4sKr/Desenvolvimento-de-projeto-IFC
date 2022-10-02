from os import path, getcwd

from scripts.data.data_utils import Data_util


class Images:

    # Diretórios de imagem
    image_dir = path.join(getcwd() + f"/assets/images/{Data_util.get_image()}")

    asteroid_image_dir = f"{image_dir}/sprites/asteroid"
    explosion_image_dir = f"{image_dir}/sprites/explosion"
    enemy_image_dir = f"{image_dir}/sprites/enemy"
    kamikaze_image_dir = f"{image_dir}/sprites/kamikaze"
    boss_body_image_dir = f"{image_dir}/sprites/boss/body"
    boss_wing_image_dir = f"{image_dir}/sprites/boss/wings"

    # Imagens
    manu_image_background = f"{image_dir}/backgrounds/menu-background.png"
    game_image_background = f"{image_dir}/backgrounds/game-background.png"
    player_image = f"{image_dir}/sprites/spaceships/{Data_util.get_player_spaceship()}.png"
    shield_powerup_image = f"{image_dir}/powerups/shield.png"
    gun_powerup_image = f"{image_dir}/powerups/gun.png"
    bullet_player_image = f"{image_dir}/bullet/player-bullet.png"
    bullet_enemy_image = f"{image_dir}/bullet/enemy-bullet.png"
    bullet_boss_image = f"{image_dir}/bullet/boss-bullet-blue.png"
    coin_image = f"{image_dir}/coins/coin-1.png"

    @staticmethod
    def update():
        Images.image_dir = path.join(getcwd() + f"/assets/images/{Data_util.get_image()}")

        Images.asteroid_image_dir = f"{Images.image_dir}/sprites/asteroid"
        Images.explosion_image_dir = f"{Images.image_dir}/sprites/explosion"
        Images.enemy_image_dir = f"{Images.image_dir}/sprites/enemy"
        Images.kamikaze_image_dir = f"{Images.image_dir}/sprites/kamikaze"
        Images.boss_body_image_dir = f"{Images.image_dir}/sprites/boss/body"
        Images.boss_wing_image_dir = f"{Images.image_dir}/sprites/boss/wings"

        Images.manu_image_background = f"{Images.image_dir}/backgrounds/menu-background.png"
        Images.game_image_background = f"{Images.image_dir}/backgrounds/game-background.png"
        Images.player_image = f"{Images.image_dir}/sprites/spaceships/{Data_util.get_player_spaceship()}.png"
        Images.shield_powerup_image = f"{Images.image_dir}/powerups/shield.png"
        Images.gun_powerup_image = f"{Images.image_dir}/powerups/gun.png"
        Images.bullet_player_image = f"{Images.image_dir}/bullet/player-bullet.png"
        Images.bullet_enemy_image = f"{Images.image_dir}/bullet/enemy-bullet.png"
        Images.bullet_boss_image = f"{Images.image_dir}/bullet/boss-bullet-blue.png"
        Images.coin_image = f"{Images.image_dir}/coins/coin-1.png"
