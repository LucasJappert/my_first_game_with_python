import random

import pygame
from src.models.utils_models import Point
from src.utils.camera_variables import CAMERA_VARIABLES

def get_randome_tile():
    result: Point = Point(0, 0)
    result.x = random.randint(0, CAMERA_VARIABLES.tiles.x -1)
    result.y = random.randint(0, CAMERA_VARIABLES.tiles.y -1)
    return result

def get_center_tile():
    result: Point = Point(0, 0)
    result.x = int(CAMERA_VARIABLES.tiles.x / 2)
    result.y = int(CAMERA_VARIABLES.tiles.y / 2)
    return result

def get_fixed_mouse_position():
    mouse_position = pygame.mouse.get_pos()
    screen_size = pygame.display.get_surface().get_size()
    camera_surface_size = CAMERA_VARIABLES.surface.get_size()
    aux_position_x = int(mouse_position[0] * (camera_surface_size[0]/screen_size[0]))
    aux_position_y = int(mouse_position[1] * (camera_surface_size[1]/screen_size[1]))
    return Point(aux_position_x, aux_position_y)
