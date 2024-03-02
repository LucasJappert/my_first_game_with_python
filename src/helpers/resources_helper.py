from enum import Enum
import pygame
from src.utils.camera_variables import CAMERA_VARIABLES

class ResourcesNames(Enum):
    GRASS = "grass"
    SQUARE = "square"

class Resources:
    textures: dict[str, pygame.Surface] = {}

    def load_textures(self):
        grass = pygame.image.load("src/assets/terrain/grass.png").convert()
        grass = pygame.transform.scale(grass, (CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size))
        self.textures["grass"] = grass
        
        square = pygame.image.load("src/assets/square.png").convert_alpha()
        square = pygame.transform.scale(square, (CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size))
        self.textures["square"] = square

RESOURCES = Resources()

_cache: dict[str, pygame.Surface] = {}
def get_sacaled_image(texture_name: str, width: int, height: int):
    key = f"{texture_name}_{width}_{height}"
    if key in _cache:
        return _cache[key]
    
    texture = RESOURCES.textures[texture_name]
    scaled_image = pygame.transform.scale(texture, (width, height))
    _cache[key] = scaled_image

    return scaled_image
