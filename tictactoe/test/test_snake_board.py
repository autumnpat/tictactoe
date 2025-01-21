import unittest
import board
import snake_board
import player
import logging

class TestSnakeBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)

    def test_empty_snake_board(self):
        blankboard="""\
 | | 
-+-+-
 | | 
-+-+-
 | | \
"""
        b = snake_board.SnakeBoard(3, 3, 3, False)
        self.assertEqual(b.board_state_string(), blankboard)

    def test_snake_win_3x3_goal3(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(3, 3, 3, False)
        # X O -
        # X O -
        # - X -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,1, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_snake_win_4x4_goal3(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(4, 4, 3, False)
        # X O - -
        # O X - -
        # - X O -
        # - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,1, playerx), (2,2, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_straight_win_4x4_goal3(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(4, 4, 3, True)
        # X - - -
        # X O O -
        # X - - -
        # - - - -
        moves = [
            (0,0, playerx), (1,1, playery),
            (1,0, playerx), (1,2, playery),
            (2,0, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_snake_no_win_4x4_goal4(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(4, 4, 4, False)
        # X O - -
        # O X - -
        # - X O -
        # - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,1, playerx), (2,2, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

    def test_snake_win_5x5_goal4(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(5, 5, 4, False)
        # X O - - -
        # X O - - -
        # X O - - -
        # X - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,0, playerx), (2,1, playery),
            (3,0, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_snake_win_5x4_goal3_rectangular(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(5, 4, 3, False)
        # X O - -
        # O X - -
        # - X - -
        # - - - -
        # - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,1, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_snake_win_6x6_goal4_diagonal(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(6, 6, 4, False)
        # X O - - - -
        # O X - - - -
        # - O X - - -
        # - - - X - -
        # - - - - - -
        # - - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,2, playerx), (2,1, playery),
            (3,3, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_straight_no_win_6x6_goal4_diagonal(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(6, 6, 4, True)
        # Same moves as above but with straight=True
        # X O - - - -
        # O X - - - -
        # - O X - - -
        # - - - - - -
        # - - - - X -
        # - - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,2, playerx), (2,1, playery),
            (4,5, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

    def test_out_of_bounds_moves(self):
        playerx = player.Player('X')
        b = snake_board.SnakeBoard(4, 3, 3, False)
        with self.assertRaises(board.IllegalMoveException):
            b.move(4, 0, playerx)
        with self.assertRaises(board.IllegalMoveException):
            b.move(0, 3, playerx)
        with self.assertRaises(board.IllegalMoveException):
            b.move(-1, 0, playerx)

    def test_snake_win_3x5_goal3_rectangular(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(3, 5, 3, False)
        # X O -
        # O X -
        # - X -
        # - - -
        # - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,1, playerx), (1,0, playery),
            (2,1, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_snake_near_miss_5x5_goal4(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(5, 5, 4, False)
        # X O - - -
        # X O - - -
        # X O - - -
        # O - - - -
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,0, playerx), (2,1, playery),
            (3,0, playery)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertEqual(result, playery)

    def test_snake_5x5_goal6_starts_on_right_side(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(5, 5, 6, False)
        # X O - - -
        # X O - X X
        # X O - - X
        # O - X X X
        # - - - - -
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,0, playerx), (2,1, playery),
            (3,0, playery), (1,3, playerx),
            (1,4, playerx), (2,4, playerx),
            (3,4, playerx), (3,3, playerx),
            (3,2, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertEqual(result, playerx)

    def test_snake_5x5_goal6_no_winner(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = snake_board.SnakeBoard(5, 5, 6, False)
        # X O - - -
        # X O - X X
        # X O - - X
        # O - - - -
        # - - X X X
        moves = [
            (0,0, playerx), (0,1, playery),
            (1,0, playerx), (1,1, playery),
            (2,0, playerx), (2,1, playery),
            (3,0, playery), (1,3, playerx),
            (1,4, playerx), (2,4, playerx),
            (4,4, playerx), (4,3, playerx),
            (4,2, playerx)
        ]
        for row, col, p in moves:
            b.move(row, col, p)
        result = b.winner()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
