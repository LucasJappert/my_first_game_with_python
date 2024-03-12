from src.models.my_sprite import MyTransparentSprite
from src.models.utils_models import Point
from src.helpers.resources_helper import GeneralTextures, get_scaled_image
from src.utils.map_variables import MAP_VARIABLES

class Tile:
    _position: Point = None
    _is_blocked: bool = False
    _sprite: MyTransparentSprite = None
    
    def __init__(self, position: Point):
        self._position = position
        self._is_blocked = False
        self._sprite = MyTransparentSprite(get_scaled_image(GeneralTextures.SQUARE.name, MAP_VARIABLES.tile_size.x, MAP_VARIABLES.tile_size.y))
        self._sprite.set_top_left((position.x - 1) * MAP_VARIABLES.tile_size.x, (position.y - 1) * MAP_VARIABLES.tile_size.y)
