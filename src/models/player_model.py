import pygame
from src.models.tile_model import Tile
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType
from src.utils.map_utils import get_fixed_mouse_position

class Player(MapObject):

    def __init__(self, tile_in: Tile, name: str):
        super().__init__(tile_in, name, MapObjectType.PLAYER)
        self._set_speed(4)

    #region GETTERs
    #endregion

    #region SETTERs
    #endregion
        
    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                self.on_right_click()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass

    def on_right_click(self):
        fixed_mouse_position = get_fixed_mouse_position()
        # self._set_target_position(fixed_mouse_position)
        result = self.find_shortest_path(fixed_mouse_position)
        print(result)
