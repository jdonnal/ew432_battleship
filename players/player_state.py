from random import randint
from typing import List, Optional, Tuple

from ship import Ship

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

    def all_ships(self):
        return self._ships

