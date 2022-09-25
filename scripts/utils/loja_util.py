


class Loja_util:

    @staticmethod
    def equip_spaceship(util, spaceship):
        if spaceship in util.get_purchased_ships():
            util.set_player_spaceship(spaceship)

    @staticmethod
    def buy_spaceship(util, spaceship):
        if util.get_coins() >= util.get_spaceships(spaceship)["price"]:
            util.set_coins(-util.get_spaceships(spaceship)["price"])
            util.set_purchased_ships(spaceship)
