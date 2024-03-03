from enum import Enum
import pygame
from src.utils.camera_variables import CAMERA_VARIABLES

class ResourcesNames(Enum):
    GRASS = "src/assets/terrain/grass.png"
    SQUARE = "src/assets/square.png"
    ENEMY = "src/assets/enemies/enemy.png"
    PLAYER = "src/assets/players/my-player.png"


DIRECTIONS = ["bottom", "left", "right", "top"]

class Resources:
    textures: dict[str, pygame.Surface] = {}

    def load_textures(self):
        for texture_name in ResourcesNames:
            texture = pygame.image.load(texture_name.value).convert_alpha()
            texture = pygame.transform.scale(texture, (CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y))
            self.textures[texture_name.name] = texture
        
        # Add sprites contained in the enemies spritesheet
        enemies_by_columns = 8
        enemies_by_rows = 4
        frames_by_animation = 3
        enemies_spritesheet = pygame.image.load("src/assets/enemies/enemies-spritesheet.png").convert_alpha()
        frame_size = 32
        for row in range(enemies_by_rows):
            for column in range(enemies_by_columns):
                enemy_id = row * enemies_by_columns + column + 1
                for direction_index, direction in enumerate(DIRECTIONS):
                    for frame in range(frames_by_animation):
                        x_into_spritesheet = column * frames_by_animation * frame_size + frame * frame_size
                        y_into_spritesheet = row * len(DIRECTIONS) * frame_size + direction_index * frame_size
                        texture = enemies_spritesheet.subsurface(pygame.Rect(x_into_spritesheet, y_into_spritesheet, frame_size, frame_size))
                        self.textures[f"enemy_{enemy_id}_{direction}_{frame+1}"] = texture
        
        # Add sprites contained in the players spritesheet
        players_by_columns = 4
        players_by_rows = 2
        frames_by_animation = 3
        players_spritesheet = pygame.image.load("src/assets/players/players-spritesheet.png").convert_alpha()
        frame_size = 32
        for row in range(players_by_rows):
            for column in range(players_by_columns):
                player_id = row * players_by_columns + column + 1
                for direction_index, direction in enumerate(DIRECTIONS):
                    for frame in range(frames_by_animation):
                        x_into_spritesheet = column * frames_by_animation * frame_size + frame * frame_size
                        y_into_spritesheet = row * len(DIRECTIONS) * frame_size + direction_index * frame_size
                        texture = players_spritesheet.subsurface(pygame.Rect(x_into_spritesheet, y_into_spritesheet, frame_size, frame_size))
                        self.textures[f"player_{player_id}_{direction}_{frame+1}"] = texture

    def get_textures_by_enemy_id(self, enemy_id: int):
        result: dict[str, list[pygame.Surface]] = {}

        keys_bottom = list(filter(lambda key: f"enemy_{enemy_id}_{DIRECTIONS[0]}" in key, self.textures.keys()))
        keys_left = list(filter(lambda key: f"enemy_{enemy_id}_{DIRECTIONS[1]}" in key, self.textures.keys()))
        keys_right = list(filter(lambda key: f"enemy_{enemy_id}_{DIRECTIONS[2]}" in key, self.textures.keys()))
        keys_top = list(filter(lambda key: f"enemy_{enemy_id}_{DIRECTIONS[3]}" in key, self.textures.keys()))
        result[DIRECTIONS[0]] = list(map(lambda key: self.textures[key], keys_bottom))
        result[DIRECTIONS[1]] = list(map(lambda key: self.textures[key], keys_left))
        result[DIRECTIONS[2]] = list(map(lambda key: self.textures[key], keys_right))
        result[DIRECTIONS[3]] = list(map(lambda key: self.textures[key], keys_top))

        return result




RESOURCES = Resources()

_get_sacaled_image_cache: dict[str, pygame.Surface] = {}
def get_scaled_image(texture_key: str, width: int, height: int):
    """Implements an internal cache to avoid recalculating the same scaled image."""
    key = f"{texture_key}_{width}_{height}"
    if key in _get_sacaled_image_cache:
        return _get_sacaled_image_cache[key]
    
    texture = RESOURCES.textures[texture_key]
    scaled_image = pygame.transform.scale(texture, (width, height))
    _get_sacaled_image_cache[key] = scaled_image

    return scaled_image
