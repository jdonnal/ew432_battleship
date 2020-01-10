import pygame
import sys
from pygame.locals import *

import players
import utilities


class Engine:

    def __init__(self, player1, board1, player2, board2):
        self.player1 = player1
        self.board1 = board1
        self.player2 = player2
        self.board2 = board2

    def play(self) -> players.Player:
        player2_hits = []
        player2_misses = []
        player1_hits = []
        player1_misses = []

        while True:
            # ==== Player1's turn ====
            guess = self.player1.get_guess()
            self.player2.send_guess(guess)

            player2_state = self.player2.get_state()
            self.player1.send_state(player2_state)

            if player2_state.is_hit():
                player2_hits.append(guess)
            else:
                player2_misses.append(guess)

            utilities.draw_ships(self.board2, player2_state.sunk_ships())
            utilities.draw_hits(self.board2, player2_hits)
            utilities.draw_misses(self.board2, player2_misses)
            self.board2.draw()
            pygame.display.update()

            # Did Player1 win?
            if player2_state.all_sunk():
                # share all of Player1's ships with Player2 (both sunk and unsunk)
                # this way if Player2 is remote, they can verify that Player1 did not cheat
                player1_solved_state = self.player1.get_state()
                self.player2.send_state(player1_solved_state, reveal=True)
                # verify for ourselves that Player1 did not cheat
                if not player1_solved_state.is_valid():
                    print("Player 1 cheated!")
                else:
                    print("Player1 played a fair game")
                return self.player1

            # ==== Player2's turn ====

            # NOTE: Following the pattern above, implement cheat detection for Player2

            # --------- BEGIN YOUR CODE ----------

            # Following the pattern above implement the logic for Player2's turn

            # --------- END YOUR CODE ----------

            # process event queue, quit if user clicks 'X' button
            # if you don't do this the game will appear frozen
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
