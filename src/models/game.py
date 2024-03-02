import pygame
from src.models.camera import CAMERA
from src.helpers.resources_helper import RESOURCES
from src.utils.camera_variables import CAMERA_VARIABLES
from src.helpers.my_logger_helper import MyLogger
from src.utils.map_variables import MAP


class Game:
    textures: dict = {}
    running = False
    
    def initialize(self):
        pygame.init()

        pygame.display.set_caption("My game")

        CAMERA.initialize()
        MAP.initialize()

        self.running = True

    def end(self):
        self.running = False

    def start(self):
        self.initialize()

        while self.running:
            CAMERA.update()

            CAMERA.draw()
            
            handle_keyboard_events(self)
        
        pygame.quit()
        MyLogger.green("GAME ENDED!")

def handle_keyboard_events(my_game: Game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.end()
