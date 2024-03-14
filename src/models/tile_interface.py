from src.models.utils_models import Point
from src.models.my_sprite_interface import MySpriteInterface

class TileInterface():
    _position: Point = None
    _blocked: bool = False
    _sprite: MySpriteInterface = None
