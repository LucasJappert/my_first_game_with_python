import pygame
from pygame import Surface

from src.helpers.resources_helper import Resources

class MyTransparentSprite(pygame.sprite.Sprite):
    def __init__(self, texture: pygame.Surface, topleft_x: int, topleft_y: int):
        super().__init__()
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.topleft = (topleft_x, topleft_y)

    
