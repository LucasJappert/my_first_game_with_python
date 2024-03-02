from enum import Enum
import pygame
from src.utils.camera_variables import CAMERA_VARIABLES

class ResourcesNames(Enum):
    GRASS = "src/assets/terrain/grass.png"
    SQUARE = "src/assets/square.png"
    ENEMY = "src/assets/enemies/enemy.png"

class Resources:
    textures: dict[str, pygame.Surface] = {}

    def load_textures(self):
        for texture_name in ResourcesNames:
            texture = pygame.image.load(texture_name.value).convert_alpha()
            texture = pygame.transform.scale(texture, (CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size))
            self.textures[texture_name.name] = texture

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
