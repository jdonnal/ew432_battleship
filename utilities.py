from typing import List, Tuple
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

def draw_hits(board: game_board.GameBoard, hits: List[Tuple[int, int]]):
    # --------- BEGIN YOUR CODE ----------

    # add a "hit" sprite at every hit
    pass  # <-- remove this

    # --------- END YOUR CODE ----------


def draw_misses(board: game_board.GameBoard, misses: List[Tuple[int, int]]):
    # --------- BEGIN YOUR CODE ----------

    # add a "miss" sprite at every miss
    pass  # <-- remove this

    # --------- END YOUR CODE ----------
