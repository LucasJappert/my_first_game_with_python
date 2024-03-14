from src.models.tile_model import Tile
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType

class Enemy(MapObject):
    initial_enemies = 100
    types = 24

    def __init__(self, tile_in: Tile, name: str):
        super().__init__(tile_in, name, MapObjectType.ENEMY)
        self._set_speed(1.5)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
