import math
import pygame
import src.models.utils_models as UtilsModels
from src.utils.configurations import Configurations
from src.helpers.resources_helper import Resources
from pygame.font import Font
from src.helpers.my_logger_helper import MyLogger
import src.utils.variables as Variables
from src.models.fps import FPS

class Camera:

    @staticmethod
    def initialize():
        Variables.Camera.position.x = 0
        Variables.Camera.position.y = 0
        Variables.Camera.font = pygame.font.SysFont(None, 48)
        Variables.Camera.tile_size = 128 # math.trunc(Configurations.my_screen_size.x / Variables.Camera.tiles.x)
        Variables.Camera.surface = pygame.Surface((Variables.Camera.tiles.x * Variables.Camera.tile_size, Variables.Camera.tiles.y * Variables.Camera.tile_size))
        MyLogger.green(Configurations.my_screen_size)
        screen_size_80 = (math.trunc(Configurations.my_screen_size.x * 0.6), math.trunc(Configurations.my_screen_size.y * 0.6))
        pygame.display.set_mode(screen_size_80, pygame.RESIZABLE)
        
    @staticmethod
    def update():
        FPS.set_fps()

    @staticmethod
    def draw():
        Variables.Camera.surface.fill((0, 0, 0))
        _draw_terrain()

        _draw_ui()



def _draw_terrain():
    grass = Resources.textures["grass"]
    for x in range(Variables.Camera.tiles.x):
        for y in range(Variables.Camera.tiles.y):
            rect = pygame.Rect(x * Variables.Camera.tile_size, y * Variables.Camera.tile_size, Variables.Camera.tile_size, Variables.Camera.tile_size)
            Variables.Camera.surface.blit(grass, rect)
            if Variables.Camera.draw_grid:
                pygame.draw.rect(Variables.Camera.surface, (0, 0, 0), rect, 1)

def _draw_ui():
    fps_text = Variables.Camera.font.render(f"FPS: {Variables.Camera.fps}", True, (255, 255, 255))
    Variables.Camera.surface.blit(fps_text, (10, 10))


