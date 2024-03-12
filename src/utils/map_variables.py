import math
import tkinter

import pygame
from src.models.utils_models import Point
from pygame.font import Font

TILES_GRID_COL_ROW = Point(25, 15)


root = tkinter.Tk()
screen_size_aux: Point = Point(1920, 1080)
# tile_size: int = 128

class MapVariables:
    TILES_GRID_COL_ROW = TILES_GRID_COL_ROW
    tile_size = Point(math.trunc(screen_size_aux.x / TILES_GRID_COL_ROW.x), math.trunc(screen_size_aux.y / TILES_GRID_COL_ROW.y))
    font: Font = None
    clock = pygame.time.Clock()
    draw_grid = True
    surface: pygame.Surface = None
    fps = 0
    
    def initialize(self):
        print(f"tile_size: {self.tile_size.x}x{self.tile_size.y}")
        self.font = pygame.font.SysFont(None, 48)
        self.surface = pygame.Surface((TILES_GRID_COL_ROW.x * self.tile_size.x, TILES_GRID_COL_ROW.y * self.tile_size.y))
        print(f"surface: {self.surface.get_size()}")
        my_full_screen_size = Point(root.winfo_screenwidth(), root.winfo_screenheight())
        game_screen_size = (math.trunc(my_full_screen_size.x * 0.8), math.trunc(my_full_screen_size.y * 0.8))
        pygame.display.set_mode(game_screen_size, pygame.RESIZABLE)
        print(f"game_screen_size: {game_screen_size}")

    
MAP_VARIABLES = MapVariables()
