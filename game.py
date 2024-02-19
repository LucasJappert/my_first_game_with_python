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

            # # Obtiene el tamaño actual de la pantalla
            # screen_size = pygame.display.get_surface().get_size()

            # # Escala la superficie de buffer al tamaño de la pantalla
            # scaled_surface = pygame.transform.scale(Game.buffer_surface, screen_size)

            # # Dibuja la superficie escalada en la pantalla
            # pygame.display.get_surface().blit(Game.surface, (0, 0))

            # Actualiza la pantalla
            pygame.display.flip()
        
        print("Game ended")

def keyboad_checks():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()