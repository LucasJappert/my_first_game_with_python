import pygame
from src.models.my_sprite import MyTransparentSprite


class MapObject():
    def __init__(self, rect_in_map: pygame.Rect, texture: pygame.Surface, name: str):
        self.rect_in_map = rect_in_map

        self.sprite = MyTransparentSprite(self.rect_in_map.x, self.rect_in_map.y)
