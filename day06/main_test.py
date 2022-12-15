import unittest

from day06 import main

class MainTestCase(unittest.TestCase):

    def test_get_marker_returns_correct_start_position(self):
        actual = main.get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4)
        self.assertEqual(actual, 7)

    def test_get_marker_returns_correct_start_position2(self):
        actual = main.get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4)
        self.assertEqual(actual, 5)

    def test_get_marker_returns_correct_start_position3(self):
        actual = main.get_marker("nppdvjthqldpwncqszvftbrmjlhg", 4)
        self.assertEqual(actual, 6)

    def test_get_marker_returns_correct_start_position4(self):
        actual = main.get_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
        self.assertEqual(actual, 19)

    def test_get_marker_returns_correct_start_position5(self):
        actual = main.get_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
        self.assertEqual(actual, 23)

    def test_get_marker_returns_correct_start_position6(self):
        actual = main.get_marker("nppdvjthqldpwncqszvftbrmjlhg", 14)
        self.assertEqual(actual, 23)

