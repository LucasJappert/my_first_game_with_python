import pygame

class MySpriteInterface(pygame.sprite.Sprite):
    image: pygame.Surface = None
    rect: pygame.Rect = None
    
    def __init__(self):
        super().__init__()
    
    def set_top_left(self, x: int, y: int):
        pass
