from src.models.tile_model import Tile
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType

class Enemy(MapObject):
    initial_enemies = 100
    types = 24

    def __init__(self, tile_in: Tile, name: str, tiles_info: dict[str, Tile]):
        super().__init__(tile_in, name, MapObjectType.ENEMY, tiles_info)
        self._set_speed(1)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
