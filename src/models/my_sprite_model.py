import pygame
from pygame import Surface
from src.models.utils_models import Point
from src.models.my_sprite_interface import MySpriteInterface
from src.models.tile_interface import TileInterface
from src.utils.map_variables import MAP_VARIABLES

class MySprite(MySpriteInterface):
    def __init__(self, texture: pygame.Surface):
        super().__init__()
        self.image = texture
        self.rect = self.image.get_rect()

    def set_top_left(self, x: int, y: int):
        self.rect.topleft = (x, y)
    
    def set_top_left_for_map_object(self, position: Point):
        # top_left_x = tile._position.x * tile._size.x - int(self.image.get_width() * 0.5)
        # top_left_y = int(tile._position.y * tile._size.y - (self.image.get_height() - _collide_circle_radius * 0.5))
        # top_left_x = int((tile._position.x - 0.5) * tile._size.x - self.image.get_width() * 0.5)
        # top_left_y = int(tile._position.y * tile._size.y - self.image.get_height())
        top_left_x = int(position.x - self.image.get_width() * 0.5)
        top_left_y = int(position.y + MAP_VARIABLES.tile_size.y * 0.5 - self.image.get_height())
        self.set_top_left(top_left_x, top_left_y)
    
