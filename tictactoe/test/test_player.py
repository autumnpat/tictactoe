import unittest

import player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        p = player.Player('X')
        self.assertEqual(p.get_designation(),"X")

    def test_equal(self):
        p = player.Player("X")
        self.assertTrue(p.equal(p))
        self.assertFalse(p.equal(player.Player("Y")))
        self.assertTrue(p.equal(player.Player("X")))