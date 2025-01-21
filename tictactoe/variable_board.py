import board

class VariableBoard(board.Board):
    """
    VariableBoard allows any size board
    """
    def __init__(self, xsize, ysize, goal):
        print ("VariableBoard.__init__")
        self.do_initialization(xsize, ysize, goal)    