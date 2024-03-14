import pygame
from pygame import Surface
from src.models.my_sprite_interface import MySpriteInterface
from src.models.tile_interface import TileInterface

class MySprite(MySpriteInterface):
    def __init__(self, texture: pygame.Surface):
        super().__init__()
        self.image = texture
        self.rect = self.image.get_rect()

    def set_top_left(self, x: int, y: int):
        self.rect.topleft = (x, y)
    
    def set_top_left_for_map_object(self, tile: TileInterface, _collide_circle_radius: int):
        top_left_x = tile._position.x - int(self.image.get_width() * 0.5)
        top_left_y = int(tile._position.y - (self.image.get_height() - _collide_circle_radius * 0.5))
        self.set_top_left(top_left_x, top_left_y)
    
