import pygame
import src.models.utils_models as UtilsModels
from pygame.font import Font

tiles = UtilsModels.Point(25, 25)
position = UtilsModels.Point(0, 0)
font: Font = None
clock = pygame.time.Clock()
draw_grid = True
tile_size = 64
surface: pygame.Surface = None
fps = 0
