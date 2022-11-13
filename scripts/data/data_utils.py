import json

from os import getcwd, path


class Data_util:

    with open(path.join(getcwd() + "/scripts/data/data.json"), "r") as file:
        json_obj = json.load(file)

    @staticmethod
    def open_file():
        with open(path.join(getcwd() + "/scripts/data/data.json"), "r") as file:
            Data_util.json_obj = json.load(file)

    @staticmethod
    def save_file():
        with open(path.join(getcwd() + "/scripts/data/data.json"), "w") as save:
            json.dump(Data_util.json_obj, save, indent=4)

    @staticmethod
    def get_coins():
        return Data_util.json_obj["player"]["coins"]

    @staticmethod
    def set_coins(coin):
        Data_util.json_obj["player"]["coins"] += coin
        Data_util.save_file()

    @staticmethod
    def get_player_spaceship():
        return Data_util.json_obj["player"]["ship"]

    @staticmethod
    def set_player_spaceship(spaceship):
        Data_util.json_obj["player"]["ship"] = str(spaceship)
        Data_util.save_file()

    @staticmethod
    def get_spaceships(spaceship_name):
        return Data_util.json_obj["spaceships"][spaceship_name]

    @staticmethod
    def get_purchased_ships():
        return Data_util.json_obj["player"]["purchased-ships"]

    @staticmethod
    def set_purchased_ships(spaceship):
        Data_util.json_obj["player"]["purchased-ships"].append(spaceship)
        Data_util.save_file()

    @staticmethod
    def get_image():
        return Data_util.json_obj["game"]["image"]

    @staticmethod
    def set_image(image):
        Data_util.json_obj["game"]["image"] = image
        Data_util.save_file()

    @staticmethod
    def get_music():
        return Data_util.json_obj["game"]["music"]

    @staticmethod
    def get_music_activated():
        return Data_util.json_obj["game"]["music_activated"]

    @staticmethod
    def set_music_activated(resp):
        Data_util.json_obj["game"]["music_activated"] = resp
        Data_util.save_file()

    @staticmethod
    def get_sound_activated():
        return Data_util.json_obj["game"]["sounds_activated"]

    @staticmethod
    def set_sound_activated(resp):
        Data_util.json_obj["game"]["sounds_activated"] = resp
        Data_util.save_file()

    @staticmethod
    def spaceship_attributes():
        return Data_util.json_obj["spaceships"][Data_util.get_player_spaceship()]
