import pygame
from configurations import Configurations


class Resources:
    textures: dict[str, pygame.Surface] = {}

    @staticmethod
    def load_textures():
        grass = pygame.image.load("src/terrain/grass.png")
        grass = pygame.transform.scale(grass, (Configurations.tile_size, Configurations.tile_size))
        Resources.textures["grass"] = grass