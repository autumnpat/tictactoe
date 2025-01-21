# Core tic-tac-toe implementation

This is a generic tic-tac-toe implementation that allows for an NxM board with variable length goals and variable number of participants and a variation that allows for non-straight lines.

The design of the project is as follows:

## Board
The `Board` class is a 3x3 with a 3 straight line goal implementation (classic tic-tac-toe).  This also serves as the foundation for the logic of the goal and basic edge-case enforcement (bounds testing, winning determination, etc.)

## VariableBoard
`VariableBoard` extends the `Board` class by allowing the board to be initialized with a MxN sized board and a variable goal size (e.g., 4 in a row in a 8x10 board).

## SnakeBoard
`SnakeBoard` extends the `VariableBoard` class by allowing the goal to be reached, optionally, by a non-linear pattern of connected occupied squares of a variable goal length.

## Player
The `Player` class represents a player in the game.  A `Square` can have a `Player` occupant, and the `winner` method in the `Board` implementation will return a `Player` winner if one is available.

## Square
The `Board` is made of `Square` objects representing the spaces.  Using instances of a class to represent the squares on the board allows us to potentially modify the board later on by creating other things besides `Player` objects that can occupy it.

## Testing
The testing can be exercised by running `python3 -m unittest discover -s test`.  There is also a script `runtests.sh` that will run the unit testing every time files are saved to disk.  The tests are all located in the `test` directory.