import pygame

from os import listdir


class Sprite_sheet:

    # Cria as sprite sheets de naves
    @staticmethod
    def create_sprite_sheet(sprite_directory, sprite_size_x, sprite_size_y):
        animation_list = []
        num_of_frames = len(listdir(sprite_directory))
        for i in range(1, num_of_frames):
            image = pygame.image.load(f"{sprite_directory}/sprite-{i}.png").convert_alpha()
            image = pygame.transform.scale(image, (int(sprite_size_x), int(sprite_size_y)))
            animation_list.append(image)
        return animation_list
