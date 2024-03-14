from enum import Enum
import math
import pygame
from src.models.tile_interface import TileInterface
from src.models.tile_model import Tile
from src.models.general_enums import MapObjectType
from src.helpers.resources_helper import get_scaled_image, GeneralTextures, DIRECTIONS
from src.models.utils_models import Point
from src.models.my_sprite_model import MySprite
from src.utils.map_variables import MAP_VARIABLES
import src.utils.map_utils as map_utils
import math
import heapq


class MapObject():
    _target_position: Point = None
    _tile_in: TileInterface = None
    _name: str = ""
    _speed: float = 1
    _object_type: MapObjectType = MapObjectType.ENEMY
    _sprite: MySprite = None
    _direction: str = DIRECTIONS[0]
    _current_frame: int = 1
    _frame_counter = 0
    _frame_rate = 10
    _scale_respect_to_tile: float = 2
    _collide_circle_radius: int = 30
    
    def __init__(self, tile_in: Tile, name: str, object_type: MapObjectType):
        self._name = name
        self._set_my_tile_in(tile_in)
        tile_in.set_blocked(True)
        self._object_type = object_type

        if object_type == MapObjectType.PLAYER:
            self._set_texture()

        if object_type == MapObjectType.ENEMY:
            self._scale_respect_to_tile = 1.5
            self._set_texture()
            # self._set_random_target()

    #region GETTERs
    def _get_rect_in_map(self):
        return self._sprite.rect
    #endregion

    #region SETTERs
    def _set_direction_from_dx_dy(self, dx: float, dy: float):
        if abs(dx) > abs(dy):
            if dx > 0: self._set_direction(DIRECTIONS[2])
            else: self._set_direction(DIRECTIONS[1])
        else:
            if dy > 0: self._set_direction(DIRECTIONS[0])
            else: self._set_direction(DIRECTIONS[3])
    def _set_direction(self, direction: str):
        self._direction = direction
        self._set_texture()
    def _set_target_position(self, target_position: Point):
        self._target_position = target_position
        if target_position is None:
            self._current_frame = 2
            self._set_texture()
    def _set_my_tile_in(self, tile: Tile):
        self._tile_in = tile
        if self._sprite is not None:
            self._sprite.set_top_left_for_map_object(self._tile_in, self._collide_circle_radius)
    def _set_random_target(self):
        random_tile = map_utils.get_random_tile()
        random_x = random_tile.x * MAP_VARIABLES.tile_size.x + int(MAP_VARIABLES.tile_size.x / 2)
        random_y = random_tile.y * MAP_VARIABLES.tile_size.y + int(MAP_VARIABLES.tile_size.y / 2)
        self._set_target_position(Point(random_x, random_y))
    def _set_speed(self, value: float):
        self._speed = value
    def _set_texture(self):
        texture_key = f"{self._name}_{self._direction}_{self._current_frame}"
        texture = get_scaled_image(texture_key, int(MAP_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(MAP_VARIABLES.tile_size.y * self._scale_respect_to_tile))
        # if self._object_type == MapObjectType.ENEMY: texture = get_scaled_image(texture_key)
        # else: texture = get_scaled_image(texture_key, int(MAP_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(MAP_VARIABLES.tile_size.y * self._scale_respect_to_tile))
        self._sprite = MySprite(texture)
        self._sprite.set_top_left_for_map_object(self._tile_in, self._collide_circle_radius)
        
    def _try_set_next_frame(self):
        if self._target_position is None: return
        self._frame_counter += 1
        if self._frame_counter >= self._frame_rate:
            self._frame_counter = 0
            self._current_frame += 1
            if self._current_frame > 3: self._current_frame = 1
            self._set_texture()
    
    #endregion

    def update(self):
        self._try_set_next_frame()
        self._try_to_move()

    def draw(self, map_objects_group: pygame.sprite.Group):
        map_objects_group.add(self._sprite)
        

    def get_tuple_to_use_in_blits(self):
        return (self._sprite.image, self._sprite.rect)

    def _try_to_move(self):
        # FIXME
        if self._target_position is None: return

        # Calculate the direction to the target
        dx = self._target_position.x - self._tile_in.x
        dy = self._target_position.y - self._tile_in.y
        distance = math.hypot(dx, dy)
        if distance <= 0: return self._set_target_position(None)

        # Normalize the direction vector and scale it by the speed
        dx /= distance
        dy /= distance
        dx *= self._speed
        dy *= self._speed

        self._set_direction_from_dx_dy(dx, dy)

        self._set_my_tile_in(self.get_center_x() + dx, self.get_center_y() + dy)

        # If the object is close enough to the target, stop moving
        if math.hypot(self._target_position.x - self.get_center_x(), self._target_position.y - self.get_center_y()) <= self._speed:
            self._set_my_tile_in(self._target_position.x, self._target_position.y)
            self._set_target_position(None)

        if self._target_position is None and self._object_type == MapObjectType.ENEMY:
            self._set_random_target()

    def find_shortest_path(self, target_position: Point):
        pass
    
    def is_collision_with_obstacle(self, next_position: tuple[int, int], obstacles: list[list[bool]]):
        # Calcula el área de colisión del personaje en la siguiente posición
        next_collision_area = (next_position[0], next_position[1], self._collide_circle_radius)

        # Comprueba si el área de colisión del personaje se superpone con algún obstáculo
        for obstacle in obstacles:
            if self.is_collision(next_collision_area, obstacle):
                return True

        return False

    def is_collision(self, circle1: tuple[int, int, int], circle2: tuple[int, int, int]):
        # Comprueba si dos círculos se superponen
        distance = math.sqrt((circle1[0] - circle2[0])**2 + (circle1[1] - circle2[1])**2)
        return distance <= circle1[2] + circle2[2]

    def get_path(self):
        return self.find_shortest_path()

