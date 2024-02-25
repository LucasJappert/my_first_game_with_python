import pygame
import src.utils.variables as Variables

class Resources:
    textures: dict[str, pygame.Surface] = {}

    @staticmethod
    def load_textures():
        grass = pygame.image.load("src/assets/terrain/grass.png").convert()
        grass = pygame.transform.scale(grass, (Variables.Camera.tile_size, Variables.Camera.tile_size))
        Resources.textures["grass"] = grass
