# EW432 Battleship Game

Complete the lab assignments by adding code inside the markers (example shown below):
    
    # --------- BEGIN YOUR CODE ----------
    
      your code goes here!
    
    # --------- END YOUR CODE ----------

Do **not** add any code outside of these markers, it may prevent you from merging subsequent labs.


Lab 1: Introduction to PyGame
-----------------------------
By the end of this lab you should have two empty battleship boards displayed side by side.
Code is required in the following locations:

| File Name       | Function:Line     | Description      |
|-----------------|-------------------|------------------|
|``main.py``      |``main:36``        | draw board titles|
|``game_board.py``| ``initialize:50`` | draw game board  |


Lab 2: Working with Objects
---------------------------
By the end of this lab you should have ships displayed on your battleship board.
When you close the game a message box with "Bye!" should display for one second.
Code is required in the following locations:

| File Name         | Function:Line         | Description           |
|-------------------|-----------------------|-----------------------|
|``main.py``        |``display_message:73`` | show a message box    |
|``utilities.py``   |``draw_ships:18``      | draw ships on a board |
|``player_state.py``| ``place_ships:43``    | randomly place ships  |
|``sprites.py``     | ``--global--:28``     | create sprite objects |


Lab 3: Playing the Computer
---------------------------
By the end of this lab you should be able to play a game of battleship against
your computer. Code is required in the following locations:

| File Name          | Function:Line     | Description                    |
|--------------------|-------------------|--------------------------------|
|``human.py``        | ``get_guess:26``  | get a guess from the keyboard  |
|``computer.py``     | ``__init__:20``   | initialize _unguessed_spaces   |
|``computer.py``     | ``get_guess:34``  | make a random guess            |
|``engine.py``       | ``play:55``       | run player2's turn             |
|``utilities.py``    | ``draw_hits:26``  | add hit sprites to a board     |
|``utilities.py``    | ``draw_misses:35``| add miss sprites to a board    |
|``player_state.py`` | ``all_sunk:72``   | determine if a player has lost |
|``ship.py``         | ``is_hit:38``     | determine if a ship is hit     |
