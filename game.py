import math
import pygame
from configurations import Configurations
from screen_resources import ScreenResources
from visible_screen import VisibleScreen
from resources import Resources
from screeninfo import get_monitors


class Game:
    window_surface: pygame.Surface = None
    textures: dict = {}

    @staticmethod
    def initialize():
        monitor = get_monitors()[0]
        screen_size_80 = (monitor.width*0.8, monitor.height*0.8)
        Configurations.tile_size = math.trunc(screen_size_80[0] / VisibleScreen.tiles.x)

        pygame.init()
        ScreenResources.surface = pygame.Surface((VisibleScreen.tiles.x * Configurations.tile_size, VisibleScreen.tiles.y * Configurations.tile_size))

        pygame.display.set_caption("Game")
        pygame.display.set_mode(screen_size_80, pygame.RESIZABLE)


    @staticmethod
    def start_game():
        Game.initialize()
        Resources.load_textures()
        VisibleScreen.initialize()

        while True:
            keyboad_checks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            ScreenResources.surface.fill((0, 0, 0))
            VisibleScreen.draw()
            _scale_and_blit()
        
        print("Game ended")

def _scale_and_blit():
    # Get the size of the screen
    screen_size = pygame.display.get_surface().get_size()

    # Scale the surface to the size of the screen
    scaled_surface = pygame.transform.scale(ScreenResources.surface, screen_size)

    # Draw the scaled surface to the screen
    pygame.display.get_surface().blit(scaled_surface, (0, 0))

    # Update the display
    pygame.display.flip()

def keyboad_checks():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()