import unittest

from day09 import main
from day09.main import Point, Rope

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.moves_input = [
            "R 4",
            "U 4",
            "L 3",
            "D 1",
            "R 4",
            "D 1",
            "L 5",
            "R 2"
        ]

        self.moves_input_large = [
            "R 5",
            "U 8",
            "L 8",
            "D 3",
            "R 17",
            "D 10",
            "L 25",
            "U 20"
        ]

    def test_process_moves_returns_correct_visited_count_first_knot(self):
        rope = main.process_moves(self.moves_input, 2)
        actual = rope.count_tail_visited_points(1)
        self.assertEqual(actual, 13)

    def test_process_moves_returns_correct_visited_count_last_knot(self):
        rope = main.process_moves(self.moves_input_large, 10)
        actual = rope.count_tail_visited_points(9)
        self.assertEqual(actual, 36)
