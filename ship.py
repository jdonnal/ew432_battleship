class Ship:

    def __init__(self, length: int, row: int,
                 col: int, is_vertical: bool):
        """ Ships are specified by their length, the (row,col)
        coordinate of the bow, and whether they are vertical or
        horizontal. Two examples are illustrated on the board below:

        X = Ship(5,2,4,False)
        Y = Ship(3,5,1,True)

          0|1|2|3|4|5|6|7|8|9|
        A|_|_|_|_|_|_|_|_|_|_|
        B|_|_|_|_|_|_|_|_|_|_|
        C|_|_|_|_|X|X|X|X|X|_|
        D|_|Y|_|_|_|_|_|_|_|_|
        E|_|Y|_|_|_|_|_|_|_|_|
        F|_|Y|_|_|_|_|_|_|_|_|
        G|_|_|_|_|_|_|_|_|_|_|
        H|_|_|_|_|_|_|_|_|_|_|
        I|_|_|_|_|_|_|_|_|_|_|
        J|_|_|_|_|_|_|_|_|_|_|

        """
        self.length = length
        self.row = row
        self.col = col
        self.is_vertical = is_vertical

        # keep track of which parts of the ship are hit
        self._hits = []

    def is_hit(self, guess):
        # ignore duplicate guesses
        if guess in self._hits:
            return True

        # --------- BEGIN YOUR CODE ----------

        # check if the guess corresponds to part of the ship
        # if so add the guess to _hits and return True
        # otherwise return False

        return False  # <-- remove this!
        # --------- END YOUR CODE ----------

    def is_sunk(self):
        return len(self._hits) == self.length
