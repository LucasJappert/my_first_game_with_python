import pygame
import src.utils.camera_variables as camera_variables

class Resources:
    textures: dict[str, pygame.Surface] = {}

    @staticmethod
    def load_textures():
        grass = pygame.image.load("src/assets/terrain/grass.png").convert()
        grass = pygame.transform.scale(grass, (camera_variables.tile_size, camera_variables.tile_size))
        Resources.textures["grass"] = grass
