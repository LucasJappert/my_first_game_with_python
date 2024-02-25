import pygame

class Keyboard:
    
    @staticmethod
    def pressed_key(key: int):
        return pygame.key.get_pressed()[key]
