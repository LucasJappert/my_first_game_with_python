from src.models.utils_models import Point
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType

class Enemy(MapObject):
    _target_position: Point = None
    initial_enemies = 200

    def __init__(self, center_position: Point, name: str):
        super().__init__(center_position, name, MapObjectType.ENEMY)
        self.set_speed(1.5)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
