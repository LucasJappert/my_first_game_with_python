import pygame
from src.models.game import Game

def handle_keyboard_events(my_game: Game):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                my_game.end()
