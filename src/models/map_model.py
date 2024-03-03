from src.models.my_player_model import MyPlayer
from src.models.utils_models import Point
from src.models.enemy_model import Enemy
from src.utils.camera_variables import CAMERA_VARIABLES
import src.utils.map_utils as map_utils
from src.configs.configurations import Configurations

class Map():
    enemies: list[Enemy] = []
    my_player: MyPlayer = None
    
    def __init__(self):
        pass
    
    def initialize(self):
        for i in range(Configurations.enemies_number):
            random_tile = map_utils.get_randome_tile()
            random_x = random_tile.x * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.y / 2)
            random_y = random_tile.y * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.y / 2)
            self.enemies.append(Enemy(Point(random_x, random_y), f"enemy_{i}"))
        
        self.my_player = MyPlayer(map_utils.get_center_tile(), "my_player")
    
MAP = Map()
