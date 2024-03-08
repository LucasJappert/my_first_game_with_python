import math
import pygame
import src.models.utils_models as UtilsModels
from pygame.font import Font
import tkinter

root = tkinter.Tk()
screen_size_aux: UtilsModels.Point = UtilsModels.Point(1920, 1080)
tiles = UtilsModels.Point(17, 9)
# tile_size: int = 128

class CameraVariables:
    tiles = tiles
    tile_size = UtilsModels.Point(math.trunc(screen_size_aux.x / tiles.x), math.trunc(screen_size_aux.y / tiles.y))
    screen_size = UtilsModels.Point(0, 0)
    position = UtilsModels.Point(0, 0)
    font: Font = None
    clock = pygame.time.Clock()
    draw_grid = False
    surface: pygame.Surface = None
    fps = 0
    grid_map_busy_state: list[list[bool]] = []
    
    def initialize(self):
        print(f"tile_size: {self.tile_size.x}x{self.tile_size.y}")
        self.screen_size =  UtilsModels.Point(tiles.x * self.tile_size.x, tiles.y * self.tile_size.y)
        self.grid_map_busy_state = [[False for x in range(self.screen_size.x)] for y in range(self.screen_size.y)]
        self.position.x = 0
        self.position.y = 0
        self.font = pygame.font.SysFont(None, 48)
        self.surface = pygame.Surface((self.tiles.x * self.tile_size.x, self.tiles.y * self.tile_size.y))
        
        my_full_screen_size = UtilsModels.Point(root.winfo_screenwidth(), root.winfo_screenheight())
        game_screen_size = (math.trunc(my_full_screen_size.x * 0.8), math.trunc(my_full_screen_size.y * 0.8))
        pygame.display.set_mode(game_screen_size, pygame.RESIZABLE)

    
CAMERA_VARIABLES = CameraVariables()
