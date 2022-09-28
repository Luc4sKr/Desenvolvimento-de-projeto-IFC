from scripts.constants import Constants as Const
from scripts.data.data_utils import Data_util



class Loja_util:

    @staticmethod
    def equip_spaceship(util, spaceship):
        if spaceship in util.get_purchased_ships():
            util.set_player_spaceship(spaceship)

            # -!! Achar uma forma mais organizada para trocar a imagem do Player !!- #
            Const.PLAYER_IMAGE = f"{Const.IMAGE_DIR}/sprites/spaceships/{Data_util.get_player_spaceship()}.png"

    @staticmethod
    def buy_spaceship(util, spaceship):
        if util.get_coins() >= util.get_spaceships(spaceship)["price"]:
            util.set_coins(-util.get_spaceships(spaceship)["price"])
            util.set_purchased_ships(spaceship)
     