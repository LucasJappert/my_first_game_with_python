import math
import pygame
import src.models.utils_models as UtilsModels
from pygame.font import Font
import tkinter

root = tkinter.Tk()

class CameraVariables:
    tiles = UtilsModels.Point(25, 25)
    position = UtilsModels.Point(0, 0)
    font: Font = None
    clock = pygame.time.Clock()
    draw_grid = True
    tile_size = 64
    surface: pygame.Surface = None
    fps = 0
    
    def initialize(self):
        self.position.x = 0
        self.position.y = 0
        self.font = pygame.font.SysFont(None, 48)
        self.surface = pygame.Surface((self.tiles.x * self.tile_size, self.tiles.y * self.tile_size))
        
        my_full_screen_size = UtilsModels.Point(root.winfo_screenwidth(), root.winfo_screenheight())
        game_screen_size = (math.trunc(my_full_screen_size.x * 0.8), math.trunc(my_full_screen_size.y * 0.8))
        pygame.display.set_mode(game_screen_size, pygame.DOUBLEBUF)   
    
CAMERA_VARIABLES = CameraVariables()
