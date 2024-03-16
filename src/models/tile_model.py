from src.models.tile_interface import TileInterface
from src.models.my_sprite_model import MySprite
from src.models.utils_models import Point
from src.helpers.resources_helper import GeneralTextures, get_scaled_image
from src.utils.map_variables import MAP_VARIABLES
from src.events.event_observers import Event
        
class Tile(TileInterface):
    _tiles_info: dict[str, "Tile"] = {}
    
    def __init__(self, position: Point, tiles_info: dict[str, "Tile"]):
        self._tiles_info = tiles_info
        self._position = position
        self._blocked = False
        self._size = MAP_VARIABLES.tile_size
        self._sprite = MySprite(get_scaled_image(GeneralTextures.SQUARE.name, MAP_VARIABLES.tile_size.x, MAP_VARIABLES.tile_size.y))
        self._sprite.set_top_left((position.x - 1) * MAP_VARIABLES.tile_size.x, (position.y - 1) * MAP_VARIABLES.tile_size.y)
        self._tile_updated = Event()
        
    def subscribe(self, observer):
        self._tile_updated.subscribe(observer)
        
    def set_blocked(self, blocked: bool):
        self._blocked = blocked
        self._tile_updated.emit(self)
        
    def get_position(self):
        return self._position
    
    def get_position_in_pixels(self):
        return Point(int((self._position.x - 0.5) * self._size.x), int((self._position.y - 0.5) * self._size.y))
    
    @staticmethod
    def get_tile_key(col: int, row: int):
        return f"{col}_{row}"
        
