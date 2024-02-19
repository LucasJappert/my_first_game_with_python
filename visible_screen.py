import pygame
import models.utils_models as UtilsModels
from configurations import Configurations
from resources import Resources
from pygame.font import Font

from screen_resources import ScreenResources

class VisibleScreen:
    tiles = UtilsModels.Point(14, 9)
    center_position = UtilsModels.Point(0, 0)
    font: Font = None
    clock = pygame.time.Clock()

    @staticmethod
    def initialize():
        VisibleScreen.center_position.x = 0
        VisibleScreen.center_position.y = 0
        VisibleScreen.font = pygame.font.SysFont(None, 48)

    @staticmethod
    def draw():
        _draw_terrain()

        _draw_ui()

def _draw_terrain():
    grass = Resources.textures["grass"]
    for x in range(VisibleScreen.tiles.x):
        for y in range(VisibleScreen.tiles.y):
            rect = pygame.Rect(x * Configurations.tile_size, y * Configurations.tile_size, Configurations.tile_size, Configurations.tile_size)
            ScreenResources.surface.blit(grass, rect)

def _draw_ui():
    milliseconds = VisibleScreen.clock.tick(60)
    fps = int(1000 / milliseconds)
    fps_text = VisibleScreen.font.render(f"FPS: {fps}", True, (255, 255, 255))
    ScreenResources.surface.blit(fps_text, (10, 10))


