import unittest
import logging
import board
import player
import sys

class TestBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)

    def test_empty_board(self):
        blankboard="""\
 | | 
-+-+-
 | | 
-+-+-
 | | \
"""
        b = board.Board()
        self.assertEqual(b.board_state_string(),blankboard)

    def test_move(self):
        markedboard="""\
X| | 
-+-+-
 | | 
-+-+-
 | | \
"""
        playerx = player.Player('X')
        b = board.Board()
        b.move(0,0, playerx)
        self.assertEqual(b.board_state_string(), markedboard)            
        self.assertIsNone(b.winner())
        
    def test_winner(self):
        playerx = player.Player('X')
        playery = player.Player('Y')
        b = board.Board()
        b.move(0,0, playerx)
        b.move(0,1, playery)
        b.move(1,0, playerx)
        self.assertIsNone(b.winner())
        b.move(0,2, playery)
        b.move(2,0, playerx)
        result = b.winner()
        self.assertIsNotNone(result)
        self.assertIsNot(playery, result)
        self.assertIs(playerx, result)

    def test_illegal_move(self):
        playerx = player.Player('X')
        playery = player.Player('Y')
        b = board.Board()
        b.move(0,0, playerx)
        b.move(1,0, playery)
        with self.assertRaises(board.IllegalMoveException):
            b.move(1,0, playerx)

    def test_winner_horizontal_row1(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # X X X
        # O O -
        # - - -
        b.move(0,0, playerx)
        b.move(1,0, playery)
        b.move(0,1, playerx)
        b.move(1,1, playery)
        b.move(0,2, playerx)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_horizontal_row2(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # O - O
        # X X X
        # - - -
        b.move(1,0, playerx)
        b.move(0,0, playery)
        b.move(1,1, playerx)
        b.move(0,2, playery)
        b.move(1,2, playerx)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_vertical_col1(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # X O O
        # X - -
        # X - -
        b.move(0,0, playerx)
        b.move(0,1, playery)
        b.move(1,0, playerx)
        b.move(0,2, playery)
        b.move(2,0, playerx)
        result = b.winner()
        self.assertIs(playerx, result)

    def test_winner_diagonal1(self):
        print("test_winner_diagonal1")
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # X O O
        # - X -
        # - - X
        b.move(0,0, playerx)
        b.move(0,1, playery)
        b.move(1,1, playerx)
        b.move(0,2, playery)
        b.move(2,2, playerx)
        result = b.winner()
        print("-"*30)
        self.assertIs(playerx, result)


    def test_draw_game(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # X O X
        # X O O
        # O X X
        moves = [
            (0,0, playerx), (0,1, playery), (0,2, playerx),
            (1,0, playerx), (1,1, playery), (1,2, playery),
            (2,0, playery), (2,1, playerx), (2,2, playerx)
        ]
        for row, col, myplayer in moves:
            b.move(row, col, myplayer)
        result = b.winner()
        self.assertIsNone(result)

    def test_almost_win_blocked(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # X X O
        # O - -
        # - - -
        b.move(0,0, playerx)
        b.move(1,0, playery)
        b.move(0,1, playerx)
        b.move(0,2, playery)
        result = b.winner()
        self.assertIsNone(result)

    def test_winner_diagonal2(self):
        playerx = player.Player('X')
        playery = player.Player('O')
        b = board.Board()
        # O O X
        # - X -
        # X - O
        b.move(0,2, playerx)
        b.move(0,1, playery)
        b.move(1,1, playerx)
        b.move(0,0, playery)
        b.move(2,0, playerx)
        b.move(2,2, playery)
        result = b.winner()
        self.assertIs(playerx, result)

if __name__ == '__main__':
    unittest.main()
