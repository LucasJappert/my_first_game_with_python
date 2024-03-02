import pygame
from src.models.camera import Camera
from src.helpers.resources_helper import RESOURCES
from src.utils.camera_variables import CAMERA_VARIABLES
from src.helpers.my_logger_helper import MyLogger


class Game:
    textures: dict = {}
    running = False
    camera: Camera = None
    
    def initialize(self):
        pygame.init()

        pygame.display.set_caption("My game")

    def end(self):
        self.running = False

    def start(self):
        self.initialize()
        self.running = True
        self.camera = Camera()

        RESOURCES.load_textures()

        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
                
            self.camera.update()

            self.camera.draw()
            
            handle_keyboard_events(self)
        
        pygame.quit()
        MyLogger.green("GAME ENDED!")

def handle_keyboard_events(my_game: Game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.end()
