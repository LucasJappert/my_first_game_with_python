import math
import pygame
import src.models.utils_models as UtilsModels
from src.utils.configurations import Configurations
from src.helpers.resources_helper import Resources
from pygame.font import Font
from src.helpers.my_logger_helper import MyLogger
from src.models.fps import FPS
import src.utils.camera_variables as camera_variables

class Camera:
    tilemap = None

    def __init__(self):
        camera_variables.position.x = 0
        camera_variables.position.y = 0
        camera_variables.font = pygame.font.SysFont(None, 48)
        camera_variables.tile_size = 128 # math.trunc(Configurations.my_screen_size.x / CameraVariables.tiles.x)
        camera_variables.surface = pygame.Surface((camera_variables.tiles.x * camera_variables.tile_size, camera_variables.tiles.y * camera_variables.tile_size))
        MyLogger.green(Configurations.my_screen_size)
        screen_size_80 = (math.trunc(Configurations.my_screen_size.x * 0.6), math.trunc(Configurations.my_screen_size.y * 0.6))
        pygame.display.set_mode(screen_size_80, pygame.DOUBLEBUF)   
        
    def update(self):
        FPS.set_fps()

    def draw(self):
        camera_variables.surface.fill((0, 0, 0))
        _draw_terrain()

        _draw_ui()

        _scale_and_blit()


def _scale_and_blit():
    # Get the size of the screen
    screen_size = pygame.display.get_surface().get_size()

    # Scale the surface to the size of the screen
    scaled_surface = pygame.transform.scale(camera_variables.surface, screen_size)

    # Draw the scaled surface to the screen
    pygame.display.get_surface().blit(scaled_surface, (0, 0))

    # Update the display
    pygame.display.flip()


def _draw_terrain():
    grass = Resources.textures["grass"]
    square = Resources.textures["square"]
    for x in range(camera_variables.tiles.x):
        for y in range(camera_variables.tiles.y):
            rect = pygame.Rect(x * camera_variables.tile_size, y * camera_variables.tile_size, camera_variables.tile_size, camera_variables.tile_size)
            camera_variables.surface.blit(grass, rect)
            # if camera_variables.draw_grid:
            #     camera_variables.surface.blit(square, rect)

    for x in range(camera_variables.tiles.x):
        x_axis = camera_variables.font.render(f"{x}", True, (255, 255, 255))
        camera_variables.surface.blit(x_axis, ((x+1) * camera_variables.tile_size - 20, 10))



    # Dibujar el tilemap en la superficie de la cámara
    # if Camera.tilemap is None:
    # Camera.tilemap = create_tilemap()
    # camera_variables.surface.blit(Camera.tilemap, (0, 0))

def create_tilemap():
    # Crear una nueva superficie para el tilemap
    tilemap = pygame.Surface((camera_variables.tiles.x * camera_variables.tile_size, camera_variables.tiles.y * camera_variables.tile_size))

    # Dibujar cada tile en la superficie del tilemap
    grass = Resources.textures["grass"]
    square = Resources.textures["square"]
    for x in range(camera_variables.tiles.x):
        for y in range(camera_variables.tiles.y):
            rect = pygame.Rect(x * camera_variables.tile_size, y * camera_variables.tile_size, camera_variables.tile_size, camera_variables.tile_size)
            tilemap.blit(grass, rect)
            if camera_variables.draw_grid:
                tilemap.blit(square, rect)

    # Devolver la superficie del tilemap
    return tilemap

def _draw_ui():
    fps_text = camera_variables.font.render(f"FPS: {camera_variables.fps}", True, (255, 255, 255))
    camera_variables.surface.blit(fps_text, (10, 10))


