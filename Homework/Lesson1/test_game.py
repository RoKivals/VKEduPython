import unittest
from io import StringIO

from player import *
from tic_tac_game import *

win_tactics = [((0, 0), (1, 1), (2, 2)), ((0, 0), (0, 1), (0, 2)), ((0, 0), (0, 1), (0, 2))]
lose_tactics = [((0, 0), (1, 2), (2, 2)), ((1, 0), (0, 1), (0, 2)), ((1, 1), (2, 1), (0, 2))]


class TestGame(unittest.TestCase):

    def test_win(self):
        player = Player("name", 'X')
        for i in range(len(win_tactics)):
            with self.subTest(i=i):
                self.game = TicTacGame()
                for x, y in win_tactics[i]:
                    self.game.field[x][y] = 'X'
                else:
                    self.assertTrue(self.game.check_win(x, y, player))

    def test_lose(self):
        player = Player("name", 'X')
        for i in range(len(lose_tactics)):
            with self.subTest(i=i):
                self.game = TicTacGame()
                for x, y in lose_tactics[i]:
                    self.game.field[x][y] = 'X'
                else:
                    self.assertFalse(self.game.check_win(x, y, player))


    def test_change_size(self):
        self.game = TicTacGame()
        self.game.change_size('12')
        self.assertEqual(12, self.game.size)


if __name__ == '__main__':
    main()
