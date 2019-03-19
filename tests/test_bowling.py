import unittest

import katas.bowling_game.bowling as bowl


class TestBowlingCalculator(unittest.TestCase):

    def setUp(self):
        self.game = bowl.BowlingGame()

    def test_correctly_calculates_if_all_gutters(self):
        self.roll_many(20, 0)
        result = self.game.score()
        self.assertEqual(result, 0)

    def test_correctly_calculates_if_all_ones(self):
        self.roll_many(20, 1)
        result = self.game.score()
        self.assertEqual(result, 20)

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 26)

    def test_all_strikes(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_all_fives(self):
        self.roll_many(21, 5)
        self.assertEqual(self.game.score(), 150)

    def roll_many(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)