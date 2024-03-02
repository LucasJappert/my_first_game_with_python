from src.models.utils_models import Point
from src.models.enemy import Enemy
from src.utils.camera_variables import CAMERA_VARIABLES
import src.utils.map_utils as map_utils

class Map():
    
    def __init__(self):
        self.enemies: list[Enemy] = []
    
    def initialize(self):
        for i in range(20):
            random_tile = map_utils.get_randome_tile()
            random_x = random_tile.x * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
            random_y = random_tile.y * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
            self.enemies.append(Enemy(Point(random_x, random_y), f"enemy_{i}"))
    
MAP = Map()
