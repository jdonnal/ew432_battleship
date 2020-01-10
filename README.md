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

Lab 4: Playing Local Games
--------------------------
By the end of this lab you should be able to play a game of battleship against a local opponent
with a USB serial connection. Code is required in the following locations:

| File Name          | Function:Line                | Description                              |
|--------------------|------------------------------|------------------------------------------|
|``remote.py``       | ``get_guess:18``             | get a guess from another computer        |
|``remote.py``       | ``send_guess:31``            | send a guess to another computer         |
|``remote.py``       | ``get_state:44``             | get a PlayerState from another computer  |
|``remote.py``       | ``send_state:65``            | send a PlayerState to another computer   |
|``comms.py``        | ``connect_serial_client:44`` | connect to an existing battleship server |
|``player_state.py`` | ``to_dict:106``              | encode PlayerState as a dictionary       |
|``player_state.py`` | ``from_dict:119``            | create PlayerState from a dictionary     |
|``player_state.py`` | ``all_sunk:72``              | update logic to handle remote players    |
|``ship.py``         | ``to_dict:58``               | encode Ship as a dictionary              |
|``ship.py``         | ``from_dict:67``             | create a Ship from a dictionary          |

Lab 5: Playing Remote Games
---------------------------
By the end of this lab you should be able to play a game of battleship against a remote opponent
over a network connection. You should also be able to detect if your opponent cheated. Code is
required in the following locations:

| File Name          | Function:Line                | Description                              |
|--------------------|------------------------------|------------------------------------------|
|``engine.py``       | ``play:59``                  | add cheat detection for player2          |
|``player_state.py`` | ``to_dict:125``              | add hash to dict encoding                |
|``player_state.py`` | ``from_dict:155``            | set hash from dict encoding              |
|``player_state.py`` | ``is_valid:155``             | verify PlayerState                       |
|``comms.py``        | ``host_tcp_server:61``       | host a battleship server                 |
|``comms.py``        | ``connect_tcp_client:79``    | connect to an existing battleship server |
