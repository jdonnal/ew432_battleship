from random import randint
from typing import List, Optional, Tuple, Dict

from ship import Ship
from ship import from_dict as ship_from_dict

SHIP_TYPES = [2, 3, 3, 4, 5]


class PlayerState:

    def __init__(self):
        """ Create a valid ship layout
        This function populates
        _my_ships and _board_matrix

        Ship Type  | Length
        -----------|-------
        Carrier    |   5
        Battleship |   4
        Cruiser    |   3
        Submarine  |   3
        Destroyer  |   2

        * the ship type is just FYI, it is not used in the game *
        """

        self._hits: List[Tuple[int, int]] = []
        self._hit = False
        self._misses: List[Tuple[int, int]] = []
        self._ships: List[Ship] = []
        self._hash = ''

    def place_ships(self, debug=False):
        # the board matrix is a 10x10 structure with
        # pointers to ship objects. Initialize to all
        # None values- no ships are on the board
        board_matrix: List[List[Optional[Ship]]] = [[None] * 10 for _ in range(10)]

        # place the ships on the board
        for ship_length in SHIP_TYPES:
            # --------- BEGIN YOUR CODE ----------
            pass  # <-- remove this!
            # --------- END YOUR CODE ----------

        """
        Print the board as text, useful for debugging
        """
        if debug:
            print("=" * 10)
            for row in board_matrix:
                for entry in row:
                    if entry is None:
                        print("_", end="")
                    else:
                        print(entry.length, end="")
                print("")
            print("=" * 10)

    def add_guess(self, guess):
        for ship in self._ships:
            if ship.is_hit(guess):
                self._hits.append(guess)
                self._hit = True
                return
        self._misses.append(guess)
        self._hit = False

    def is_hit(self) -> bool:
        return self._hit

    def all_sunk(self) -> bool:
        # NOTE: Modify the logic below to check if BOTH
        #   1.) All of the ships are present in _ships
        #   2.) All of the ships in _ships are sunk
        # Remote players only send their sunk ships which means it is not sufficient
        # to check if all the Ship objects in _ships are sunk

        # --------- BEGIN YOUR CODE ----------

        # return True if all of the ships are sunk
        # return False otherwise
        return False  # <-- remove this!

        # --------- END YOUR CODE ----------

    def all_ships(self):
        return self._ships

    def sunk_ships(self):
        return [ship for ship in self._ships if ship.is_sunk()]

    def update(self, new_state: 'PlayerState'):
        # update our attributes based on new_state
        # new_state is received from a remote computer

        # add any newly sunken ships
        self._ships = new_state._ships

        # whether or not the last guess was a hit
        self._hit = new_state._hit

    def to_dict(self, reveal=False) -> Dict:
        # if reveal is True, encode all ships
        if reveal:
            ships = self._ships
        # otherwise only encode the sunk ships
        else:
            ships = self.sunk_ships()
        data = {}

        # --------- BEGIN YOUR CODE ----------
        # populate data with the following keys:

        # 'ships': an array of ships encoded as dicts

        # 'hit': the value of _hit

        # --------- END YOUR CODE ----------

        return data


def from_dict(data: Dict) -> PlayerState:
    state = PlayerState()
    # --------- BEGIN YOUR CODE ----------

    # set the _hit and _ships attributes based on the provided data

    # --------- END YOUR CODE ----------
    return state
