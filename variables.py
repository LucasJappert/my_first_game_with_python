import pygame
import models.utils_models as UtilsModels
from pygame.font import Font


class Camera:
    tiles = UtilsModels.Point(31, 19)
    position = UtilsModels.Point(0, 0)
    font: Font = None
    clock = pygame.time.Clock()
    draw_grid = True
    tile_size = 64
    surface: pygame.Surface = None
    fps = 0
