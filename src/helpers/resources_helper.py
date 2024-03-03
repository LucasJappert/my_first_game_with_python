from enum import Enum
import pygame
from src.utils.camera_variables import CAMERA_VARIABLES

class ResourcesNames(Enum):
    GRASS = "src/assets/terrain/grass.png"
    SQUARE = "src/assets/square.png"
    ENEMY = "src/assets/enemies/enemy.png"
    PLAYER = "src/assets/players/my-player.png"

class Resources:
    textures: dict[str, pygame.Surface] = {}

    def load_textures(self):
        for texture_name in ResourcesNames:
            texture = pygame.image.load(texture_name.value).convert_alpha()
            texture = pygame.transform.scale(texture, (CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y))
            self.textures[texture_name.name] = texture

RESOURCES = Resources()

_get_sacaled_image_cache: dict[str, pygame.Surface] = {}
def get_sacaled_image(texture_name: str, width: int, height: int):
    """Implements an internal cache to avoid recalculating the same scaled image."""
    key = f"{texture_name}_{width}_{height}"
    if key in _get_sacaled_image_cache:
        return _get_sacaled_image_cache[key]
    
    texture = RESOURCES.textures[texture_name]
    scaled_image = pygame.transform.scale(texture, (width, height))
    _get_sacaled_image_cache[key] = scaled_image

    return scaled_image
