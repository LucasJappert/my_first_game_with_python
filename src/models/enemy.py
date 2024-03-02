import math
import pygame
from src.models.utils_models import Point
from src.models.my_sprite import MyTransparentSprite
from src.utils.camera_variables import CAMERA_VARIABLES
from src.helpers.resources_helper import RESOURCES, get_sacaled_image, ResourcesNames
import src.utils.map_utils as map_utils

class Enemy():
    _target_position: Point = Point(0, 0)

    def __init__(self, center_position: Point, name: str):
        self.name = name
        self._rect_in_map = pygame.Rect(center_position.x, center_position.y, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
        self._rect_in_map.centerx = center_position.x
        self._rect_in_map.centery = center_position.y
        self._rect_in_map.width = CAMERA_VARIABLES.tile_size
        self._rect_in_map.height = CAMERA_VARIABLES.tile_size
        self._speed = 2

        texture = get_sacaled_image(ResourcesNames.ENEMY.name, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
        topleft_x = center_position.x - int(CAMERA_VARIABLES.tile_size / 2)
        topleft_y = center_position.y - int(CAMERA_VARIABLES.tile_size / 2)
        self._sprite = MyTransparentSprite(texture, topleft_x, topleft_y)

        self.set_random_target()

    #region GETTERs
    def get_center_x(self):
        return self._rect_in_map.centerx
    
    def get_center_y(self):
        return self._rect_in_map.centery
    #endregion

    #region SETTERs
    def set_target_position(self, target_position: Point):
        self._target_position = target_position
    def set_center_x(self, value: int):
        self._rect_in_map.centerx = value
    def set_center_y(self, value: int):
        self._rect_in_map.centery = value
    def set_random_target(self):
        random_tile = map_utils.get_randome_tile()
        random_x = random_tile.x * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
        random_y = random_tile.y * CAMERA_VARIABLES.tile_size + int(CAMERA_VARIABLES.tile_size / 2)
        self.set_target_position(Point(random_x, random_y))
    #endregion

    def update(self):
        self._try_to_move()
        self._sprite.rect.topleft = (self._rect_in_map.x, self._rect_in_map.y)

    def draw(self, enemy_group: pygame.sprite.Group):
        enemy_group.add(self._sprite)
    
    def _try_to_move(self):
        if not self._target_position: return

        # Calculate the direction to the target
        dx = self._target_position.x - self._rect_in_map.centerx
        dy = self._target_position.y - self._rect_in_map.centery
        distance = math.hypot(dx, dy)
        if distance <= 0: return self.set_random_target()

        # Normalize the direction vector and scale it by the speed
        dx /= distance
        dy /= distance
        dx *= self._speed
        dy *= self._speed

        # Move the enemy
        self.set_center_x(self.get_center_x() + dx)
        self.set_center_y(self.get_center_y() + dy)

        # If the enemy is close enough to the target, stop moving
        if math.hypot(self._target_position.x - self.get_center_x(), self._target_position.y - self.get_center_y()) <= self._speed: 
            self.set_center_x(self._target_position.x)
            self.set_center_y(self._target_position.y)
            self._target_position = None

        if self._target_position is None: self.set_random_target()

