import pygame

FONT_PATH = 'assets/FutilePro.ttf'


def create_text(text, size, color):
    font = pygame.font.Font(FONT_PATH, size)
    image = font.render(text, True, color)
    return image
