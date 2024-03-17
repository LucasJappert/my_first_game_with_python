import pygame
from src.models.tile_model import Tile
from src.models.map_object_model import MapObject
from src.models.general_enums import MapObjectType
from src.utils.map_utils import get_tile_map_from_mouse_position

class Player(MapObject):

    def __init__(self, tile_in: Tile, name: str, tiles_info: dict[str, Tile]):
        super().__init__(tile_in, name, MapObjectType.PLAYER, tiles_info)
        self._set_speed(1.5)

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
        result = self.find_and_set_shortest_path(get_tile_map_from_mouse_position())
