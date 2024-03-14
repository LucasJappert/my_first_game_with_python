import random

import pygame
from src.models.utils_models import Point
from src.utils.map_variables import MAP_VARIABLES, TILES_GRID_COL_ROW
    
def get_random_tile():
    result: Point = Point(0, 0)
    result.x = random.randint(1, TILES_GRID_COL_ROW.x)
    result.y = random.randint(1, TILES_GRID_COL_ROW.y)
    return result

def get_center_tile():
    result: Point = Point(0, 0)
    result.x = int(TILES_GRID_COL_ROW.x * MAP_VARIABLES.tile_size.x / 2)
    result.y = int(TILES_GRID_COL_ROW.y * MAP_VARIABLES.tile_size.y / 2)
    return result

def get_fixed_mouse_position():
    mouse_position = pygame.mouse.get_pos()
    pygame_screen_size = pygame.display.get_surface().get_size()
    camera_surface_size = MAP_VARIABLES.surface.get_size()
    aux_position_x = int(mouse_position[0] * (camera_surface_size[0]/pygame_screen_size[0]))
    aux_position_y = int(mouse_position[1] * (camera_surface_size[1]/pygame_screen_size[1]))
    return Point(aux_position_x, aux_position_y)

def get_tile_map_from_mouse_position(mouse_position: Point):
    result: Point = Point(0, 0)
    result.x = int(mouse_position.x / MAP_VARIABLES.tile_size.x)
    result.y = int(mouse_position.y / MAP_VARIABLES.tile_size.y)
    return result

