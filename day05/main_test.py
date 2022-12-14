import unittest

from day05 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.crane_data = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
            ]

    def test_parse_data_returns_correct_crate_positions(self):
        c, _ = main.parse_data(self.crane_data)
        self.assertEqual(c[1], ["Z", "N"])
        self.assertEqual(c[2], ["M", "C", "D"])
        self.assertEqual(c[3], ["P"])

    def test_parse_data_returns_correct_instructions(self):
        _, i = main.parse_data(self.crane_data)
        self.assertEqual(i[0], [1, 2, 1])
        self.assertEqual(i[1], [3, 1, 3])
        self.assertEqual(i[2], [2, 2, 1])
        self.assertEqual(i[3], [1, 1, 2])

    def test_move_crates_returns_correct_stack(self):
        [c, i] = main.parse_data(self.crane_data)
        main.move_crates(c, i[0])
        self.assertEqual(c[1], ["Z","N", "D"])
        self.assertEqual(c[2], ["M", "C"])
        self.assertEqual(c[3], ["P"])

    def test_move_all_crates_returns_correct_stack(self):
        [c, i] = main.parse_data(self.crane_data)
        main.move_all_crates(c, i)
        self.assertEqual(c[1], ["C"])
        self.assertEqual(c[2], ["M"])
        self.assertEqual(c[3], ["P", "D", "N", "Z"])

    def test_move_all_crates_no_reverse_returns_correct_stack(self):
        [c, i] = main.parse_data(self.crane_data)
        main.move_all_crates(c, i, False)
        self.assertEqual(c[1], ["M"])
        self.assertEqual(c[2], ["C"])
        self.assertEqual(c[3], ["P", "Z", "N", "D"])

    def test_get_state_returns_correct_value(self):
        [c, i] = main.parse_data(self.crane_data)
        main.move_all_crates(c, i)
        actual = main.get_state(c)
        self.assertEqual(actual, "CMZ")