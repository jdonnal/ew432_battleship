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
