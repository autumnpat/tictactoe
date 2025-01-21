import unittest
import square
import player

class TestSquare(unittest.TestCase):
    def test_defaultsquare(self):
        sq = square.Square()
        self.assertEqual(sq.get_mark(), " ")

    def test_occupied(self):
        sq = square.Square()
        self.assertFalse(sq.occupied())
        sq.set_player(player.Player("X"))
        self.assertTrue(sq.occupied())