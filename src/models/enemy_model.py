from src.models.utils_models import Point
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType

class Enemy(MapObject):
    initial_enemies = 50
    types = 24

    def __init__(self, center_position: Point, name: str):
        super().__init__(center_position, name, MapObjectType.ENEMY)
        self._set_speed(1.5)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
