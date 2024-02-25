import math
import pygame
from configurations import Configurations
from camera import Camera
from resources import Resources
import variables as Variables


class Game:
    window_surface: pygame.Surface = None
    textures: dict = {}

    @staticmethod
    def initialize():
        pygame.init()

        pygame.display.set_caption("Game")


    @staticmethod
    def start_game():
        Game.initialize()
        Camera.initialize()

        Resources.load_textures()

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            keyboad_checks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            Camera.update()

            Camera.draw()
            _scale_and_blit()
        
        print("Game ended")

def _scale_and_blit():
    # Get the size of the screen
    screen_size = pygame.display.get_surface().get_size()

    # Scale the surface to the size of the screen
    scaled_surface = pygame.transform.scale(Variables.Camera.surface, screen_size)

    # Draw the scaled surface to the screen
    pygame.display.get_surface().blit(scaled_surface, (0, 0))

    # Update the display
    pygame.display.flip()

def keyboad_checks():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
