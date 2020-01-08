from typing import List
import pygame

import sprites
import ship
import game_board

FONT_PATH = 'assets/FutilePro.ttf'


def create_text(text, size, color):
    font = pygame.font.Font(FONT_PATH, size)
    image = font.render(text, True, color)
    return image


def draw_ships(board: game_board.GameBoard, ships: List[ship.Ship]):
    # --------- BEGIN YOUR CODE ----------

    # draw the ships by adding the appropriate sprites to the board
    pass  # <-- remove this

    # --------- END YOUR CODE ----------
