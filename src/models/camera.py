import pygame
from src.helpers.resources_helper import RESOURCES, get_sacaled_image, ResourcesNames
from src.helpers.my_logger_helper import MyLogger
from src.models.fps import FPS
from src.utils.camera_variables import CAMERA_VARIABLES
from src.models.my_sprite import MyTransparentSprite

class Camera:
    tilemap = None

    def __init__(self):
        CAMERA_VARIABLES.initialize()
        
    def update(self):
        FPS.set_fps()

    def draw(self):
        CAMERA_VARIABLES.surface.fill((0, 0, 0))
        _draw_terrain()

        _draw_ui()

        _scale_and_blit()

        CAMERA_VARIABLES.clock.tick(60)


def _scale_and_blit():
    # Get the size of the screen
    screen_size = pygame.display.get_surface().get_size()

    # Scale the surface to the size of the screen
    scaled_surface = pygame.transform.scale(CAMERA_VARIABLES.surface, screen_size)

    # Draw the scaled surface to the screen
    pygame.display.get_surface().blit(scaled_surface, (0, 0))

    # Update the display
    pygame.display.flip()


def _draw_terrain():
    group = pygame.sprite.Group()
    grass = get_sacaled_image(ResourcesNames.GRASS.value, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
    square = get_sacaled_image(ResourcesNames.SQUARE.value, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
    for x in range(CAMERA_VARIABLES.tiles.x):
        for y in range(CAMERA_VARIABLES.tiles.y):
            my_grass_sprite = MyTransparentSprite(grass, x * CAMERA_VARIABLES.tile_size, y * CAMERA_VARIABLES.tile_size)
            group.add(my_grass_sprite)
            if CAMERA_VARIABLES.draw_grid:
                my_square_sprite = MyTransparentSprite(square, x * CAMERA_VARIABLES.tile_size, y * CAMERA_VARIABLES.tile_size)
                group.add(my_square_sprite)

    group.draw(CAMERA_VARIABLES.surface)

    for x in range(CAMERA_VARIABLES.tiles.x):
        x_axis = CAMERA_VARIABLES.font.render(f"{x}", True, (0, 0, 0))
        CAMERA_VARIABLES.surface.blit(x_axis, ((x+1) * CAMERA_VARIABLES.tile_size - 20, 10))



    # Dibujar el tilemap en la superficie de la cámara
    # if Camera.tilemap is None:
    # Camera.tilemap = create_tilemap()
    # CAMERA_VARIABLES.surface.blit(Camera.tilemap, (0, 0))

def create_tilemap():
    # Crear una nueva superficie para el tilemap
    tilemap = pygame.Surface((CAMERA_VARIABLES.tiles.x * CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tiles.y * CAMERA_VARIABLES.tile_size))

    # Dibujar cada tile en la superficie del tilemap
    grass = get_sacaled_image(ResourcesNames.GRASS.value, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
    square = get_sacaled_image(ResourcesNames.SQUARE.value, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
    for x in range(CAMERA_VARIABLES.tiles.x):
        for y in range(CAMERA_VARIABLES.tiles.y):
            rect = pygame.Rect(x * CAMERA_VARIABLES.tile_size, y * CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size, CAMERA_VARIABLES.tile_size)
            tilemap.blit(grass, rect)
            if CAMERA_VARIABLES.draw_grid:
                tilemap.blit(square, rect)

    # Devolver la superficie del tilemap
    return tilemap

def _draw_ui():
    fps_text = CAMERA_VARIABLES.font.render(f"FPS: {CAMERA_VARIABLES.fps}", True, (255, 255, 255))
    CAMERA_VARIABLES.surface.blit(fps_text, (10, CAMERA_VARIABLES.tile_size * CAMERA_VARIABLES.tiles.y - 50))


