import pygame
from src.models.utils_models import Point
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType
from src.utils.map_utils import get_fixed_mouse_position

class Player(MapObject):

    def __init__(self, center_position: Point, name: str):
        super().__init__(center_position, name, MapObjectType.PLAYER)
        self.set_speed(4)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
        
    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                self.on_right_click()

    def on_right_click(self):
        fixed_mouse_position = get_fixed_mouse_position()
        self.set_target_position(fixed_mouse_position)
