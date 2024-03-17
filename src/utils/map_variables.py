import math
import tkinter

import pygame
from src.models.utils_models import Point
from pygame.font import Font

_fix_multiplier = 0.6
cols = 25
rows = 15
TILES_GRID_COL_ROW = Point(cols, rows)


root = tkinter.Tk()
screen_size_aux: Point = Point(int(1920*_fix_multiplier), int(1080*_fix_multiplier))
TILE_SIZE: int = 96



class MapVariables:
    TILES_GRID_COL_ROW = TILES_GRID_COL_ROW
    # tile_size = Point(math.trunc(screen_size_aux.x / TILES_GRID_COL_ROW.x), math.trunc(screen_size_aux.y / TILES_GRID_COL_ROW.y))
    tile_size = Point(TILE_SIZE, TILE_SIZE)
    font: Font = None
    clock = pygame.time.Clock()
    draw_grid = True
    surface: pygame.Surface = None
    fps = 0
    
    def initialize(self):
        self.font = pygame.font.SysFont(None, int(40 * _fix_multiplier))
        # screen_size = (TILES_GRID_COL_ROW.x * self.tile_size.x, TILES_GRID_COL_ROW.y * self.tile_size.y)
        # my_full_screen_size = Point(root.winfo_screenwidth(), root.winfo_screenheight())
        # game_screen_size = (math.trunc(my_full_screen_size.x * 0.8), math.trunc(my_full_screen_size.y * 0.8))
        
        my_full_screen_size = Point(root.winfo_screenwidth(), root.winfo_screenheight())
        screen_size_game = (math.trunc(my_full_screen_size.x * 0.80), math.trunc(my_full_screen_size.y * 0.80))
        self.tile_size = Point(math.trunc(screen_size_game[0] / cols), math.trunc(screen_size_game[1] / rows))
        self.surface = pygame.Surface((self.tile_size.x * cols, self.tile_size.y * rows))
        
        pygame.display.set_mode(self.surface.get_size())
        print(f"tile_size: {self.tile_size.x}x{self.tile_size.y}")
        print(f"surface: {self.surface.get_size()}")
        print(f"game_screen_size: {screen_size_game}")

    
MAP_VARIABLES = MapVariables()
