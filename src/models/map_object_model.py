import copy
from enum import Enum
import math
import random
import pygame
from src.models.tile_model import Tile
from src.models.general_enums import MapObjectType
from src.helpers.resources_helper import get_scaled_image, GeneralTextures, DIRECTIONS
from src.models.utils_models import Point
from src.models.my_sprite_model import MySprite
from src.utils.map_variables import MAP_VARIABLES
import src.utils.map_utils as map_utils
import math
from src.helpers.path_finder_helper import PATH_FINDER

class MapObject():
    _target_position: Point = None
    """
    The target position where the object is moving to. If None, the object is not moving. \n
    The x and y coordinates are in pixels.
    """
    _current_position: Point = None
    """
    The target position where the object is moving to. If None, the object is not moving. \n
    The x and y coordinates are in pixels.
    """
    _tile_in: Tile = None
    _tiles_info: dict[str, Tile] = {}
    _name: str = ""
    _speed: float = 1
    _object_type: MapObjectType = MapObjectType.ENEMY
    _sprites: dict[str, MySprite] = {}
    _current_sprite_key: str = ""
    _sprite: MySprite = None
    _direction: str = DIRECTIONS[0]
    _current_frame: int = 1
    _frame_counter = 0
    _frame_rate = 10
    _scale_respect_to_tile: float = 2
    _collide_circle_radius: int = 30
    _current_path: list[Point] = []
    _draw_path = True

    def __init__(self, tile_in: Tile, name: str, object_type: MapObjectType, tiles_info: dict[str, Tile]):
        self._tiles_info = tiles_info
        self._name = name
        self._set_my_tile_in(tile_in)
        self._object_type = object_type
        self._set_current_position(tile_in.get_position_in_pixels().x, tile_in.get_position_in_pixels().y)

        self._set_sprites()
        self._current_sprite_key = self._get_sprite_key(self._direction, self._current_frame)
        
        if object_type == MapObjectType.PLAYER:
            self._set_texture()

        if object_type == MapObjectType.ENEMY:
            self._scale_respect_to_tile = 1.5
            self._set_texture()


    #region GETTERs
    def _get_rect_in_map(self):
        return self._sprite.rect
    def _get_random_unblocked_point(self):
        unblocked_tiles = [tile for tile in self._tiles_info.values() if not tile._blocked]
        if len(unblocked_tiles) == 0: return None
        unblocked_tile = random.choice(unblocked_tiles)
        return unblocked_tile.get_position()
    def _get_sprite_key(self, direction: str, frame: int):
        return f"{self._name}_{direction}_{frame}"
    #endregion

    #region SETTERs
    def _set_sprites(self):
        for direction in DIRECTIONS:
            for frame in range(1, 4):
                texture_key = self._get_sprite_key(direction, frame)
                texture = get_scaled_image(texture_key, int(MAP_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(MAP_VARIABLES.tile_size.y * self._scale_respect_to_tile))
                self._sprites[texture_key] = MySprite(texture)
    
    def _set_direction_from_dx_dy(self, dx: float, dy: float):
        #TODO: Check abs function
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
    def _set_my_tile_in(self, new_tile_in: Tile):
        if self._tile_in is not None:
            self._tile_in.set_blocked(False)
        self._tile_in = new_tile_in
        self._tile_in.set_blocked(True)
    def _set_current_position(self, x: int, y: int):
        self._current_position = Point(x, y)
        if self._sprite is not None:
            self._sprite.set_top_left_for_map_object(self._current_position)
    def _set_random_target(self):
        random_tile = map_utils.get_random_tile()
        random_x = random_tile.x * MAP_VARIABLES.tile_size.x + int(MAP_VARIABLES.tile_size.x / 2)
        random_y = random_tile.y * MAP_VARIABLES.tile_size.y + int(MAP_VARIABLES.tile_size.y / 2)
        self._set_target_position(Point(random_x, random_y))
    def _set_speed(self, value: float):
        self._speed = value
        
    def _set_texture(self):#TODO: REPLACE
        texture_key = f"{self._name}_{self._direction}_{self._current_frame}"
        texture = get_scaled_image(texture_key)
        self._sprite = MySprite(texture)
        self._sprite.set_top_left_for_map_object(self._current_position)

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
        if self._object_type == MapObjectType.ENEMY:
            if self._target_position is None and len(self._current_path) == 0:
                if random.randint(0, 100) < 1:
                    random_unblocked_point = self._get_random_unblocked_point()
                    self.find_and_set_shortest_path(random_unblocked_point)

        self._try_set_next_frame()
        self._try_to_move()

    def draw(self, map_objects_group: pygame.sprite.Group):
        map_objects_group.add(self._sprite)

    def draw_path(self, map_objects_group: pygame.sprite.Group):
        if not self._draw_path: return
        if len(self._current_path) == 0: return

        for point in self._current_path:
            sprite = MySprite(get_scaled_image(GeneralTextures.CROSS.name, MAP_VARIABLES.tile_size.x, MAP_VARIABLES.tile_size.y))
            sprite.set_top_left((point.x - 1) * MAP_VARIABLES.tile_size.x, (point.y - 1) * MAP_VARIABLES.tile_size.y)
            map_objects_group.add(sprite)

    def _try_to_move(self):
        # return
        if self._target_position is None:
            if len(self._current_path) == 0: return

            next_tile_to_move = self._current_path.pop(0)

            new_tile_in = self._tiles_info[Tile.get_tile_key(next_tile_to_move.x, next_tile_to_move.y)]
            self._set_my_tile_in(new_tile_in)

            target_x = int((next_tile_to_move.x - 0.5) * self._tile_in._size.x)
            target_y = int((next_tile_to_move.y - 0.5) * self._tile_in._size.y)
            self._set_target_position(Point(target_x, target_y))

        # Calculate the direction to the target
        dx = self._target_position.x - self._current_position.x
        dy = self._target_position.y - self._current_position.y
        distance = math.hypot(dx, dy)
        if distance <= 0: return self._set_target_position(None)

        # Normalize the direction vector and scale it by the speed
        dx /= distance
        dy /= distance
        dx *= self._speed
        dy *= self._speed

        self._set_direction_from_dx_dy(dx, dy)

        self._set_current_position(self._current_position.x + dx, self._current_position.y + dy)

        # If the object is close enough to the target, stop moving
        if math.hypot(self._target_position.x - self._current_position.x, self._target_position.y - self._current_position.y) <= self._speed:
            self._set_current_position(self._target_position.x, self._target_position.y)
            self._set_target_position(None)


    def find_and_set_shortest_path(self, target_point: Point):
        result = PATH_FINDER.find_path(self._tile_in.get_position(), target_point)
        self._current_path = result

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


