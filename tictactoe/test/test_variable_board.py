import unittest
import player
import board
import logging
import variable_board

class TestVariableBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)

    def test_empty_5x5_board(self):
        blankboard="""\
 | | | | 
-+-+-+-+-
 | | | | 
-+-+-+-+-
 | | | | 
-+-+-+-+-
 | | | | 
-+-+-+-+-
 | | | | \
"""
        b = variable_board.VariableBoard(5,5,4)
        self.assertEqual(b.board_state_string(), blankboard)

    def test_winner_horizontal_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X X X X -
        # O O O - -
        # - - - - -
        # - - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (1,0, playery),
            (0,1, playerx), (1,1, playery),
            (0,2, playerx), (1,2, playery),
            (0,3, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_vertical_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X O - - -
        # X O - - -
        # X - - - -
        # X - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,0, playerx),
            (3,0, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_diagonal_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X O - - -
        # O X O - -
        # - O X - -
        # - - O X -
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,2, playerx), (1,2, playery),
            (3,3, playerx), (2,1, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_reverse_diagonal_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # - - - X -
        # - - X - -
        # - X O - -
        # X O - - -
        # O - - - -
        moves = [
            (0,3, playerx), (4,0, playery),
            (1,2, playerx), (3,1, playery),
            (2,1, playerx), (2,2, playery),
            (3,0, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_no_winner_three_in_row_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X X X - -
        # O O - - -
        # - - - - -
        # - - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (1,0, playery),
            (0,1, playerx), (1,1, playery),
            (0,2, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

    def test_winner_middle_horizontal_5x5(self):
        print("test_winner_middle_horizontal_5x5")
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # - O - - -
        # - X X X X
        # - O O O -
        # - - - - -
        # - - - - -
        moves = [
            (1,1, playerx), (0,1, playery),
            (1,2, playerx), (2,1, playery),
            (1,3, playerx), (2,2, playery),
            (1,4, playerx), (2,3, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        print("~"*30)
        self.assertIs(playerx, result)

    def test_winner_left_horizontal_5x5(self):
        print("test_winner_middle_horizontal_5x5")
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # - O - - -
        # X X X X -
        # - O O O -
        # - - - - -
        # - - - - -
        moves = [
            (1,0, playerx), (0,1, playery),
            (1,1, playerx), (2,1, playery),
            (1,2, playerx), (2,2, playery),
            (1,3, playerx), (2,3, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        print("~"*30)
        self.assertIs(playerx, result)

    def test_blocked_win_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X X X O -
        # O O - - -
        # - - - - -
        # - - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (1,0, playery),
            (0,1, playerx), (1,1, playery),
            (0,2, playerx), (0,3, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

    def test_draw_game_partial_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        # X O X O X
        # O X O X O
        # X O X O X
        # - - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery), (0,2, playerx), (0,3, playery), (0,4, playerx),
            (1,0, playery), (1,1, playerx), (1,2, playery), (1,3, playerx), (1,4, playery),
            (2,0, playerx), (2,1, playery), (2,2, playerx), (2,3, playery), (2,4, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

    def test_illegal_move_5x5(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = variable_board.VariableBoard(5,5,4)
        b.move(0,0, playerx)
        with self.assertRaises(board.IllegalMoveException):
            b.move(0,0, playery)

    def test_out_of_bounds_move_5x5(self):
        playerx = player.Player('X')
        b = variable_board.VariableBoard(5,5,4)
        with self.assertRaises(board.IllegalMoveException):
            b.move(5,0, playerx)
        with self.assertRaises(board.IllegalMoveException):
            b.move(0,5, playerx)
        with self.assertRaises(board.IllegalMoveException):
            b.move(-1,0, playerx)


if __name__ == '__main__':
    unittest.main()
