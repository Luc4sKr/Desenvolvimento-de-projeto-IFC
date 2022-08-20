import json

from os import getcwd, path


class Util:
    def __init__(self):
        self.open_file()

    def open_file(self):
        with open(path.join(getcwd() + "/scripts/data/data.json"), "r") as file:
            self.json_obj = json.load(file)

    def get_coins(self):
        return self.json_obj["player"]["coins"]

    def get_spaceship(self):
        return self.json_obj["player"]["nave"]

    def spaceship_attributes(self):
        return self.json_obj["naves"][self.get_spaceship()]

    def save_file(self):
        with open(path.join(getcwd() + "/scripts/data/data.json"), "w") as save:
            json.dump(self.json_obj, save, indent=4)
