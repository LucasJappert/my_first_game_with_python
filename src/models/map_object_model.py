from enum import Enum
import math
import pygame
from src.models.general_enums import MapObjectType
from src.helpers.resources_helper import get_scaled_image, ResourcesNames, DIRECTIONS
from src.models.utils_models import Point
from src.models.my_sprite import MyTransparentSprite
from src.utils.camera_variables import CAMERA_VARIABLES
import src.utils.map_utils as map_utils


class MapObject():
    _target_position: Point = None
    _rect_in_map: pygame.Rect = None
    _my_position: Point = Point(0, 0)
    _name: str = ""
    _speed: float = 1
    _object_type: MapObjectType = MapObjectType.ENEMY
    _sprite: MyTransparentSprite = None
    _direction: str = DIRECTIONS[0]
    _current_frame: int = 1
    _frame_counter = 0
    _frame_rate = 10
    _scale_respect_to_tile: float = 1.0

    
    def __init__(self, center_position: Point, name: str, object_type: MapObjectType):
        self._name = name
        self._rect_in_map = pygame.Rect(center_position.x, center_position.y, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
        self.set_center_x(center_position.x)
        self.set_center_y(center_position.y)
        self._rect_in_map.width = CAMERA_VARIABLES.tile_size.x
        self._rect_in_map.height = CAMERA_VARIABLES.tile_size.y
        self._object_type = object_type

        if object_type == MapObjectType.PLAYER:
            self.set_texture()

        if object_type == MapObjectType.ENEMY:
            self._scale_respect_to_tile = 0.4
            self.set_texture()
            self.set_random_target()

    #region GETTERs
    def get_center_x(self):
        return self._rect_in_map.centerx
    
    def get_center_y(self):
        return self._rect_in_map.centery
    #endregion

    #region SETTERs
    def set_direction(self, direction: str):
        self._direction = direction
        self.set_texture()
    def set_target_position(self, target_position: Point):
        self._target_position = target_position
        if target_position is None:
            self._current_frame = 2
            self.set_texture()
    def set_center_x(self, value: int):
        self._my_position.x = value
        self._rect_in_map.centerx = value
    def set_center_y(self, value: int):
        self._my_position.y = value
        self._rect_in_map.centery = value
    def set_random_target(self):
        random_tile = map_utils.get_randome_tile()
        random_x = random_tile.x * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.x / 2)
        random_y = random_tile.y * CAMERA_VARIABLES.tile_size.y + int(CAMERA_VARIABLES.tile_size.y / 2)
        self.set_target_position(Point(random_x, random_y))
    def set_speed(self, value: float):
        self._speed = value
    def set_texture(self):
        texture_key = f"{self._name}_{self._direction}_{self._current_frame}"
        texture = get_scaled_image(texture_key, int(CAMERA_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(CAMERA_VARIABLES.tile_size.y * self._scale_respect_to_tile))
        topleft_x = self._rect_in_map.centerx - int(texture.get_width() / 2)
        topleft_y = self._rect_in_map.centery - int(texture.get_height() / 2)
        self._sprite = MyTransparentSprite(texture, topleft_x, topleft_y)
        
    def _try_set_next_frame(self):
        if self._target_position is None: return
        self._frame_counter += 1
        if self._frame_counter >= self._frame_rate:
            self._frame_counter = 0
            self._current_frame += 1
            if self._current_frame > 3: self._current_frame = 1
            self.set_texture()
    #endregion

    def update(self):
        self._try_set_next_frame()
        self._try_to_move()
        self._sprite.rect.topleft = (self._rect_in_map.x, self._rect_in_map.y)

    def draw(self, map_objects_group: pygame.sprite.Group):
        map_objects_group.add(self._sprite)

    def get_tuple_to_use_in_blits(self):
        return (self._sprite.image, self._sprite.rect)

    def _try_to_move(self):
        if self._target_position is None: return

        # Calculate the direction to the target
        dx = self._target_position.x - self._rect_in_map.centerx
        dy = self._target_position.y - self._rect_in_map.centery
        distance = math.hypot(dx, dy)
        if distance <= 0: return self.set_target_position(None)

        # Normalize the direction vector and scale it by the speed
        dx /= distance
        dy /= distance
        dx *= self._speed
        dy *= self._speed

        # Set the direction
        if abs(dx) > abs(dy):
            if dx > 0: self.set_direction(DIRECTIONS[2])
            else: self.set_direction(DIRECTIONS[1])
        else:
            if dy > 0: self.set_direction(DIRECTIONS[0])
            else: self.set_direction(DIRECTIONS[3])

        # Move the enemy
        self.set_center_x(self.get_center_x() + dx)
        self.set_center_y(self.get_center_y() + dy)

        # If the enemy is close enough to the target, stop moving
        if math.hypot(self._target_position.x - self.get_center_x(), self._target_position.y - self.get_center_y()) <= self._speed: 
            self.set_center_x(self._target_position.x)
            self.set_center_y(self._target_position.y)
            self.set_target_position(None)

        if self._target_position is None and self._object_type == MapObjectType.ENEMY:
            self.set_random_target()

