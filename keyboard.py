import pygame
pressed_keys = pygame.key.get_pressed()

def set_pressed_keys():
    pressed_keys = pygame.key.get_pressed()

def pressed_key(key: int):
    return pressed_keys[key]

def pressed_keys():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    if pressed_keys[pygame.K_UP]:
        print("UP")

    return pressed_keys