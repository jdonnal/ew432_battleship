import string
from typing import Tuple

from .player import Player
from .player_state import PlayerState


class Human(Player):
    """ A human player"""

    def __init__(self):
        self.priority = 2
        self.state = PlayerState()
        # add ships to the board randomly
        self.state.place_ships()

    def get_state(self, all_ships=False):
        return self.state

    def get_guess(self) -> Tuple[int, int]:
        """
        Prompt the user to guess a row and column. The user should enter a lower case letter
        followed by a number.
        """

        # --------- BEGIN YOUR CODE ----------

        # Prompt user for a guess. Valid input would be a string like c,4
        # If the guess is not valid ask the user to enter another guess

        return 0, 0  # <-- remove this!

        # --------- END YOUR CODE ----------

    def send_guess(self, guess: Tuple[int, int]):
        self.state.add_guess(guess)
