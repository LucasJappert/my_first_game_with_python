import pygame
from src.utils.camera_variables import CAMERA_VARIABLES

class FPS:
    last_ticks = 0
    frame_counter = 0
    start_ticks = 0

    @staticmethod
    def set_fps():
        FPS.frame_counter += 1
        current_ticks = pygame.time.get_ticks()
        if current_ticks - FPS.start_ticks > 1000:
            CAMERA_VARIABLES.fps = FPS.frame_counter
            FPS.frame_counter = 0
            FPS.start_ticks = current_ticks
