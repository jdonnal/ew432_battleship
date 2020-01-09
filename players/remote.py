import json
from typing import Tuple

from .player import Player
from .player_state import PlayerState, from_dict


class Remote(Player):
    """ A remote player"""

    def __init__(self, pipe, priority):
        # whether this player goes first or second
        self.priority = priority
        self.pipe = pipe
        self._state = None

    def get_guess(self) -> Tuple[int, int]:
        # --------- BEGIN YOUR CODE ----------

        # read message (blocks until a complete message arrives)

        # convert binary data into a JSON string

        # convert the JSON string into a guess

        # return the guess
        return 0, 0  # <-- remove this!

        # --------- END YOUR CODE ----------

    def send_guess(self, guess: Tuple[int, int]):

        # --------- BEGIN YOUR CODE ----------

        # encode guess as json string and append a '\n' to terminate the message

        # convert string into binary data

        # send binary data (make sure to flush the pipe)
        pass  # <-- remove this!

        # --------- END YOUR CODE ----------

    def get_state(self) -> PlayerState:

        # --------- BEGIN YOUR CODE ----------

        # read message (blocks until a complete message arrives)

        # convert binary data into a JSON string

        # convert the JSON string into a dictionary

        # convert the dictionary into a PlayerState

        # if _state is None, replace it with the new state
        # otherwise update _state with the new state

        # --------- END YOUR CODE ----------

        return self._state

    def send_state(self, state: PlayerState, reveal=False):

        # --------- BEGIN YOUR CODE ----------

        # encode the state as a dict

        # convert the dict into a JSON string and append a '\n' to terminate the message

        # convert the message string into binary data

        # send binary data (make sure to flush the pipe)
        pass  # <-- remove this!

        # --------- END YOUR CODE ----------

    def close(self):
        self.pipe.close()
