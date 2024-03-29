import random
from src.models.player_model import Player
from src.models.utils_models import Point
from src.models.enemy_model import Enemy
from src.utils.camera_variables import CAMERA_VARIABLES
import src.utils.map_utils as map_utils

class Map():
    enemies: list[Enemy] = []
    my_player: Player = None
    
    def __init__(self):
        pass
    
    def initialize(self):
        for i in range(Enemy.initial_enemies):
            enemy_name = f"enemy_{random.randint(1, Enemy.types)}"
            # enemy_name = f"enemy_9"
            random_tile = map_utils.get_randome_tile()
            random_x = random_tile.x * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.y / 2)
            random_y = random_tile.y * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.y / 2)
            self.enemies.append(Enemy(Point(random_x, random_y), enemy_name))
        
        self.my_player = Player(map_utils.get_center_tile(), "player_1")
    
MAP = Map()
