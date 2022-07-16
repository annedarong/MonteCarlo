import unittest

from numpy import equal
import montecarlo as mc

class TestDie(unittest.TestCase):
    test_die = mc.Die(["H","T"])
    def test_change_weight_throws_exception_face(self):
        with self.assertRaises(Exception):
            self.test_die.change_weight("HT",1)
    

    def test_change_weight_throws_exception_weight(self):
        with self.assertRaises(ValueError):
            self.test_die.change_weight("H","Not real float")

class TestGame(unittest.TestCase):
    test_die = mc.Die(["H","T"])
    test_game = mc.Game([test_die])

    def test_play_normal(self):
        self.test_game.play(100)
        expected = 100
        actual = len(self.test_game.show())
        self.assertEqual(expected,actual)

class TestAnalyzer(unittest.TestCase):
    test_die = mc.Die(["H","T"])
    test_game = mc.Game([test_die])
    test_game.play(100)
    test_analyzer = mc.Analyzer(test_game)

    def test_same_jackpot_count(self):
        count = self.test_analyzer.jackpot()
        actual = len(self.test_analyzer.jackpot_df)
        self.assertEqual(count,actual)


if __name__ == '__main__':
    unittest.main()