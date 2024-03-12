import pygame
from src.models.my_screen import MY_SCREEN
from src.helpers.resources_helper import RESOURCES
from src.helpers.my_logger_helper import MyLogger
from src.models.map_model import MAP
from src.utils.map_variables import MAP_VARIABLES


class Game:
    textures: dict = {}
    running = False
    clock = pygame.time.Clock()
    
    def initialize(self):
        pygame.init()
        pygame.display.set_caption("Moo Moo")

        MAP_VARIABLES.initialize()
        RESOURCES.load_textures()
        MAP.initialize()

        self.running = True

    def end(self):
        self.running = False

    def start(self):
        self.initialize()

        while self.running:

            self.update()
            self.draw()
            
            handle_keyboard_events(self)
        
        pygame.quit()
        MyLogger.green("###################### GAME OVER! ######################")

    def update(self):
        MAP.update()
    
    def draw(self):
        MAP_VARIABLES.surface.fill((0, 0, 0))
        
        MAP.draw()
        
        MY_SCREEN.draw_fps()
        MY_SCREEN.scale_and_blit()

        self.clock.tick(60)
            
    
def handle_keyboard_events(my_game: Game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.end()
                
        MAP.handle_events(event)
        MAP._my_player.handle_events(event)
