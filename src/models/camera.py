import pygame
from src.helpers.resources_helper import RESOURCES, get_scaled_image, ResourcesNames
from src.helpers.my_logger_helper import MyLogger
from src.models.fps import FPS
from src.utils.camera_variables import CAMERA_VARIABLES
from src.models.map_model import MAP
from src.models.my_sprite import MyTransparentSprite
from src.utils.map_utils import get_fixed_mouse_position
from src.models.map_object_model import MapObject

class Camera:
    _tilemap = None

    def initialize(self):
        CAMERA_VARIABLES.initialize()
        RESOURCES.load_textures()
        
    def update(self):
        FPS.set_fps()

        for enemy in MAP.enemies:
            enemy.update()

        MAP.my_player.update()

    def draw(self):
        CAMERA_VARIABLES.surface.fill((0, 0, 0))
        _draw_terrain()

        map_objects_group = pygame.sprite.Group()
        _draw_mouse_square(map_objects_group)

        for obj in _get_ordered_map_objects():
            obj.draw(map_objects_group)

        map_objects_group.draw(CAMERA_VARIABLES.surface)

        _draw_ui()

        _scale_and_blit()

        CAMERA_VARIABLES.clock.tick(60)

CAMERA = Camera()


def _scale_and_blit():
    # Get the size of the screen
    screen_size = pygame.display.get_surface().get_size()

    # Scale the surface to the size of the screen
    scaled_surface = pygame.transform.scale(CAMERA_VARIABLES.surface, screen_size)

    # Draw the scaled surface to the screen
    pygame.display.get_surface().blit(scaled_surface, (0, 0))
    # pygame.display.get_surface().blits([(scaled_surface, (0, 0))] * 2)

    # Update the display
    pygame.display.flip()

def _draw_terrain():
    # group = pygame.sprite.Group()
    # grass = get_sacaled_image(ResourcesNames.GRASS.name, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
    # square = get_sacaled_image(ResourcesNames.SQUARE.name, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
    # for x in range(CAMERA_VARIABLES.tiles.x):
    #     for y in range(CAMERA_VARIABLES.tiles.y):
    #         my_grass_sprite = MyTransparentSprite(grass, x * CAMERA_VARIABLES.tile_size.x, y * CAMERA_VARIABLES.tile_size.y)
    #         group.add(my_grass_sprite)
    #         if CAMERA_VARIABLES.draw_grid:
    #             my_square_sprite = MyTransparentSprite(square, x * CAMERA_VARIABLES.tile_size.x, y * CAMERA_VARIABLES.tile_size.y)
    #             group.add(my_square_sprite)

    # group.draw(CAMERA_VARIABLES.surface)

    # if CAMERA_VARIABLES.draw_grid:
    #     for x in range(CAMERA_VARIABLES.tiles.x):
    #         x_axis = CAMERA_VARIABLES.font.render(f"{x+1}", True, (0, 0, 0))
    #         CAMERA_VARIABLES.surface.blit(x_axis, ((x+1) * CAMERA_VARIABLES.tile_size.x - 60, 10))

    # Dibujar el tilemap en la superficie de la cámara
    if Camera._tilemap is None:
        Camera._tilemap = _create_tilemap()
    CAMERA_VARIABLES.surface.blit(Camera._tilemap, (0, 0))

def _create_tilemap():
    # Crear una nueva superficie para el tilemap
    tilemap = pygame.Surface((CAMERA_VARIABLES.tiles.x * CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tiles.y * CAMERA_VARIABLES.tile_size.y))

    # Dibujar cada tile en la superficie del tilemap
    grass = get_scaled_image(ResourcesNames.GRASS.name, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
    square = get_scaled_image(ResourcesNames.SQUARE.name, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
    for x in range(CAMERA_VARIABLES.tiles.x):
        for y in range(CAMERA_VARIABLES.tiles.y):
            rect = pygame.Rect(x * CAMERA_VARIABLES.tile_size.x, y * CAMERA_VARIABLES.tile_size.y, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y)
            CAMERA_VARIABLES.surface.blit(grass, rect)
            tilemap.blit(grass, rect)
            if CAMERA_VARIABLES.draw_grid:
                pygame.draw.rect(CAMERA_VARIABLES.surface, (0, 0, 0), rect, 1)
                tilemap.blit(square, rect)

    # Devolver la superficie del tilemap
    return tilemap

def _draw_ui():
    fps_text = CAMERA_VARIABLES.font.render(f"FPS: {CAMERA_VARIABLES.fps}", True, (255, 255, 255))
    CAMERA_VARIABLES.surface.blit(fps_text, (10, CAMERA_VARIABLES.tile_size.y * CAMERA_VARIABLES.tiles.y - 50))

def _draw_mouse_square(map_objects_group: pygame.sprite.Group):
        fixed_mouse_position = get_fixed_mouse_position()
        topleft_x = int(fixed_mouse_position.x - CAMERA_VARIABLES.tile_size.x / 2)
        topleft_y = int(fixed_mouse_position.y - CAMERA_VARIABLES.tile_size.y / 2)
        square = MyTransparentSprite(get_scaled_image(ResourcesNames.SQUARE.name, CAMERA_VARIABLES.tile_size.x, CAMERA_VARIABLES.tile_size.y))
        square.set_top_left(topleft_x, topleft_y)
        map_objects_group.add(square)
        # square_text = CAMERA_VARIABLES.font.render(f"x: {fixed_mouse_position.x}, y: {fixed_mouse_position.y}", True, (255, 255, 255))
        # CAMERA_VARIABLES.surface.blit(square_text, (200, 200))

def _get_ordered_map_objects():
    objects: list[MapObject] = []
    for enemy in MAP.enemies:
        objects.append(enemy)
    objects.append(MAP.my_player)

    ordered_list = sorted(objects, key=lambda obj: (obj.get_center_y(), obj.get_center_x()))

    return ordered_list

