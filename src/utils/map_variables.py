import random
from src.models.utils_models import Point
from src.models.enemy import Enemy
from src.utils.camera_variables import CAMERA_VARIABLES
from src.helpers.resources_helper import get_sacaled_image, ResourcesNames

class Map():
    
    def __init__(self):
        self.enemies: list[Enemy] = []
    
    def initialize(self):
        for i in range(10):
            random_tile = self.get_randome_tile()
            random_x = random_tile.x * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
            random_y = random_tile.y * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
            self.enemies.append(Enemy(Point(random_x, random_y), f"enemy_{i}"))

    def get_randome_tile(self):
        result: Point = Point(0, 0)
        result.x = random.randint(0, CAMERA_VARIABLES.tiles.x -1)
        result.y = random.randint(0, CAMERA_VARIABLES.tiles.y -1)
        return result
    
MAP = Map()
