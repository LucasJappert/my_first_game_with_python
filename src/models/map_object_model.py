from enum import Enum
import math
import pygame
from src.models.general_enums import MapObjectType
from src.helpers.resources_helper import get_scaled_image, ResourcesNames, DIRECTIONS
from src.models.utils_models import Point
from src.models.my_sprite import MyTransparentSprite
from src.utils.camera_variables import CAMERA_VARIABLES
import src.utils.map_utils as map_utils
import math
import heapq


class MapObject():
    _target_position: Point = None
    _my_position: Point
    _name: str = ""
    _speed: float = 1
    _object_type: MapObjectType = MapObjectType.ENEMY
    _sprite: MyTransparentSprite = None
    _direction: str = DIRECTIONS[0]
    _current_frame: int = 1
    _frame_counter = 0
    _frame_rate = 10
    _scale_respect_to_tile: float = 1
    _collide_circle_radius: int = 30
    
    def __init__(self, center_position: Point, name: str, object_type: MapObjectType):
        self._name = name
        self._set_my_position(center_position.x, center_position.y)
        self._object_type = object_type

        if object_type == MapObjectType.PLAYER:
            self._set_texture()

        if object_type == MapObjectType.ENEMY:
            self._scale_respect_to_tile = 0.7
            self._set_texture()
            self._set_random_target()

    #region GETTERs
    def get_center_x(self):
        return self._my_position.x
    
    def get_center_y(self):
        return self._my_position.y
    
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
    def _set_my_position(self, x: int, y: int):
        self._my_position = Point(x, y)
        if self._sprite is not None:
            self._sprite.set_top_left_for_map_object(self._my_position, self._collide_circle_radius)
    def _set_random_target(self):
        random_tile = map_utils.get_randome_tile()
        random_x = random_tile.x * CAMERA_VARIABLES.tile_size.x + int(CAMERA_VARIABLES.tile_size.x / 2)
        random_y = random_tile.y * CAMERA_VARIABLES.tile_size.y + int(CAMERA_VARIABLES.tile_size.y / 2)
        self._set_target_position(Point(random_x, random_y))
    def _set_speed(self, value: float):
        self._speed = value
    def _set_texture(self):
        texture_key = f"{self._name}_{self._direction}_{self._current_frame}"
        texture = get_scaled_image(texture_key, int(CAMERA_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(CAMERA_VARIABLES.tile_size.y * self._scale_respect_to_tile))
        # if self._object_type == MapObjectType.ENEMY: texture = get_scaled_image(texture_key)
        # else: texture = get_scaled_image(texture_key, int(CAMERA_VARIABLES.tile_size.x * self._scale_respect_to_tile), int(CAMERA_VARIABLES.tile_size.y * self._scale_respect_to_tile))
        self._sprite = MyTransparentSprite(texture)
        self._sprite.set_top_left_for_map_object(self._my_position, self._collide_circle_radius)
        
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
        #draw the collide circle around the object
        # pygame.draw.circle(CAMERA_VARIABLES.surface, (0, 0, 0), (self.get_center_x(), self.get_center_y()), self._collide_circle_radius)
        

    def get_tuple_to_use_in_blits(self):
        return (self._sprite.image, self._sprite.rect)

    def _try_to_move(self):
        if self._target_position is None: return

        # Calculate the direction to the target
        dx = self._target_position.x - self._my_position.x
        dy = self._target_position.y - self._my_position.y
        distance = math.hypot(dx, dy)
        if distance <= 0: return self._set_target_position(None)

        # Normalize the direction vector and scale it by the speed
        dx /= distance
        dy /= distance
        dx *= self._speed
        dy *= self._speed

        self._set_direction_from_dx_dy(dx, dy)

        self._set_my_position(self.get_center_x() + dx, self.get_center_y() + dy)

        # If the object is close enough to the target, stop moving
        if math.hypot(self._target_position.x - self.get_center_x(), self._target_position.y - self.get_center_y()) <= self._speed:
            self._set_my_position(self._target_position.x, self._target_position.y)
            self._set_target_position(None)

        if self._target_position is None and self._object_type == MapObjectType.ENEMY:
            self._set_random_target()

    def find_shortest_path(self):
        start = (self._my_position.x, self._my_position.y)
        target = (self._target_position.x, self._target_position.y)
        # Implementación básica del algoritmo A*

        # Define la función heurística (distancia euclidiana)
        def heuristic(node):
            dx = node[0] - target[0]
            dy = node[1] - target[1]
            return math.sqrt(dx**2 + dy**2)

        # Define los movimientos permitidos (arriba, abajo, izquierda, derecha y diagonales)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        # Inicializa la lista abierta y la lista cerrada
        open_list = []
        closed_list = set()

        # Inicializa el nodo de inicio y lo agrega a la lista abierta
        heapq.heappush(open_list, (0, start))
        
        # Inicializa el diccionario came_from
        came_from = {}
        
        while open_list:
            # Extrae el nodo con el costo más bajo de la lista abierta
            current_cost, current_node = heapq.heappop(open_list)

            # Si el nodo actual es el nodo objetivo, reconstruye el camino y devuélvelo
            if current_node == target:
                path = []
                while current_node != start:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.append(start)
                return list(reversed(path))

            # Agrega el nodo actual a la lista cerrada
            closed_list.add(current_node)

            obstacles = CAMERA_VARIABLES.grid_map_busy_state
            # Genera los sucesores del nodo actual
            for move in movements:
                next_node = (current_node[0] + move[0], current_node[1] + move[1])

                # Si el sucesor está fuera del mapa, o es un obstáculo, o ya está en la lista cerrada, ignóralo
                if next_node[0] < 0 or next_node[0] >= len(obstacles) or next_node[1] < 0 or next_node[1] >= len(obstacles[0]) or obstacles[next_node[0]][next_node[1]]:
                    continue
                
                # Si el sucesor está bloqueado por un obstáculo, ignóralo
                if self.is_collision_with_obstacle(next_node, obstacles):
                    continue

                # Calcula el nuevo costo desde el inicio hasta el sucesor
                new_cost = current_cost + heuristic(next_node)

                # Si el sucesor no está en la lista abierta o el nuevo costo es menor, actualiza su costo y agrega a la lista abierta
                if next_node not in closed_list:
                    heapq.heappush(open_list, (new_cost, next_node))
                    came_from[next_node] = current_node

        # Si no se pudo encontrar un camino, devuelve None
        return None
    
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


