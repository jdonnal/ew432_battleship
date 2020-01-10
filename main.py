import pygame
from pygame.locals import *
import sys
import argparse

import comms
import engine
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

    # parse command line arguments
    parser = argparse.ArgumentParser("Battleship Simulator")
    parser.add_argument("--type", "-t", choices=['cpu', 'serial-server', 'serial-client',
                                                 'tcp-server', 'tcp-client'], default='cpu')
    parser.add_argument("--interface", "-i", help="serial device, port or IP address:PORT")
    args = parser.parse_args()

    # determine the type of opponent
    if args.type == 'cpu':
        them = players.Computer()
    elif args.type == 'serial-server':
        (priority, file) = comms.host_serial_server(args.interface)
        them = players.Remote(file, priority=priority)
    elif args.type == 'serial-client':
        (priority, file) = comms.connect_serial_client(args.interface)
        them = players.Remote(file, priority=priority)
    elif args.type == 'tcp-server':
        (priority, file) = comms.host_tcp_server(args.interface)
        them = players.Remote(file, priority=priority)
    elif args.type == 'tcp-client':
        (priority, file) = comms.connect_tcp_client(args.interface)
        them = players.Remote(file, priority=priority)
    else:
        print("Invalid player type")
        return

    me = players.Human()
    my_board.initialize()
    utilities.draw_ships(my_board, me.state.all_ships())
    my_board.draw()

    their_board.initialize()
    their_board.draw()

    pygame.display.update()

    # Create an engine to run the game
    if me.priority > them.priority:
        # I go first
        game = engine.Engine(me, my_board, them, their_board)
    else:
        # They go first
        game = engine.Engine(them, their_board, me, my_board)

    # Play battleship!
    winner = game.play()

    # Display the winner in a message box
    if winner == me:
        _display_message(screen, "You Win!")
    elif winner == them:
        _display_message(screen, "You Lose!")

    # wait until the user closes the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                _display_message(screen, "Bye!")
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
