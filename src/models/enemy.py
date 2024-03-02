import pygame
from src.models.utils_models import Point
from src.models.my_sprite import MyTransparentSprite
from src.utils.camera_variables import CAMERA_VARIABLES
from src.helpers.resources_helper import RESOURCES, get_sacaled_image, ResourcesNames

class Enemy():
    def __init__(self, center_position: Point, name: str):
        self.name = name
        self._rect_in_map = pygame.Rect(center_position.x, center_position.y, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
        self._rect_in_map.centerx = center_position.x
        self._rect_in_map.centery = center_position.y
        self._rect_in_map.width = CAMERA_VARIABLES.tile_size
        self._rect_in_map.height = CAMERA_VARIABLES.tile_size
        self._velocity = 0

        texture = get_sacaled_image(ResourcesNames.ENEMY.name, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
        topleft_x = center_position.x - int(CAMERA_VARIABLES.tile_size / 2)
        topleft_y = center_position.y - int(CAMERA_VARIABLES.tile_size / 2)
        self._sprite = MyTransparentSprite(texture, topleft_x, topleft_y)

    def update(self):
        self._rect_in_map.centerx += self._velocity
        self._rect_in_map.centery += self._velocity
        self._sprite.rect.topleft = (self._rect_in_map.x, self._rect_in_map.y)

    def draw(self, enemy_group: pygame.sprite.Group):
        enemy_group.add(self._sprite)
