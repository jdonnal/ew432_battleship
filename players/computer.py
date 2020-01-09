from random import randint
import time
from typing import List, Tuple

from .player import Player
from .player_state import PlayerState


class Computer(Player):
    """ A computer player"""

    def __init__(self):
        self.priority = 1
        # list of board spaces that have not been guessed
        # eg: _unguessed_spaces = [(0,0), (0,1), (0,2),...]
        self._unguessed_spaces = []

        # --------- BEGIN YOUR CODE ----------

        # Populate _unguessed_spaces with every possible board space
        # Hint: use two nested for loops

        # --------- END YOUR CODE ----------

        self.state = PlayerState()
        # the debug flag prints ship locations to the terminal
        self.state.place_ships(debug=True)

    def get_state(self):
        return self.state

    def get_guess(self) -> Tuple[int, int]:
        # --------- BEGIN YOUR CODE ----------

        # guess a random entry from _unguessed_spaces

        # remove the guess from _unguessed_spaces

        # enforce a short delay to make the computer
        # appear to "think" about its guess
        time.sleep(0.5)

        return 0, 0  # <-- remove this!

        # --------- END YOUR CODE ----------

    def send_guess(self, guess: Tuple[int, int]):
        self.state.add_guess(guess)

