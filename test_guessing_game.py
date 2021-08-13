import unittest
from guessing_game import compare_numbers

class TestMe(unittest.TestCase):

    def test_low(self):
        self.assertEqual(compare_numbers(16, 23), "You have guessed incorrectly the number is too low ")
    def test_high(self):
        self.assertEqual(compare_numbers(33, 23), "You have guessed incorrectly the number is too high ")
    def test_correct(self):
        self.assertEqual(compare_numbers(23, 23), "You have guessed correctly!")

    def test_invalid(self):
        self.assertRaises(ValueError, compare_numbers, 101, 23)
        self.assertRaises(ValueError, compare_numbers, -4, 23)
        self.assertRaises(TypeError, compare_numbers, 9.8, 23)
        self.assertRaises(TypeError, compare_numbers, "One", 23)




