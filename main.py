import pygame
from pygame.locals import *
import sys

import players
import sprites
import colors
import utilities
from game_board import GameBoard

BLOCK_SIZE = 30
NBLOCKS = 11
TOP_MARGIN = 30
PADDING = 10


def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(((BLOCK_SIZE * NBLOCKS) * 2 + PADDING * 3,
                                                      BLOCK_SIZE * NBLOCKS + TOP_MARGIN + PADDING))
    screen.fill(colors.screen_bkgd)
    pygame.display.set_caption('USNA Battleship')
    sprites.initialize()

    # size of the game board figure based on BLOCK SIZE pixels
    board_dimension = (BLOCK_SIZE * NBLOCKS, BLOCK_SIZE * NBLOCKS)
    # "my" game board displays my ships with their guesses
    my_board: GameBoard = GameBoard(board_dimension, screen)
    my_board.rect.top = TOP_MARGIN
    my_board.rect.left = PADDING

    # "their" game board displays my guesses with their *sunk* ships
    their_board: GameBoard = GameBoard(board_dimension, screen)
    their_board.rect.top = TOP_MARGIN
    their_board.rect.left = PADDING * 2 + my_board.rect.width

    # --------- BEGIN YOUR CODE ----------
    # add titles above the game boards

    # draw 'YOU' centered above my_board

    # draw 'THEM' centered above their_board

    # --------- END YOUR CODE ----------

    me = players.Human()
    my_board.initialize()
    utilities.draw_ships(my_board, me.state.all_ships())
    my_board.draw()

    their_board.initialize()
    their_board.draw()

    pygame.display.update()

    # wait until the user closes the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                _display_message(screen, "Bye!")
                pygame.display.update()
                pygame.time.wait(1000)
                pygame.quit()
                sys.exit()


def _display_message(screen: pygame.Surface, msg: str):
    """
    Display [msg] in the message box sprite in the center of the screen
    """

    # make a copy of the msg_box sprite because we need to edit it
    box = sprites.msg_box.copy()

    # --------- BEGIN YOUR CODE ----------

    # create a text object with size 42 font of [msg]

    # blit the text onto the box surface

    # blit the box onto the center of the screen

    # remove this once you have implemented the drawing code
    print(msg)

    # --------- END YOUR CODE ----------


if __name__ == "__main__":
    main()
