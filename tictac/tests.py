import unittest
import copy
import random
import tictac


class TestCases(unittest.TestCase):
    """Testing class"""

    def setUp(self):
        """Instructions before tests"""
        self.game = tictac.TicTacGame()

    def test_init(self):
        """Initialization test"""

        self.assertEqual(self.game.pos_coords, [0, 0])
        self.assertFalse(self.game.correct_inp)
        self.assertEqual(self.game.occupied_num, 0)
        for i in range(3):
            for j in range(3):
                with self.subTest(i=i, j=j):
                    self.assertEqual(self.game.board[i][j], '_')

    def test_validate(self):
        """Validation test"""

        self.assertRaises(tictac.WrongInp, self.game.validate_input, "-2,3")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "1, 1")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "2.5,0")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "0,1,2,3")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "1")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "qwerty")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "qwerty,abc")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, " 1, 5")
        self.assertRaises(tictac.WrongInp, self.game.validate_input, "2,5")
        self.game.board[1][1] = 'x'
        self.game.board[0][2] = 'o'
        self.assertRaises(tictac.Occupied, self.game.validate_input, "1,1")
        self.assertRaises(tictac.Occupied, self.game.validate_input, "0,2")
        self.game.validate_input("1,2")
        self.assertEqual(self.game.pos_coords, [1, 2])
        self.game.validate_input("0,1")
        self.assertEqual(self.game.pos_coords, [0, 1])

    def test_play(self):
        """Draw test"""

        self.game.board[0][0] = self.game.board[0][1] = 'x'
        self.game.board[1][2] = self.game.board[2][0] = 'x'
        self.game.board[0][2] = self.game.board[1][0] = 'o'
        self.game.board[1][1] = self.game.board[2][1] = self.game.board[2][2] = 'o'
        self.game.occupied_num = 9
        self.assertEqual(self.game.play_game(), "It is a draw!")

    def test_win_check(self):
        """Check_winner function test"""
        for i in range(10):
            curboard = copy.deepcopy(self.game.board)
            if i < 3:
                curboard[i][0], curboard[i][1], curboard[i][2] = 'x', 'x', 'x'
                with self.subTest(i=i):
                    self.assertTrue(self.game.check_winner(curboard))
            elif i < 6:
                curboard[0][i % 3], curboard[1][i % 3], curboard[2][i % 3] = 'o', 'o', 'o'
                with self.subTest(i=i):
                    self.assertTrue(self.game.check_winner(curboard))
            elif i == 6:
                curboard[0][0], curboard[1][1], curboard[2][2] = 'x', 'x', 'x'
                self.assertTrue(self.game.check_winner(curboard))
            elif i == 7:
                curboard[0][2], curboard[1][1], curboard[2][0] = 'o', 'o', 'o'
                self.assertTrue(self.game.check_winner(curboard))
            else:
                i, j = random.randint(0, 2), random.randint(0, 2)
                curboard[i][j] = 'x'
                self.assertFalse(self.game.check_winner(curboard))
