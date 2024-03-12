import pygame
from src.helpers.resources_helper import RESOURCES, get_scaled_image, GeneralTextures
from src.helpers.my_logger_helper import MyLogger
from src.models.fps import FPS
from src.utils.map_variables import MAP_VARIABLES
from src.models.map_model import MAP
from src.models.my_sprite import MyTransparentSprite
import src.utils.map_utils as map_utils
from src.models.map_object_model import MapObject

class MyScreen:
    _tilemap = None
        
    def update(self):
        pass

    def draw(self):
        pass

    def draw_fps(self):
        fps_text = MAP_VARIABLES.font.render(f"FPS: {MAP_VARIABLES.fps}", True, (255, 255, 255))
        MAP_VARIABLES.surface.blit(fps_text, (10, MAP_VARIABLES.TILES_GRID_COL_ROW.y * MAP_VARIABLES.tile_size.y - 50))
        
    def scale_and_blit(self):
        # Get the size of the screen
        screen_size = pygame.display.get_surface().get_size()

        # Scale the surface to the size of the screen
        scaled_surface = pygame.transform.scale(MAP_VARIABLES.surface, screen_size)

        # Draw the scaled surface to the screen
        pygame.display.get_surface().blit(scaled_surface, (0, 0))
        # pygame.display.get_surface().blits([(scaled_surface, (0, 0))] * 2)

        # Update the display
        pygame.display.flip()

MY_SCREEN = MyScreen()

def _draw_mouse_square(map_objects_group: pygame.sprite.Group):
    pass
    # fixed_mouse_position = map_utils.get_fixed_mouse_position()
    # topleft_x = int(fixed_mouse_position.x - MAP_VARIABLES.TILES_GRID_SIZE.x / 2)
    # topleft_y = int(fixed_mouse_position.y - MAP_VARIABLES.TILES_GRID_SIZE.y / 2)
    # square = MyTransparentSprite(get_scaled_image(GeneralTextures.SQUARE.name, MAP_VARIABLES.TILES_GRID_SIZE.x, MAP_VARIABLES.TILES_GRID_SIZE.y))
    # square.set_top_left(topleft_x, topleft_y)
    # map_objects_group.add(square)
    # # square_text = MAP_VARIABLES.font.render(f"x: {fixed_mouse_position.x}, y: {fixed_mouse_position.y}", True, (255, 255, 255))
    # # MAP_VARIABLES.surface.blit(square_text, (200, 200))
    
    # tile = map_utils.get_tile_map_from_mouse_position(fixed_mouse_position)
    # square = 


