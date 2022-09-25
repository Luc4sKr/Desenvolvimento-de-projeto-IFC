import json

from os import getcwd, path


class Util:

    with open(path.join(getcwd() + "/scripts/data/data.json"), "r") as file:
        json_obj = json.load(file)

    @staticmethod
    def open_file():
        with open(path.join(getcwd() + "/scripts/data/data.json"), "r") as file:
            Util.json_obj = json.load(file)

    @staticmethod
    def save_file():
        with open(path.join(getcwd() + "/scripts/data/data.json"), "w") as save:
            json.dump(Util.json_obj, save, indent=4)

    @staticmethod
    def get_coins():
        return Util.json_obj["player"]["coins"]

    @staticmethod
    def set_coins(coin):
        Util.json_obj["player"]["coins"] += coin
        Util.save_file()

    @staticmethod
    def get_player_spaceship():
        return Util.json_obj["player"]["ship"]

    @staticmethod
    def set_player_spaceship(spaceship):
        Util.json_obj["player"]["ship"] = str(spaceship)
        Util.save_file()

    @staticmethod
    def get_spaceships(spaceship_name):
        return Util.json_obj["spaceships"][spaceship_name]

    @staticmethod
    def get_purchased_ships():
        return Util.json_obj["player"]["purchased-ships"]

    @staticmethod
    def set_purchased_ships(spaceship):
        Util.json_obj["player"]["purchased-ships"].append(spaceship)
        Util.save_file()

    @staticmethod
    def get_image():
        return Util.json_obj["game"]["image"]

    @staticmethod
    def set_image(image):
        Util.json_obj["game"]["image"] = image
        Util.save_file()

    @staticmethod
    def get_music():
        return Util.json_obj["game"]["music"]

    @staticmethod
    def spaceship_attributes():
        return Util.json_obj["spaceships"][Util.get_player_spaceship()]
